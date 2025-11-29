from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book

"""
This test module validates:
- CRUD operations for Book API
- Filtering, searching, ordering
- Authentication and permission enforcement
"""

class BookAPITestCase(APITestCase):

    def setUp(self):
        """
        This method runs before EVERY test.
        It sets up initial test data.
        """

        # ✅ Create test user for authentication
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )

        # ✅ Create test author
        self.author = Author.objects.create(name="John Writer")

        # ✅ Create test books
        self.book1 = Book.objects.create(
            title="Django for Beginners",
            publication_year=2020,
            author=self.author
        )

        self.book2 = Book.objects.create(
            title="Advanced Django",
            publication_year=2023,
            author=self.author
        )

        # ✅ API URLs
        self.list_url = "/api/books/"
        self.detail_url = f"/api/books/{self.book1.id}/"

    # ✅ ---------------------------
    # ✅ READ OPERATIONS (PUBLIC)
    # ✅ ---------------------------

    def test_get_all_books(self):
        """
        Test retrieving all books (ListView)
        """
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_single_book(self):
        """
        Test retrieving a single book by ID (DetailView)
        """
        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Django for Beginners")

    # ✅ ---------------------------
    # ✅ CREATE OPERATION (AUTH)
    # ✅ ---------------------------

    def test_create_book_authenticated(self):
        """
        Test creating a book with authentication
        """
        self.client.login(username="testuser", password="testpassword")

        data = {
            "title": "REST APIs with Django",
            "publication_year": 2022,
            "author": self.author.id
        }

        response = self.client.post(self.list_url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        """
        Test creating a book WITHOUT authentication (should fail)
        """
        data = {
            "title": "Unauthorized Book",
            "publication_year": 2023,
            "author": self.author.id
        }

        response = self.client.post(self.list_url, data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ✅ ---------------------------
    # ✅ UPDATE OPERATION (AUTH)
    # ✅ ---------------------------

    def test_update_book_authenticated(self):
        """
        Test updating a book with authentication
        """
        self.client.login(username="testuser", password="testpassword")

        data = {
            "title": "Updated Django Book",
            "publication_year": 2021,
            "author": self.author.id
        }

        response = self.client.put(self.detail_url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Django Book")

    # ✅ ---------------------------
    # ✅ DELETE OPERATION (AUTH)
    # ✅ ---------------------------

    def test_delete_book_authenticated(self):
        """
        Test deleting a book with authentication
        """
        self.client.login(username="testuser", password="testpassword")

        response = self.client.delete(self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # ✅ ---------------------------
    # ✅ FILTERING TESTS
    # ✅ ---------------------------

    def test_filter_books_by_year(self):
        """
        Test filtering books by publication_year
        """
        response = self.client.get("/api/books/?publication_year=2023")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Advanced Django")

    # ✅ ---------------------------
    # ✅ SEARCH TESTS
    # ✅ ---------------------------

    def test_search_books_by_title(self):
        """
        Test searching books by title keyword
        """
        response = self.client.get("/api/books/?search=Advanced")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # ✅ ---------------------------
    # ✅ ORDERING TESTS
    # ✅ ---------------------------

    def test_order_books_by_year_desc(self):
        """
        Test ordering books by publication_year descending
        """
        response = self.client.get("/api/books/?ordering=-publication_year")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Advanced Django")
