from django.urls import path,re_path
from . import views
urlpatterns = [

path(r'products/', views.products, name = "products"), 
re_path(r'^api/products/$', views.ProductList.as_view()),
re_path(r'api/product/product-id/(?P<pk>[0-9]+)/$',
        views.ProductDescription.as_view()),

 ]