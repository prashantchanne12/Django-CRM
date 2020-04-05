from django.contrib import admin
from django.urls import path


# import views from current directory to access functions
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user/', views.user, name='user'),
    path('customers/<str:pk>/', views.customers, name='customers'),
    path('products/', views.products, name='products'),
    
    path('create-order/<str:pk>', views.createOrder, name='create-order'),
    path('update-order/<str:pk>', views.updateOrder, name='update-order'),
    path('delete-order/<str:pk>', views.deleteOrder, name='delete-order'),

    path('login/', views.loginPage, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutUser, name='logout'),


]
