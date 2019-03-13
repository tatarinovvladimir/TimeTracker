from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('myprofile/', views.myprofile, name='myprofile'),

    
]
