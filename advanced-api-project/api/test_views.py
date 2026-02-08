"""
Unit tests for Book API views.

What we test:
1) CRUD behavior + correct status codes
2) Response data integrity (created/updated values appear in responses)
3) Permissions:
   - Unauthenticated users can read (list/detail)
   - Unauthenticated users cannot write (create/update/delete)
   - Authenticated users can write
4) Filtering, searching, ordering on the list endpoint

How to run:
    python manage.py test api
"""

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

from api.models import Author, Book


class BookAPITests(APITestCase):
    """
    Tests for Book endpoints using DRF's APITestCase.

    Endpoints assumed (based on your urls.py):
      - GET    /api/books/
      - GET    /api/books/<pk>/
      - POST   /api/books/create/
      - PATCH  /api/books/<pk>/update/
      - DELETE /api/books/<pk>/delete/

    Filtering/search/ordering assumed on:
      - GET /api/books/?title=...
      - GET /api/books/?author=<id>
      - GET /api/books/?publication_year=...
      - GET /api/books/?search=...
      - GET /api/books/?ordering=title or -publication_year
    """

    @classmethod
    def setUpTestData(cls):
        # Create authors
        cls.author1 = Author.objects.create(name="Ursula K. Le Guin")
        cls.author2 = Author.objects.create(name="Octavia E. Butler")

        # Create some books
        cls.book1 = Book.objects.create(
            title="A Wizard of Earthsea",
            publication_year=1968,
            author=cls.author1,
        )
        cls.book2 = Book.objects.create(
            title="The Dispossessed",
            publication_year=1974,
            author=cls.author1,
        )
        cls.book3 = Book.objects.create(
            title="Kindred",
            publication_year=1979,
            author=cls.author2,
        )

        # Create a user for authenticated actions
        User = get_user_model()
        cls.user = User.objects.create_user(username="tester", password="pass12345")

    def setUp(self):
        # Base endpoints (keep them in one place so changes are easy)
        self.list_url = "/api/books/"
        self.create_url = "/api/books/create/"

    # ---------------------------
    # READ tests (public access)
    # ---------------------------

    def test_list_books_unauthenticated(self):
        """Unauthenticated user can list books (200)."""
        resp = self.client.get(self.list_url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue(isinstance(resp.data, list))
        self.assertGreaterEqual(len(resp.data), 3)

    def test_retrieve_book_unauthenticated(self):
        """Unauthenticated user can retrieve a book detail (200)."""
        detail_url = f"/api/books/{self.book1.pk}/"
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], self.book1.pk)
        self.assertEqual(response.data["title"], self.book1.title)

    # ---------------------------
    # WRITE tests (permissions)
    # ---------------------------

    def test_create_book_unauthenticated_denied(self):
        """Unauthenticated user cannot create (403)."""
        payload = {
            "title": "New Book",
            "publication_year": 2000,
            "author": self.author1.pk,
        }
        resp = self.client.post(self.create_url, payload, format="json")
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_book_authenticated_success(self):
        """Authenticated user can create (201) and data is saved."""
        self.client.login(username="tester", password="pass12345")
        payload = {
            "title": "Left Hand of Darkness",
            "publication_year": 1969,
            "author": self.author1.pk,
        }
        resp = self.client.post(self.create_url, payload, format="json")
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

        # Ensure returned data matches payload
        self.assertEqual(resp.data["title"], payload["title"])
        self.assertEqual(resp.data["publication_year"], payload["publication_year"])
        self.assertEqual(resp.data["author"], payload["author"])

        # Ensure it exists in DB
        self.assertTrue(Book.objects.filter(title="Left Hand of Darkness").exists())

    def test_update_book_unauthenticated_denied(self):
        """Unauthenticated user cannot update (403)."""
        update_url = f"/api/books/{self.book1.pk}/update/"
        resp = self.client.patch(update_url, {"title": "Updated"}, format="json")
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book_authenticated_success(self):
        """Authenticated user can update (200) and changes persist."""
        self.client.login(username="tester", password="pass12345")
        update_url = f"/api/books/{self.book1.pk}/update/"
        resp = self.client.patch(update_url, {"title": "Earthsea (Updated)"}, format="json")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data["title"], "Earthsea (Updated)")

        # Verify DB updated
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Earthsea (Updated)")

    def test_delete_book_unauthenticated_denied(self):
        """Unauthenticated user cannot delete (403)."""
        delete_url = f"/api/books/{self.book2.pk}/delete/"
        resp = self.client.delete(delete_url)
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_book_authenticated_success(self):
        """Authenticated user can delete (204) and book is removed."""
        self.client.login(username="tester", password="pass12345")
        delete_url = f"/api/books/{self.book2.pk}/delete/"
        resp = self.client.delete(delete_url)
        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(pk=self.book2.pk).exists())

    # ---------------------------
    # FILTER / SEARCH / ORDER tests
    # ---------------------------

    def test_filter_by_author(self):
        """Filter list by author id returns only that author's books."""
        resp = self.client.get(self.list_url, {"author": self.author1.pk})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(resp.data), 2)
        # All returned items should match author1
        for item in resp.data:
            self.assertEqual(item["author"], self.author1.pk)

    def test_filter_by_title_contains(self):
        """Filter list by title (icontains) returns matching books."""
        resp = self.client.get(self.list_url, {"title": "earth"})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        titles = [b["title"].lower() for b in resp.data]
        self.assertTrue(any("earth" in t for t in titles))

    def test_filter_by_publication_year(self):
        """Filter list by publication_year exact."""
        resp = self.client.get(self.list_url, {"publication_year": 1979})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data), 1)
        self.assertEqual(resp.data[0]["title"], "Kindred")

    def test_search_by_title_or_author_name(self):
        """Search should match across title and author__name if configured."""
        # Search by author name substring
        resp = self.client.get(self.list_url, {"search": "Butler"})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(resp.data), 1)
        # Should include Kindred (author2)
        returned_titles = [b["title"] for b in resp.data]
        self.assertIn("Kindred", returned_titles)

    def test_ordering_by_title(self):
        """Ordering by title should return results sorted ascending by title."""
        resp = self.client.get(self.list_url, {"ordering": "title"})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        titles = [b["title"] for b in resp.data]
        self.assertEqual(titles, sorted(titles))

    def test_ordering_by_publication_year_desc(self):
        """Ordering by -publication_year should return newest first."""
        resp = self.client.get(self.list_url, {"ordering": "-publication_year"})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        years = [b["publication_year"] for b in resp.data]
        self.assertEqual(years, sorted(years, reverse=True))
