from django.test import TestCase
from products.forms import ProductForm

class ProductFormTest(TestCase):

    def test_form_valid_data(self):
        form = ProductForm(data={
            'categories': 'coffee'
        })

        self.assertTrue(form.is_valid())