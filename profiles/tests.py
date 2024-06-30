from django.test import TestCase
from .models import UserProfile

class UserProfileModelTest(TestCase):
    def test_profile_model_exists(self):
        user_profiles = UserProfile.objects.count()

        self.assertEqual(user_profiles, 0)
