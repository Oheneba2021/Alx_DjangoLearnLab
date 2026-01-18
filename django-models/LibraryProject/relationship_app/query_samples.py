from relationship_app.models import *

# Sample Queries

def query_books_by_author(author_name):
   """Retrieve all books by a specific author."""
   books = Book.objects.filter(author__name=author_name)
   return books

def list_books_in_library(library_name):
   """List all books in a specific library."""
   library = Library.objects.get(name=library_name)
   books = library.books.all()
   return books

def get_librarian_for_library(library_name):
   """Get the librarian for a specific library."""
   library = Library.objects.get(name=library_name)
   librarian = library.librarian
   return librarian 

