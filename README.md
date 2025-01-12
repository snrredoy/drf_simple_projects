# Effective DRF Project: Password Reset Implementation

This project is a simple yet effective Django REST Framework (DRF) project that demonstrates how to implement a password reset feature. It includes essential authentication and authorization tools, such as JWT token authentication, email OTP verification, and password reset functionality.

## Features

- **Django Built-in User Model**: Use Django's built-in user management for handling authentication and registration.
- **Sign In and Sign Up**: Secure user sign-in and sign-up functionality.
- **JWT Token Authentication**: Uses JSON Web Token (JWT) for authentication.
- **OTP to Email**: Sends One-Time Password (OTP) to the user's email for verification during the password reset process.
- **Password Reset**: Allows users to securely reset their passwords through OTP verification.

## Project Structure

1. **User Authentication & Management**
   - Django Built-in User
   - Sign In & Sign Up Endpoints
   - JWT Authentication for secure access

2. **Password Reset**
   - Generate and send OTP to the user's email
   - Verify OTP and reset the password securely

## Installation

### Prerequisites

Make sure you have the following installed:
- Python 3.x
- Django
- Django REST Framework
- JWT Authentication libraries (e.g., `djangorestframework-simplejwt`)
- Email service (for sending OTP via email)

### Steps to Install

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/effective-drf-password-reset.git

