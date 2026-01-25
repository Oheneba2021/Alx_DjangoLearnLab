from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import permission_required
from .forms import ExampleForm
from .models import Book

"""
Permissions & Groups Setup:

Custom permissions are defined on the Book model:
- can_view
- can_create
- can_edit
- can_delete

Groups configured via Django admin:
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: all permissions

Views are protected using @permission_required with raise_exception=True
to enforce access control based on group membership.
"""

def example_form_view(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = ExampleForm()

    return render(request, "bookshelf/form_example.html", {"form": form})


@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})

@permission_required("bookshelf.can_create", raise_exception=True)
def create_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        publication_year = request.POST.get("publication_year")

        Book.objects.create(
            title=title,
            author=author,
            publication_year=publication_year
        )
        return redirect("book_list")

    return render(request, "bookshelf/create_book.html")

@permission_required("bookshelf.can_edit", raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.publication_year = request.POST.get("publication_year")
        book.save()
        return redirect("book_list")

    return render(request, "bookshelf/edit_book.html", {"book": book})

@permission_required("bookshelf.can_delete", raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        book.delete()
        return redirect("book_list")

    return render(request, "bookshelf/delete_book.html", {"book": book})


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