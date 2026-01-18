from django.urls import path, include
from . import views


from .models import Book

from .views import list_books, LibraryDetailView

urlpatterns = [
    path('libraries/<int:library_id>/', views.LibraryDetailView.as_view(), name='LibraryDetailView'),
    path('books/', views.list_books, name='list_books'),
       path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
]

