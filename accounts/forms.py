from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


from .models import *

class OrderForm(ModelForm):
	class Meta:
		model = Order # class name
		fields = '__all__' # create a form with all the fields in the class
		# if you want the specific fields pass the fields in form of list
		# ex:
		# fields = ['customer', 'product']

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'
		exclude = ['user']