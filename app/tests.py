from django.test import TestCase
from .models import *

class CustomerTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.edith = Customer(first_name = 'Edith', last_name ='Muriuki', email ='james@moringaschool.com', join_date = '17-07-2022')
    def test_instance(self):
        self.assertTrue(isinstance(self.edith,Customer))
    
    def test_save_method(self):
        self.edith.save_customer()
        editors = Customer.objects.all()
        self.assertTrue(len(editors) > 0)
        
class CompanyTestClass(TestCase):
    def setUp(self):
        
        self.title = 'Bidco'
        self.summary = 'We manufacture cooking oil'
        self.customer = Customer.objects.create(first_name='Edith')
        
        self.create_company = {
            "title": self.title,
            "summary": self.summary,
            "customer": self.customer.id
        }

    def tearDown(self):
        Company.objects.all().delete()
        

   

   