<!-- Command used  -->
book = Book.objects.get(title="1984")
book.title = "Nineteen Eigthy-Four"
book.save()

book.title

<!-- Expected Output -->
#'Nineteen Eighty-Four'

