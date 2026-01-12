<!-- Command used -->
from bookshelf.models import Book

book = Book.objects.get(title = "Nineteen Eighty-Four")
book.delete()

Book.objects.all()


<!-- Expected Output -->
#(1, {'library.Book: 1'})

#<QuerySet []>