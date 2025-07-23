from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from .models import Library
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views import View


# Create your views here.
def list_books(request):
    books = Book.objects.all()

    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context

# Login view
class UserLoginView(LoginView):
    template_name = 'relationship_app/login.html'

# Logout view
class UserLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

# Register view
class register(CreateView):
    form_class = UserCreationForm
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        return response
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after successful registration
            return redirect('home')
        return render(request, 'relationship_app/register.html', {'form': form})

def home(request):
    return render(request, 'relationship_app/home.html')
