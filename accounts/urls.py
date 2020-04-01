from django.contrib import admin
from django.urls import path

# import views from current directory to access functions
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('customers/<str:pk>/', views.customers, name='customers'),
    path('products/', views.products, name='products'),
]
