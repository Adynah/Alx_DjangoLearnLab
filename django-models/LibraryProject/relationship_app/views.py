from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from .models import Library


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
