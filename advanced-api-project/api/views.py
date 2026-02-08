from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Book
from .serializers import BookSerializer
from .filters import BookFilter


class BookListView(generics.ListAPIView):
    """
    GET /api/books/

    Adds:
      - Filtering (DjangoFilterBackend + BookFilter)
      - Searching (SearchFilter)
      - Ordering (OrderingFilter)

    Examples:
      - Filter:  /api/books/?author=1&publication_year=1968
      - Filter title contains: /api/books/?title=earth
      - Search:  /api/books/?search=wizard
      - Order:   /api/books/?ordering=title
      - Order desc: /api/books/?ordering=-publication_year
    """
    queryset = Book.objects.select_related("author").all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # The three query features:
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Filtering
    filterset_class = BookFilter

    # Searching (supports related fields)
    search_fields = ["title", "author__name"]

    # Ordering
    ordering_fields = ["id", "title", "publication_year"]
    ordering = ["id"]



class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieve a single book.
    Anyone can access (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
    """
    Create a new book.
    Only authenticated users allowed.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookUpdateView(generics.UpdateAPIView):
    """
    Update an existing book.
    Only authenticated users allowed.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
    """
    Delete a book.
    Only authenticated users allowed.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
