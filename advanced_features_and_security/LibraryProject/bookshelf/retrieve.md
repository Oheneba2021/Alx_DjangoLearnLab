<!-- python Command used:  -->
book = Book.objects.get(title = "1984")
book.title, book.author, book.publication_date

<!-- Expected Output -->
#('1984', 'George Orwell', 1949)