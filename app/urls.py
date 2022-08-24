from django.urls import path,re_path
from . import views
urlpatterns = [

path('', views.home, name = "home"),
path(r'customers/', views.customers, name = "customers"), 
path(r'signup/', views.SignUp.as_view(), name="signup"),
re_path(r'^api/customers/$', views.CustomerList.as_view()),
re_path(r'api/customer/customer-id/(?P<pk>[0-9]+)/$',
        views.CustomerDescription.as_view()),
re_path(r'^api/companies/$', views.CompanyList.as_view()),
re_path(r'api/companies/company-id/(?P<pk>[0-9]+)/$',
        views.CompanyDescription.as_view())
 ]