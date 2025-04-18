# Multi-Factor Authentication (MFA) Project

## Overview
This project, developed by Group 8, focuses on implementing a secure and user-friendly Multi-Factor Authentication (MFA) system. MFA enhances security by requiring users to provide multiple forms of verification to access a system.

## Features
- **Two-Factor Authentication (2FA):** Combines password-based authentication with an additional verification method.
- **Support for Multiple Factors:** Includes options like SMS, email, and authenticator apps.
- **Secure Token Generation:** Uses time-based one-time passwords (TOTP) for enhanced security.
- **User-Friendly Interface:** Simplifies the authentication process for end-users.
- **Scalable Design:** Suitable for small to large-scale applications.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo/multi-factor_authentication.git
    ```
2. Navigate to the project directory:
    ```bash
    cd multi-factor_authentication
    ```
3. Install dependencies, make migrations and run server:
    ```bash
    pip install -r requirements.txt
    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py runserver
    ```
2. Access the application at `http://localhost:3000`.
3. Follow the on-screen instructions to set up MFA for your account.

## Technologies Used
- **Backend:** Python
- **Frontend:** html, css, bootstrap
- **Database:** sqlite3
- **Authentication:** TOTP

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-name
    ```
3. Commit your changes and push to your fork.
4. Submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For questions or support, please contact Group 8 at `dave@gmail.com`.