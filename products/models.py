from django.db import models

from app.models import Company
from .models import *

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length =30)
    category = models.CharField(max_length =30)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']
    def save_product(self):
            self.save()
    @classmethod
    def display_products(cls):
        products = cls.objects.all()
        return products