from django.shortcuts import render, redirect
from .models import Library
from .models import Book
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# from django.http import HttpResponse
from django.views.generic.detail import DetailView

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    pk_url_kwarg = 'library_id'

# def login_view(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect("home")  # change if you use a different landing page
#     else:
#         form = AuthenticationForm()

#     return render(request, "relationship_app/login.html", {"form": form})

# @login_required
# def logout_view(request):
#     logout(request)
#     return render(request, "relationship_app/logout.html")

# def register_view(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("login")
#     else:
#         form = UserCreationForm()

#     return render(request, "relationship_app/register.html", {"form": form})

class RegisterView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = "relationship_app/register.html"
    success_url = reverse_lazy("login")