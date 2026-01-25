from django import forms
from .models import Book


class ExampleForm(forms.Form):
    """
    ExampleForm demonstrates secure handling and validation
    of user input using Django forms.
    """

    title = forms.CharField(max_length=200)
    author = forms.CharField(max_length=100)


class BookForm(forms.ModelForm):
    """
    BookForm is used to validate and sanitize user input
    before creating or updating Book instances.
    This helps prevent malformed data and injection attacks.
    """

    class Meta:
        model = Book
        fields = ["title", "author", "publication_year"]
