<!--python Command used -->
from library.models import Book

book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)

book

<!-- Expected Output (Commented) -->
#<Book: 1984>

