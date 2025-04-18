from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('', views.landing, name='landing'),  # Set landing page as the root path
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout, name='logout'),
    path('add-villager/', views.add_villager, name='add_villager'),
]
