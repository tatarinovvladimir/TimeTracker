"""Timetracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from mainApp import views
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.conf import settings
from django.conf.urls.static import static
from mainApp.models import Project
from mainApp.models import Task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts_manager.urls')),
    path('',include('mainApp.urls')),
    path('',include('tinymce.urls')),
    path('upload_profile_img', views.uploadProfileImg, name = "uploadProfileImg"),
    path('log_out/', views.auth_logout, name = "auth_logout"),
    path('myprojects/', views.myprojects, name = "myprojects"),
    path('home/', views.home, name = "home"),
    path('myprofile/', views.myprofile, name = "myprojects"),
    path('mytasks/', views.mytasks, name = "mytasks"),
    path('journal/', views.journal, name = "journal"),
    path('myprojects/<int:pk>/', login_required(DetailView.as_view(model=Project, template_name="myprojects/project_template.html"), 
        login_url='/log_in', )),
    path('mytasks/<int:pk>/', views.mytasksdetail, name='mytasksdetail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
