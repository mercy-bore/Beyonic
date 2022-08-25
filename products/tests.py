from django.test import TestCase
from .models import *
from app.models import *


# Create your tests here.
class ComTestClass(TestCase):
    def setUp(self):
        self.company = Company(title='mercy')
        self.company.save_company()
class ProductTestClass(TestCase):
    def setUp(self):
        self.product = Product(name='Pwani Oil')
        self.product.save_product()

    def tearDown(self):
        Product.objects.all().delete()
        

    def test_instance(self):
        self.assertTrue(isinstance(self.product,Product))

    def test_save_method(self):
        self.product.save_product()
        product = Product.objects.all()
        self.assertTrue(len(product) > 0)