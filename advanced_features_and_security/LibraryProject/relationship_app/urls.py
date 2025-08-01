from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView
from .views import home
from . import views
from django.contrib.auth.decorators import permission_required

urlpatterns = [
    path('', home, name='home'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register.as_view(), name='register'),
    # Role-based views
    path('Admin/', views.admin_view, name='Admin'),
    path('Librarian/', views.librarian_view, name='Librarian'),
    path('Member/', views.member_view, name='Member'),
    # Book actions
    path('books/', views.list_books, name='list_books'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),

    # Library details
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
