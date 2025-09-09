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


# Social Media API – Posts & Comments

This section of the Social Media API allows users to create, view, edit, and delete posts and comments. It also includes pagination, filtering, and permissions to ensure users can only modify their own content.

## Models

### Post
| Field       | Type                  | Description                          |
|------------|----------------------|--------------------------------------|
| author   | ForeignKey (User)     | User who created the post            |
| title    | CharField             | Title of the post                    |
| content  | TextField             | Body content of the post             |
| created_at | DateTimeField       | Timestamp when post was created     |
| updated_at | DateTimeField       | Timestamp when post was last updated|

### Comment
| Field       | Type                  | Description                          |
|------------|----------------------|--------------------------------------|
| post     | ForeignKey (Post)     | Post the comment belongs to          |
| author   | ForeignKey (User)     | User who wrote the comment           |
| content  | TextField             | Body content of the comment          |
| created_at | DateTimeField       | Timestamp when comment was created  |
| updated_at | DateTimeField       | Timestamp when comment was last updated|


## Serializers

- PostSerializer: Serializes posts and displays author username.
- CommentSerializer: Serializes comments and displays author username.

## Views

- PostViewSet: CRUD operations for posts.
  - Users can only edit/delete their own posts.
  - Supports search by title/content.
  - Pagination implemented.
- CommentViewSet: CRUD operations for comments.
  - Users can only edit/delete their own comments.
  - Pagination implemented.

## API Endpoints

| Endpoint                  | Method | Description                                         |
|----------------------------|--------|-----------------------------------------------------|
| /api/posts/              | GET    | List all posts (paginated)                          |
| /api/posts/              | POST   | Create a new post (authenticated users only)       |
| /api/posts/{id}/         | GET    | Retrieve a specific post                            |
| /api/posts/{id}/         | PUT/PATCH | Update a post (author only)                        |
| /api/posts/{id}/         | DELETE | Delete a post (author only)                         |
| /api/comments/           | GET    | List all comments (paginated)                       |
| /api/comments/           | POST   | Create a new comment (authenticated users only)    |
| /api/comments/{id}/      | GET    | Retrieve a specific comment                         |
| /api/comments/{id}/      | PUT/PATCH | Update a comment (author only)                     |
| /api/comments/{id}/      | DELETE | Delete a comment (author only)                      |


### Pagination
- Default page size: 10 items per page.
- Page size can be customized via query param 'page_size'.
- Example:  GET /api/posts/?page=2&page_size=5

### Filtering & Search
- Search posts by 'title' or 'content' using query parameter 'search'.
- Example: GET /api/posts/?search=django

### Testing
- Use 'Postman' or 'cURL' to test all endpoints.
- Verify:
- Only authors can update/delete their posts/comments.
- Pagination works.
- Search returns expected results.
- Data integrity is maintained.

Example: Create a Post
POST /api/posts/
Authorization: Token <user_token>
Content-Type: application/json

{
"title": "My First Post",
"content": "This is the content of my post."
}

Example: Create a Comment
POST /api/comments/
Authorization: Token <user_token>
Content-Type: application/json

{
  "post": 1,
  "content": "Great post!"
}

### Follow Endpoints

| Endpoint                            | Method | Description                                |
| ----------------------------------- | ------ | ------------------------------------------ |
| `/api/accounts/follow/<user_id>/`   | POST   | Follow a user (authenticated users only)   |
| `/api/accounts/unfollow/<user_id>/` | POST   | Unfollow a user (authenticated users only) |

### Feed Endpoint

| Endpoint           | Method | Description                                                                  |
| ------------------ | ------ | ---------------------------------------------------------------------------- |
| `/api/posts/feed/` | GET    | Retrieve posts from users the current user follows, ordered by creation date |

### Example Responses

#### Follow User:

{
  "success": "You are now following alice."
}


#### Unfollow User:

{
  "success": "You have unfollowed alice."
}


#### Feed Example:

[
  {
    "id": 5,
    "author": "alice",
    "title": "Post Title",
    "content": "Post content here",
    "created_at": "2025-09-09T10:15:30Z",
    "updated_at": "2025-09-09T10:15:30Z"
  }
]

## Likes & Notifications Features
Overview

The platform allows users to interact more socially by liking posts and receiving notifications for key activities such as:
- New followers
- Likes on their posts
- Comments on their posts

This system is built to enhance user engagement and provide a real-time interactive experience.

### Models
Like (posts app)
- Tracks which users liked which posts.

| Field        | Type       | Description                      |
| ------------ | ---------- | -------------------------------- |
| `user`       | ForeignKey | The user who liked the post      |
| `post`       | ForeignKey | The post being liked             |
| `created_at` | DateTime   | Timestamp when the like occurred |

#### Notification (notifications app)
- Stores user notifications for relevant actions.

| Field       | Type               | Description                                         |
| ----------- | ------------------ | --------------------------------------------------- |
| `recipient` | ForeignKey to User | User receiving the notification                     |
| `actor`     | ForeignKey to User | User performing the action                          |
| `verb`      | CharField          | Description of the action (e.g., "liked your post") |
| `target`    | GenericForeignKey  | Object related to the action (Post, Comment, User)  |
| `is_read`   | BooleanField       | Whether the notification has been read              |
| `timestamp` | DateTimeField      | Time of the action                                  |

#### API Endpoints
Likes
| Endpoint                      | Method | Description   | Auth Required |
| ----------------------------- | ------ | ------------- | ------------- |
| `/api/posts/<int:pk>/like/`   | POST   | Like a post   | Yes           |
| `/api/posts/<int:pk>/unlike/` | POST   | Remove a like | Yes           |

##### Example: Like a Post
POST /api/posts/12/like/
Authorization: Token <user-token>


Response:
{
  "success": "You liked the post."
}

| Endpoint                        | Method | Description                      | Auth Required |
| ------------------------------- | ------ | -------------------------------- | ------------- |
| `/api/notifications/`           | GET    | Get all notifications for a user | Yes           |
| `/api/notifications/<id>/read/` | POST   | Mark notification as read        | Yes           |

##### Example: Get Notifications
GET /api/notifications/
Authorization: Token <user-token>

Response:
[
  {
    "id": 5,
    "actor": "alice",
    "verb": "liked your post",
    "target": "Post #12",
    "is_read": false,
    "timestamp": "2025-09-09T10:00:00Z"
  }
]

#### How It Works
- Like a Post: Creates a Like object and triggers a notification for the post author.
- Unlike a Post: Removes the Like object. Optionally updates notifications.
- New Followers: Generates a notification for the followed user.
- Comments: Creates a notification for the post author.
- Notifications can be filtered to show unread first.
- Pagination is recommended for users with many notifications.
- Users cannot like the same post multiple times.

##### Example Workflow
- Alice follows Bob → Bob gets: "Alice started following you".
- Bob posts a photo → No notification yet.
- Alice likes Bob’s post → Bob gets: "Alice liked your post".
- Alice comments → Bob gets: "Alice commented on your post".
- Bob checks notifications → Marks them as read.
