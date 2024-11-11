from django.test import SimpleTestCase
from django.urls import reverse, resolve
from . import views


class HomepageTests(SimpleTestCase):
    def setUp(self) -> None:
        url = reverse("pages:home")
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, "home.html")

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, "Homepage")

    def test_homepage_not_contains_incorrect_html(self):
        self.assertNotContains(self.response, "incorrect_html")

    def test_homepage_url_resolve(self):
        view = resolve("/")
        self.assertEqual(
            view.func.__name__,
            views.HomePageView.as_view().__name__,
        )


class AboutPageTests(SimpleTestCase):
    def setUp(self) -> None:
        url = reverse("pages:about")
        self.response = self.client.get(url)

    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_templates(self):
        self.assertTemplateUsed(self.response, "about.html")

    def test_about_page_contains_correct_html(self):
        self.assertContains(self.response, "About Page")

    def test_about_page_not_contains_incorrect_html(self):
        self.assertNotContains(self.response, "incorrect_html")

    def test_about_page_url_resloves_aboutpagesview(self):
        view = resolve("/about/")
        self.assertEqual(
            view.func.__name__,
            views.AboutPageView.as_view().__name__,
        )
