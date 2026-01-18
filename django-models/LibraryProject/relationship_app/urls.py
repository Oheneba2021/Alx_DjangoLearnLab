from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .admin_view import admin_view
from .librarian_view import librarian_view
from .member_view import member_view

urlpatterns = [
    path(
        "libraries/<int:library_id>/",
        views.LibraryDetailView.as_view(),
        name="LibraryDetailView",
    ),
    path(
        "books/",
        views.list_books,
        name="list_books",
    ),
    path(
        "login/",
        LoginView.as_view(template_name="relationship_app/login.html"),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(template_name="relationship_app/logout.html"),
        name="logout",
    ),
    path(
        "register/",
        views.register,
        name="register",
    ),
    path("admin-role/", admin_view, name="admin_view"),
    path("librarian-role/", librarian_view, name="librarian_view"),
    path("member-role/", member_view, name="member_view"),
]
