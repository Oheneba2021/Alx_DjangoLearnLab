from datetime import date
from rest_framework import serializers
from .models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    """
    Serializes Book instances.

    Includes all model fields:
      - id, title, publication_year, author

    Custom validation:
      - publication_year cannot be in the future.
    """

    class Meta:
        model = Book
        fields = "__all__"

    def validate_publication_year(self, value: int) -> int:
        """
        Field-level validator for publication_year.

        DRF will call this automatically when validating incoming data.
        """
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError(
                f"publication_year cannot be in the future (>{current_year})."
            )
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes Author instances.

    Nested relationship handling:
      - books is a nested list of the author's related Book objects.
      - read_only=True means this serializer is focused on *outputting* nested books
        rather than creating/updating them in the same request.

    How it works:
      - Because Book.author uses related_name="books", DRF can pull
        author.books.all() and serialize each with BookSerializer.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["id", "name", "books"]
