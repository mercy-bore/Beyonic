from django.shortcuts import render
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
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import viewsets
# Create your views here.

# Create your views here.
def products(request):
    products = Product.display_products()
    return render(request, 'products.html',{"products": products})

       
class ProductList(APIView):
        def get(self, request, format=None):
            all_merch = Product.objects.all()
            serializers = ProductSerializer(all_merch, many=True)
            return Response(serializers.data)
        def post(self, request, format=None):
            serializers = ProductSerializer(data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
class ProductDescription(APIView):
        def get_product(self, pk):
            try:
                return Product.objects.get(pk=pk)
            except Product.DoesNotExist:
                return Http404

        def get(self, request, pk, format=None):
            company = self.get_product(pk)
            serializers = ProductSerializer(company)
            return Response(serializers.data)
        
        def put(self, request, pk, format=None):
            merch = self.get_product(pk)
            serializers = ProductSerializer(merch, request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data)
            else:
                return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
        def delete(self, request, pk, format=None):
            product = self.get_product(pk)
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)