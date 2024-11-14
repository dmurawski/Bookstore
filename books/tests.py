from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.test import Client, TestCase
from django.urls import reverse

from reviews.models import Review

from .models import Book


class BookTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = get_user_model().objects.create_user(
            username="review_user",
            email="review_user@email.com",
            password="testpass123",
        )
        cls.special_permission = Permission.objects.get(
            codename="special_status",
        )
        cls.book = Book.objects.create(
            title="Test book",
            author="John Doe",
            price="22.88",
        )
        cls.review = Review.objects.create(
            book=cls.book,
            author=cls.user,
            review="Very good book!",
        )

    def test_book_listing(self):
        self.assertEqual(self.book.title, "Test book")
        self.assertEqual(self.book.author, "John Doe")
        self.assertEqual(self.book.price, "22.88")

    def test_book_list_view_for_logged_in_user(self):
        self.client.login(
            email="review_user@email.com",
            password="testpass123",
        )
        response = self.client.get(reverse("books:book_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test book")
        self.assertTemplateUsed(response, "books/book_list.html")

    def test_book_detail_view_with_permissions(self):
        self.client.login(
            email="review_user@email.com",
            password="testpass123",
        )
        self.user.user_permissions.add(self.special_permission)
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get("/books/132312/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "John Doe")
        self.assertContains(response, "Very good book!")
        self.assertTemplateUsed(response, "books/book_detail.html")

    def test_book_list_view_for_logged_out_user(self):
        self.client.logout()
        response = self.client.get(reverse("books:book_list"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            "%s?next=/books/" % (reverse("account_login")),
        )
        response = self.client.get(
            "%s?next=/books/" % (reverse("account_login")),
        )
        self.assertContains(response, "Log In")
