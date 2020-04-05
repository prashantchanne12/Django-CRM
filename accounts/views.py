from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .models import *
from .forms import *
from .filters import OrderFilter

from .decorators import *

@unauthenticated_user
def register(request):
	# initialize CreateUserForm()
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()

			group = Group.objects.get(name='customers')
			user.groups.add(group)

			username = form.cleaned_data.get('username')
			messages.success(request, 'Account was created for '+username)

			return redirect('login')

	context = { 'form':form }
	return render(request, 'accounts/register.html', context)

@unauthenticated_user
def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR Password in Incorrect')
			return render(request, 'accounts/login.html')
	return render(request, 'accounts/login.html')


def logoutUser(request):
	logout(request)
	return redirect('login')


@login_required(login_url='login')
@admin_only
# @allowed_users(allowed_roles=['admin'])
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

def user(request):
	context = {}
	return render(request, 'accounts/user.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def products(request):
	products = Product.objects.all()
	return render(request, 'accounts/products.html', {'products':products})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customers(request, pk):
	customer = Customer.objects.get(id=pk)
	orders = customer.order_set.all()
	orders_count = orders.count()

	# Initializing filter
	myFilter = OrderFilter(request.GET, queryset=orders)
	orders = myFilter.qs

	context = {'customer' : customer,
			   'orders'	: orders,
			   'orders_count':orders_count,
			   'myFilter' : myFilter
	          }
	return render(request, 'accounts/customers.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createOrder(request, pk): 
	# inline formset allows us to create multiple forms in a single form
	# inlineformset_factory takes to models : 
	# Customer -> parent model
	# Order -> child model
	OrderFormSet = inlineformset_factory(Customer, Order, fields=('product','status'), extra=5)
	customer = Customer.objects.get(id=pk)
	formSet = OrderFormSet(queryset=Order.objects.none(), instance=customer)
	# form = OrderForm(initial={'customer':customer})
	if request.method == 'POST':
		# print('Printing POST: ', request.POST)
		formset = OrderFormSet(request.POST, instance=customer)
		if formset.is_valid():
			formset.save()
			return redirect('/')

	context = {'form' : formSet}

	return render(request, 'accounts/order_form.html', context)

@login_required(login_url='login')
def updateOrder(request, pk):
	order = Order.objects.get(id=pk)
	# passing the order as a instance
	# so that our form will be prefilled
	form = OrderForm(instance=order)
	
	context = {'form':form}

	if request.method == 'POST':
		# passing request.POST and then saving the form using form.save()
		# will create new instance, Instead we want to update in current instance
		# to update the order of current pass instance = order
		form = OrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')



	return render(request, 'accounts/order_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)

	if request.method == 'POST':
		order.delete()
		return redirect('')

	context = {'item':order}
	return render(request, 'accounts/delete.html', context=context)


'''
Django by default looks into our accounts (app name) folder and looks for
the file called templates
Inside templates it tells us to create another folder with same app name
(In this case accounts)
that's where our templates need to be stored
'''