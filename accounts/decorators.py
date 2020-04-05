from django.http import HttpResponse
from django.shortcuts import render, redirect

def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('home')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func


def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):

			group = None
			# check if the group exists or not
			if request.user.groups.exists():
			   # if exists assign group to 1st group in list
			   group = request.user.groups.all()[0].name

			# if the group is in allowed_roles
			# then return the fucntion
			if group in allowed_roles:
				return view_func(request, *args, **kwargs)
			else:
				return HttpResponse('You are not authorized to view this page')

		return wrapper_func
	return decorator



def admin_only(view_func):
	def wrapper_function(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		if group == 'customers':
			return redirect('user')

		if group == 'admins':
			return view_func(request, *args, **kwargs)

	return wrapper_function	