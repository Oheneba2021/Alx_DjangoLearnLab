from django.shortcuts import render
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from .models import Book

# # Create your views here.
from django.http import HttpResponse


class BookDetailView(DetailView):
    """
    Docstring for BookDetailView
    """
    model = Book
    template_name = 'bookshelf/book_detail.html'
    
    def get_context_data(self, **kwargs):
        '''
        Docstring for get_context_data
        
        '''
        context = super().get_context_data(**kwargs)
        book = self.get_object()
        context['average_rating'] = book.average_rating()
        
        return context
# def index(request):
    # return HttpResponse("Welcome to the Bookshelf App!")

def  index(request):
    """Retrieves all books and renders a template displaying the List."""
    
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

# class LoginView(CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'registration/login.html'
    
# class LogoutView(CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'registration/logout.html' 

class TemplateView(CreateView):
    template_name = 'accounts/profile.html'    