from django.test import TestCase
from .models import UserProfile

class UserProfileModelTest(TestCase):
    def test_profile_model_exists(self):
        user_profiles = UserProfile.objects.count()

        self.assertEqual(user_profiles, 0)

    
class ProfilePageTest(TestCase):
    def test_profile_page_returns_correct_response(self):
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'profiles/profile.html')
        self.assertEqual(response.status_code, 200)
