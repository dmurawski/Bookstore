from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="testuser123",
            email="testuser123@email.com",
            password="testpass123",
        )
        self.assertEqual(user.username, "testuser123")
        self.assertEqual(user.email, "testuser123@email.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        superuser = User.objects.create_superuser(
            username="superuser123",
            email="superuser123@email.com",
            password="testpass123",
        )
        self.assertEqual(superuser.username, "superuser123")
        self.assertEqual(superuser.email, "superuser123@email.com")
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)
