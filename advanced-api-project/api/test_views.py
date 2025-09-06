from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book, Author

# Tests for Book API
class BookAPITests(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpass")

        # Create an author
        self.author = Author.objects.create(name="John Doe")

        # Create a book
        self.book = Book.objects.create(
            title="Test Book",
            author=self.author,
            publication_year=2020
        )

        self.list_url = "/api/books/"
        self.detail_url = f"/api/books/{self.book.id}/"
        self.create_url = "/api/books/create/"
        self.update_url = f"/api/books/{self.book.id}/update/"
        self.delete_url = f"/api/books/{self.book.id}/delete/"

    """
    CRUD Operations for Book model
    Authentication & permissions: ensuring unauthenticated users have read-only access.
    """
    def test_list_books(self):
        """Unauthenticated users can list books"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_book(self):
        """Unauthenticated users can retrieve a single book"""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Test Book")

    def test_create_book_authenticated(self):
        """Authenticated users can create a book"""
        self.client.login(username="testuser", password="testpass")
        response = self.client.post(self.create_url, {
            "title": "New Book",
            "author": self.author.id,
            "publication_year": 2021
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_book_unauthenticated(self):
        """Unauthenticated users cannot create a book"""
        response = self.client.post(self.create_url, {
            "title": "Unauthorized Book",
            "author": self.author.id,
            "publication_year": 2021
        }, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book_authenticated(self):
        """Authenticated users can update a book"""
        self.client.login(username="testuser", password="testpass")
        response = self.client.put(self.update_url, {
            "title": "Updated Title",
            "author": self.author.id,
            "publication_year": 2019
        }, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Title")

    def test_delete_book_authenticated(self):
        """Authenticated users can delete a book"""
        self.client.login(username="testuser", password="testpass")
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

   """
   Filtering by `title`, `author`, and `publicationYear`.
   Searching in `title` and `author`.
   Ordering results by `title` or `publication_year`.
   """
    def test_filter_books_by_title(self):
        response = self.client.get(f"{self.list_url}?title=Test Book")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        response = self.client.get(f"{self.list_url}?search=Test")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books_by_publication_year(self):
        Book.objects.create(title="Older Book", author=self.author, publication_year=1999)
        response = self.client.get(f"{self.list_url}?ordering=publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book["publication_year"] for book in response.data]
        self.assertEqual(years, sorted(years))

"""
Test is run with: 
python manage.py test api
"""
