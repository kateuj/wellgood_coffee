from django.test import TestCase
from .models import UserProfile
from django.urls import reverse


class UserProfileModelTest(TestCase):

    def test_profile_model_exists(self):
        user_profiles = UserProfile.objects.count()

        self.assertEqual(user_profiles, 0)


class ProfilePageTest(TestCase):

    def test_profile_view_status_code(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)

    def test_profile_view_template_used(self):
        response = self.client.get(reverse('profile'))
        self.assertTemplateUsed(response, 'profiles/profile.html')
