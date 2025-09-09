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


## Pagination
- Default page size: 10 items per page.
- Page size can be customized via query param 'page_size'.
- Example:  GET /api/posts/?page=2&page_size=5

## Filtering & Search
- Search posts by 'title' or 'content' using query parameter 'search'.
- Example: GET /api/posts/?search=django

## Testing
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
