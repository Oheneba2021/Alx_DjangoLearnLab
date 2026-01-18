from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

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
]
