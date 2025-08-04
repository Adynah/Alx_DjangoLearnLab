from django.contrib import admin
from django.urls import path
from . import views
from .views import BookList

urlpatterns = [
    path('books/', views.BookList.as_view(), name="book_list_create"),
]
