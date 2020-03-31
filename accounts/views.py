from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request, 'accounts/dashboard.html')

def products(request):
	return render(request, 'accounts/products.html')

def customers(request):
	return render(request, 'accounts/customers.html')


'''
Django by default looks into our accounts (app name) folder and looks for
the file called templates
Inside templates it tells us to create another folder with same app name
(In this case accounts)
that's where our templates need to be stored
'''