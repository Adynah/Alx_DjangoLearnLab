from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView
from .views import home
from . import views
from django.contrib.auth.decorators import permission_required

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('', home, name='home'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register.as_view(), name='register'),
    # Role-based views
    path('Admin/', views.admin_view, name='Admin'),
    path('Librarian/', views.librarian_view, name='Librarian'),
    path('Member/', views.member_view, name='Member'),
    # Book actions
     path('add_book/', permission_required('relationship_app.can_add_book')(views.AddBookView.as_view()), name='add_book'),
    path('edit_book/<int:pk>/', permission_required('relationship_app.can_change_book')(views.EditBookView.as_view()), name='edit_book'),
    path('delete_book/<int:pk>/', permission_required('relationship_app.can_delete_book')(views.DeleteBookView.as_view()), name='delete_book'),

    # List books (optional for navigation)
    path('books/', views.BookListView.as_view(), name='list_books'),
]
