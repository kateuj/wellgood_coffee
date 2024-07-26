from django.test import TestCase
from .forms import ItemForm

# Create your tests here.


class TestLoginForm(TestCase):

    def test_login_username_is_required(self):
        form = ItemForm({'username': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors.keys())
        self.assertEqual(form.errors['username'][0], 'This field is required.')

    def test_login_password_is_required(self):
        form = ItemForm({'password': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('password', form.errors.keys())
        self.assertEqual(form.errors['password'][1], 'This field is required.')
