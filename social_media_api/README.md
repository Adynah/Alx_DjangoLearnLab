# Social Media API

A Django REST Framework-based Social Media API that supports user registration, login, and profile management with token-based authentication.

---

## Project Overview

This project implements the foundational backend of a social media platform. It allows users to:

- Register an account
- Log in and receive an authentication token
- Manage basic profile information (bio, profile picture)
- Follow and be followed by other users (future enhancement)

Built using **Django** and **Django REST Framework (DRF)** with token-based authentication.

---

## Installation and Setup

### 1. Clone the Repository

git clone <>
cd social_media_api

### 2. Create Virtual Environment
python -m venv venv

### 3. Install Dependencies
pip install django djangorestframework djangorestframework-simplejwt Pillow

### 4. Apply Migrations
python manage.py makemigrations
python manage.py migrate

### 5. Create Superuser
python manage.py createsuperuser

### 6. Run the Development Server
python manage.py runserver

## User Model
Custom user model CustomUser extends Django’s AbstractUser

| Field             | Type              | Description                |
| ----------------- | ----------------- | -------------------------- |
| `username`        | `CharField`       | Unique username            |
| `email`           | `EmailField`      | Unique email address       |
| `password`        | `CharField`       | User password (hashed)     |
| `bio`             | `TextField`       | Optional user biography    |
| `profile_picture` | `ImageField`      | Optional profile image     |
| `followers`       | `ManyToManyField` | Users who follow this user |

## API Endpoints

### Base URL: /api/accounts/

1. Register User
- URL: /register/
- Method: POST
- Description: Creates a new user and returns an authentication token.
- Request Body:
    {
      "username": "testuser",
      "email": "test@example.com",
      "password": "StrongPass123",
      "bio": "Hello, I am a new user!",
      "profile_picture": "<file>"
    }
- Response Example:
{
  "id": 1,
  "username": "testuser",
  "email": "test@example.com",
  "bio": "Hello, I am a new user!",
  "profile_picture": "profile_pics/user1.png",
  "token": "0123456789abcdef0123456789abcdef01234567"
}
2. Login User
- URL: /login/
- Method: POST
- Description: Authenticates user and returns a token.
- Request Body:
{
  "username": "testuser",
  "password": "StrongPass123"
}
- Response Example:
{
  "token": "0123456789abcdef0123456789abcdef01234567"
}

### Testing the API

Use Postman or cURL:
curl -X POST http://127.0.0.1:8000/api/accounts/register/ \
-H "Content-Type: application/json" \
-d '{"username": "testuser", "email": "test@example.com", "password": "StrongPass123"}'

## Folder Structure
social_media_api/
├── accounts/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── social_media_api/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── README.md
