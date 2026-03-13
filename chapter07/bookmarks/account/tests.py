from django.test import TestCase
from django.contrib.auth.models import User

from .models import Profile


class ProfileSignalTests(TestCase):
    def test_profile_is_created_for_new_user(self):
        user = User.objects.create_user(
            username='signal-user',
            email='signal@example.com',
            password='testpass123',
        )
        self.assertTrue(Profile.objects.filter(user=user).exists())
