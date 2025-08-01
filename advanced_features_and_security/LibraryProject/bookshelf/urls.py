from django.urls import path
from .views import BookListView, create_book, edit_book, delete_book

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('add/', create_book, name='create_book'),
    path('edit/<int:pk>/', edit_book, name='edit_book'),
    path('delete/<int:pk>/', delete_book, name='delete_book'),
]
