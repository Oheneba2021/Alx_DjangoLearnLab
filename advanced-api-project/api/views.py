from rest_framework import generics, permissions, filters
from rest_framework.exceptions import PermissionDenied

from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    """
    GET /books/
    Returns a list of all books.

    Permissions:
      - AllowAny: anyone can read

    Extra behavior:
      - Basic filtering by query params:
            ?author=<author_id>
            ?year=<publication_year>
      - Optional ordering / searching examples included via DRF filters.
    """
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    # Optional: enable search & ordering
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title"]
    ordering_fields = ["publication_year", "title"]
    ordering = ["id"]

    def get_queryset(self):
        queryset = Book.objects.select_related("author").all()

        author_id = self.request.query_params.get("author")
        year = self.request.query_params.get("year")

        if author_id:
            queryset = queryset.filter(author_id=author_id)
        if year:
            queryset = queryset.filter(publication_year=year)

        return queryset


class BookDetailView(generics.RetrieveAPIView):
    """
    GET /books/<pk>/
    Returns a single book by primary key.

    Permissions:
      - AllowAny: anyone can read
    """
    queryset = Book.objects.select_related("author").all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BookCreateView(generics.CreateAPIView):
    """
    POST /books/create/
    Creates a new Book.

    Permissions:
      - IsAuthenticated: only logged-in users can create

    Notes:
      - Validation is handled by BookSerializer (including publication_year not in future).
      - You can add extra logic in perform_create if you want to set defaults or audit.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Example hook: you could log creator here if your model supported it
        serializer.save()


class BookUpdateView(generics.UpdateAPIView):
    """
    PUT/PATCH /books/<pk>/update/
    Updates an existing Book.

    Permissions:
      - IsAuthenticated: only logged-in users can update

    Notes:
      - Uses serializer validation automatically.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()


class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE /books/<pk>/delete/
    Deletes an existing Book.

    Permissions:
      - IsAuthenticated: only logged-in users can delete
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
