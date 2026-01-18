from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView


from .models import Book

from .views import list_books, LibraryDetailView

urlpatterns = [
    path('libraries/<int:library_id>/', views.LibraryDetailView.as_view(), name='LibraryDetailView'),
    path('books/', views.list_books, name='list_books'),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", views.RegisterView.as_view(), name="register"),
]



