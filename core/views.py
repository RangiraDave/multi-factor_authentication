from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.mail import send_mail
from django.utils.timezone import now
from .models import User, OTP, Villager
import random
from django.conf import settings

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        phone = request.POST.get('phone', '')
        if User.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error': 'User already exists'})  # Show error message
        user = User(email=email, phone=phone)
        user.set_password(password)
        user.save()

        # Generate and send OTP
        otp_code = str(random.randint(100000, 999999))
        OTP.objects.create(email=email, code=otp_code)
        send_mail(
            'Verify Your Email',
            f'Your OTP is {otp_code}',
            settings.EMAIL_HOST_USER,  # Use EMAIL_HOST_USER dynamically
            [email]
        )

        # Store email in session and redirect to OTP verification page
        request.session['email'] = email
        return redirect('verify_otp')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.filter(email=email).first()
        if not user or not user.check_password(password):
            return render(request, 'login.html', {'error': 'Invalid credentials'})  # Show error message
        otp_code = str(random.randint(100000, 999999))
        OTP.objects.create(email=email, code=otp_code)
        send_mail(
            'Your OTP Code',
            f'Your OTP is {otp_code}',
            settings.EMAIL_HOST_USER,  # Ensure this is not None
            [email]
        )
        request.session['email'] = email
        return redirect('verify_otp')  # Redirect to OTP verification page
    return render(request, 'login.html')

def verify_otp(request):
    if request.method == 'POST':
        otp_code = request.POST['otp']
        email = request.session.get('email')
        otp = OTP.objects.filter(email=email, code=otp_code).first()
        if not otp or otp.is_expired():
            return render(request, 'verify_otp.html', {'error': 'Invalid or expired OTP'})  # Show error message
        request.session['authenticated'] = True
        otp.delete()
        return redirect('home')  # Redirect to home after successful verification
    return render(request, 'verify_otp.html')

def home(request):
    if not request.session.get('authenticated'):
        return redirect('login')

    villagers = Villager.objects.all()

    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        occupation = request.POST.get('occupation', '')
        Villager.objects.create(name=name, age=age, occupation=occupation)
        return redirect('home')

    return render(request, 'home.html', {'villagers': villagers})

def add_villager(request):
    if not request.session.get('authenticated'):
        return redirect('login')

    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        occupation = request.POST.get('occupation', '')
        Villager.objects.create(name=name, age=age, occupation=occupation)
        return redirect('home')

    return render(request, 'add_villager.html')

def logout(request):
    request.session.flush()
    return redirect('login')

def landing(request):
    villagers = Villager.objects.all()
    return render(request, 'landing.html', {'villagers': villagers})
