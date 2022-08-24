from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from urllib import request
from django.shortcuts import render
from .models import *
from django.shortcuts import render,redirect, get_object_or_404
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.conf import settings
from .models import *
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import login, authenticate #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
import os
#!............API/djangorestframework  imports>>>>>>>>>>>>
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  *
from .serializers import *
from rest_framework import status
from .permissions import IsAdminOrReadOnly
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import viewsets
# Create your views here.
 
@login_required(login_url='/accounts/login/')
def home(request):
    companies = Company.display_companies()
    return render(request, 'home.html',{"companies": companies})
def customers(request):
    customers = Customer.display_customers()
    return render(request, 'customers.html',{"customers": customers})
class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"
    
class CustomerList(APIView):
        def get(self, request, format=None):
            all_merch = Customer.objects.all()
            serializers = CustomerSerializer(all_merch, many=True)
            return Response(serializers.data)
        def post(self, request, format=None):
            serializers = CustomerSerializer(data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
class CustomerDescription(APIView):
        def get_customer(self, pk):
            try:
                return Customer.objects.get(pk=pk)
            except Customer.DoesNotExist:
                return Http404

        def get(self, request, pk, format=None):
            customer = self.get_customer(pk)
            serializers = CustomerSerializer(customer)
            return Response(serializers.data)
        
        def put(self, request, pk, format=None):
            merch = self.get_customer(pk)
            serializers = CustomerSerializer(merch, request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data)
            else:
                return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
        def delete(self, request, pk, format=None):
            customer = self.get_customer(pk)
            customer.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
       
class CompanyList(APIView):
        def get(self, request, format=None):
            all_merch = Company.objects.all()
            serializers = CompanySerializer(all_merch, many=True)
            return Response(serializers.data)
        def post(self, request, format=None):
            serializers = CompanySerializer(data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
class CompanyDescription(APIView):
        def get_company(self, pk):
            try:
                return Company.objects.get(pk=pk)
            except Company.DoesNotExist:
                return Http404

        def get(self, request, pk, format=None):
            company = self.get_company(pk)
            serializers = CompanySerializer(company)
            return Response(serializers.data)
        
        def put(self, request, pk, format=None):
            merch = self.get_company(pk)
            serializers = CompanySerializer(merch, request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data)
            else:
                return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
        def delete(self, request, pk, format=None):
            company = self.get_company(pk)
            company.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)