from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    join_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.first_name
    class Meta:
        ordering = ['first_name']
    def save_customer(self):
            self.save()
    @classmethod
    def display_customers(cls):
        customers = cls.objects.all()
        return customers  
class Company(models.Model):
    title = models.CharField(max_length =60)
    post = models.TextField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    
    def __str__(self):
            return self.title
    class Meta:
        ordering = ['title']
    def save_company(self):
        self.save()
        
    @classmethod
    def display_companies(cls):
        companies = cls.objects.all()
        return companies