from django.db import models


class Author(models.Model):
    """
    Author represents a writer in our system.

    Fields:
      - name: The author's display name.

    Relationship:
      - An Author can have many Books (one-to-many).
      - The reverse relation from Author -> Book is available as:
            author.books.all()
        because we set related_name="books" on Book.author.
    """
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    """
    Book represents a published work.

    Fields:
      - title: The book title.
      - publication_year: Year the book was published.
      - author: ForeignKey to Author (many books can belong to one author).

    Relationship:
      - Many-to-one: many Books -> one Author.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="books",  # Enables author.books.all()
    )

    def __str__(self) -> str:
        return f"{self.title} ({self.publication_year})"
