from django.contrib import admin
from django.urls import path

# import views from current directory to access functions
from . import views

urlpatterns = [
    path('', views.home),
    path('customers/', views.customers),
    path('products/', views.products),
]
