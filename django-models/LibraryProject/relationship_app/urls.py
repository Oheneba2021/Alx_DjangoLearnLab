from django.urls import path, include
from . import views

urlpatterns = [
    path('libraries/<int:library_id>/', views.library_detail.as_view(), name='library_detail'),
    path('books/', views.list_books, name='list_books'),
]

