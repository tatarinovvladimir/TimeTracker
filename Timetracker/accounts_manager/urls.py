from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
     path('', views.log_in, name='log_in'),
    path('log_in', views.log_in, name='log_in'),
    path('sign_up', views.sign_up, name='sign_up'),
]
