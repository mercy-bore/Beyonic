from django.test import TestCase
from .models import *
from app.models import *


# Create your tests here.
class ProductTestClass(TestCase):
    def setUp(self):
       
        self.name = 'Royco'
        self.category = 'Spices'
        self.company = Company.objects.create(title='Bidco', customer= Customer.objects.create(first_name='Edith'))
        self.create_product = {
            "product": self.name,
            "category": self.category,
            "company": self.company.id
        }

    def tearDown(self):
        Product.objects.all().delete()
        


    
        
    