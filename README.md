# Django Rest Framework (DRF)
# Project 1: Password Reset System

This project demonstrates how to build a password reset system using Django Rest Framework (DRF). It incorporates user authentication, JWT token-based authorization, and email OTP verification for secure password reset functionality.

## Features

- **Django Built-in User Model**
  - Utilizes the default Django user model for authentication.

- **Signup and Signin**
  - Provides endpoints to allow users to register and log in.

- **JWT Token Authentication**
  - Implements JSON Web Token (JWT) for secure authentication and authorization.

- **Send OTP to Email**
  - Sends a One-Time Password (OTP) to the user's registered email for verification.

- **Password Reset**
  - Allows users to reset their passwords by verifying the OTP sent to their email.

## Getting Started

### Prerequisites

- Python 3.x
- Django 3.x or higher
- Django Rest Framework (DRF)
- JWT Authentication Library (`djangorestframework-simplejwt`)
- Email backend configuration (e.g., Gmail, SMTP)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/snrredoy/drf_simple_projects/tree/main/reset%20password
