# MFS - BEYONIC

>[Mercy-Bore](https://github.com/macc254)  
  
# Description  
This project allows is a simple web app built in django that shows CRUDL operations for customers, companies and products.

## User Story  
  
* A user can view customers, companies and products.
* An admin can create, read, update, delete and list customers, products and companies.
  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
https://github.com/mercy-bore/Beyonic.git```
##### Navigate into the folder and install requirements  
 ```bash 
cd Beyonic pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
 python3 -m venv venv - source bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations 
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
 ### Api Endpoints
- http://127.0.0.1:8000/home/api/customers/  To view/get all customers
- http://127.0.0.1:8000/home/api/companies/  To view/get all companies
- http://127.0.0.1:8000/products/api/products/  To view/get all products
- http://127.0.0.1:8000/home/api/customers/customer-id/1/   To get a single customer, update and delete, specify the id
- http://127.0.0.1:8000/home/api/companies/company-id/1/    To get a single company, update and delete,  specify the id.
- http://127.0.0.1:8000/products/api/product/product-id/1/  To get a single product, update and delete, specify the id.
 
## Technology used  
  
* [Python3.8.10](https://www.python.org/)  
* [Django 4.0.3](https://docs.djangoproject.com/en/2.2/)  
  
  
 
  
## Contact Information   
If you have any question or contributions, please email me at [mercycherotich757@gmail.com]  
  
## License 
[License](https://github.com/mercy-bore/beyonic/blob/master/LICENSE)  
* Copyright (c) 2022 **Mercy Bore**   
