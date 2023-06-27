# from django.contrib import admin
from django.urls import path
from userapp import views

urlpatterns = [
   path('',views.loginpage,name='login'),
   path('home',views.home,name='home'),
]