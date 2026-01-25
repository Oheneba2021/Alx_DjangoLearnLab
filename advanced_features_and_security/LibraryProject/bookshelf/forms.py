from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    """
    BookForm is used to validate and sanitize user input
    before creating or updating Book instances.
    This helps prevent malformed data and injection attacks.
    """

    class Meta:
        model = Book
        fields = ["title", "author", "publication_year"]
