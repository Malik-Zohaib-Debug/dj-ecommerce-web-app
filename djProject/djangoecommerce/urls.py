from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login', views.loginPage, name='loginPage'),
    path('register', views.registrationPage, name='registerPage')
]
