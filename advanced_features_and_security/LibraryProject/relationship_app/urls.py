from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
# from .admin_view import admin_view
# from .librarian_view import librarian_view
# from .member_view import member_view

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
    path("admin-role/", views.admin_view, name="admin_view"),
    path("librarian-role/", views.librarian_view, name="librarian_view"),
    path("member-role/", views.member_view, name="member_view"),
      path("books/add_book/", views.add_book, name="add_book"),
    path("books/edit_book/<int:book_id>/", views.edit_book, name="edit_book"),
    path("books/delete_book/<int:book_id>/", views.delete_book, name="delete_book"),
]
