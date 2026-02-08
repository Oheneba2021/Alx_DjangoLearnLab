import django_filters
from .models import Book


class BookFilter(django_filters.FilterSet):
    """
    BookFilter defines explicit filtering rules for the Book list endpoint.

    Supported filters:
      - title: partial match (case-insensitive) via ?title=<text>
      - author: filter by author id via ?author=<id>
      - publication_year: exact year via ?publication_year=<year>
      - publication_year range via ?publication_year_min=...&publication_year_max=...
    """
    title = django_filters.CharFilter(field_name="title", lookup_expr="icontains")
    author = django_filters.NumberFilter(field_name="author_id")
    publication_year = django_filters.NumberFilter(field_name="publication_year")

    publication_year_min = django_filters.NumberFilter(
        field_name="publication_year", lookup_expr="gte"
    )
    publication_year_max = django_filters.NumberFilter(
        field_name="publication_year", lookup_expr="lte"
    )

    class Meta:
        model = Book
        fields = ["title", "author", "publication_year"]
