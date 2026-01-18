from django.urls import path, include
from . import views
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('libraries/<int:library_id>/', views.LibraryDetailView.as_view(), name='LibraryDetailView'),
    path('books/', views.list_books, name='list_books'),
]

