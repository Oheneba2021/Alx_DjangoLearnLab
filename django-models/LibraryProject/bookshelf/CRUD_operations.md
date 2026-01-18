<!--Create Command used -->
from library.models import Book

book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)

book

<!-- Expected Create Output (Commented) -->
#<Book: 1984>


<!-- Retrieve Command used:  -->
book = Book.objects.get(title = "1984")
book.title, book.author, book.publication_date

<!-- Expected Update Output -->
#('1984', 'George Orwell', 1949)


<!-- Update Command used  -->
book = Book.objects.get(title="1984")
book.title = "Nineteen Eigthy-Four"
book.save()

book.title

<!-- Expected Update Output -->
#'Nineteen Eighty-Four'



<!-- Delete Command used -->
book = Book.objects.get(title = "Nineteen Eighty-Four")
book.delete()

Book.objects.all()


<!-- Expected Delete Output -->
#(1, {'library.Book: 1'})

#<QuerySet []>
