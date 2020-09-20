from django.test import TestCase
from django.test.client import Client
from mainapp.models import Product, ProductCategory
from django.core.management import call_command

class TestMainappSmoke(TestCase):
   def setUp(self):
        self.client = Client()

   def test_mainapp_urls(self):
       response = self.client.get('/')
       self.assertEqual(response.status_code, 200)

       response = self.client.get('/contacts/')
       self.assertEqual(response.status_code, 200)

       response = self.client.get('/catalog/')
       self.assertEqual(response.status_code, 200)

       response = self.client.get('/catalog/category/0/')
       self.assertEqual(response.status_code, 200)

       for category in ProductCategory.objects.all():
           response = self.client.get(f'/catalog/category/{category.pk}/')
           self.assertEqual(response.status_code, 200)

       for product in Product.objects.all():
           response = self.client.get(f'/catalog/product/{product.pk}/')
           self.assertEqual(response.status_code, 200)

   def tearDown(self):
        call_command('sqlsequencereset', 'mainapp', 'authapp', 'ordersapp', 'basketapp')
