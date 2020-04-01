from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
	orders = Order.objects.all()
	customers = Customer.objects.all()

	total_customers = customers.count()
	
	total_orders = orders.count()
	delivered = orders.filter(status='Delivered').count()
	pending = orders.filter(status='Pending').count()

	context = { 'orders' : orders,
	            'customers' : customers,
	            'total_orders': total_orders,
	            'delivered': delivered,
	            'pending': pending,
	          }

	return render(request, 'accounts/dashboard.html', context)

def products(request):
	products = Product.objects.all()
	return render(request, 'accounts/products.html', {'products':products})

def customers(request, pk):
	customer = Customer.objects.get(id=pk)
	orders = customer.order_set.all()
	orders_count = orders.count()

	context = {'customer' : customer,
			   'orders'	: orders,
			   'orders_count':orders_count
	          }
	return render(request, 'accounts/customers.html', context)


'''
Django by default looks into our accounts (app name) folder and looks for
the file called templates
Inside templates it tells us to create another folder with same app name
(In this case accounts)
that's where our templates need to be stored
'''