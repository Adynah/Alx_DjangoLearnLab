# Django Blog – Authentication Documentation
## 1. Overview

The authentication system allows users to:
- Register a new account
- Login to the blog
- Logout securely
- View and edit their profile

It is implemented using a combination of Django’s built-in authentication views and custom views for registration and profile management.

## 2. Project Structure for Authentication

django_blog/
├─ blog/
│  ├─ templates/
│  │  ├─ blog/
│  │  │  └─ base.html
│  │  └─ registration/
│  │     ├─ login.html
│  │     ├─ register.html
│  │     ├─ profile.html
│  │     └─ logged_out.html
│  ├─ views.py
│  ├─ urls.py
│  └─ forms.py
├─ django_blog/
│  ├─ settings.py
│  └─ urls.py

## 3. URL Configuration
/register/	---  registration/register.html
/login/	 ---	registration/login.html	
/logout/	---	registration/logged_out.html
/profile/	---	registration/profile.html
/admin/	---	admin login page
/	---	home.html

## 4. Views
### Registration (register_view)
- Handles GET: displays a blank registration form.
- Handles POST: validates and saves the user account.
- Redirects to /login/ on success.
### Login (LoginView)
- Uses Django’s built-in authentication.
- Handles POST to check username and password.
- Redirects to next URL if present, or to LOGIN_REDIRECT_URL.
### Logout (LogoutView)
- Ends the user session.
- Redirects to the logged out page.
### Profile (profile_view)
- Displays user information.
- Allows editing of fields like email.
- Protected by @login_required decorator.

## 5. Forms
- UserCreationForm: Default Django form for creating new users.
- Can be extended to include extra fields like email, profile picture, or bio.

## 6. Templates
- All templates use {% csrf_token %} to protect against CSRF attacks.
- Form errors are displayed automatically using {{ form.as_p }}.
- Templates are styled using blog/static/css/styles.css.

## 7. Security Considerations
- Passwords are hashed using Django’s default password hasher.
- All forms use CSRF protection.
- Login and profile pages are protected by authentication checks (@login_required).
- Admin panel is restricted to staff/superuser accounts.

## 8. Testing Guide
- Visit /register/ and create a new user.
- Log in via /login/ with the newly created credentials.
- Check that you can log out via /logout/.
- Access /profile/ and ensure user info is displayed and editable.
- Try accessing /admin/ with a regular user → should redirect to login.
- Log in as superuser → /admin/ should be accessible.