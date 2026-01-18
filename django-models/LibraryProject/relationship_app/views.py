from django.shortcuts import render
from .models import Author, Book, Library, Librarian
from django.http import HttpResponse
from django.views import View, list_views, DetailView


# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class library_detail(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    pk_url_kwarg = 'library_id'
    
