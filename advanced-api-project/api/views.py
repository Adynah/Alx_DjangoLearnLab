from rest_framework import generics,
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework
from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    """
    GET /books/
    Retrieves a list of all books.
    Access allowed for all.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

     # Enable filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']  
    search_fields = ['title', 'author']  
    ordering_fields = ['title', 'publication_year']  
    ordering = ['title']  # default ordering

class BookDetailView(generics.RetrieveAPIView):
    """
    GET /books/<id>/
    Retrieves a single book by its ID.
    Access allowed for all.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
    """
    POST /books/create/
    Creates a new book.
    Only authenticated users are allowed.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Custom behavior:
        Save the book with validated data.
        """
        serializer.save()


class BookUpdateView(generics.UpdateAPIView):
    """
    PUT /books/<id>/update/
    Updates an existing book.
    Only authenticated users are allowed.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE /books/<id>/delete/
    Deletes a book.
    Only authenticated users are allowed.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
