from django.test import TestCase
from .models import *

class CustomerTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.james = Customer(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com', join_date = '17-07-2022')
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Customer))
    
    def test_save_method(self):
        self.james.save_customer()
        editors = Customer.objects.all()
        self.assertTrue(len(editors) > 0)
        
# class CompanyTestClass(TestCase):
#     def setUp(self):
#         self.MFS = Company(title = 'We offer financial  services', post = 'Thank you Kenya. We are fully open.')
#     def test_instance(self):
#         self.assertTrue(isinstance(self.MFS, Company))
    
#     def tearDown(self):
#         Customer.objects.all().delete()
#         Company.objects.all().delete()
class ComTestClass(TestCase):
    def setUp(self):
        self.company = Company(title='mercy')
        self.company= Company(id=1,title='Business',post='Welcome to our structure',customer=Customer.first_name)
        self.company.save_company()

    def tearDown(self):
        Company.objects.all().delete()
        

    def test_instance(self):
        self.assertTrue(isinstance(self.company,Company))

    def test_save_method(self):
        self.company.save_company()
        company = Company.objects.all()
        self.assertTrue(len(company) > 0)