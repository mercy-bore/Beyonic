from rest_framework import serializers
from .models import *

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id','first_name','last_name','email','join_date')
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id','title','post','customer')