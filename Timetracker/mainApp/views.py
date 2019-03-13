from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from accounts_manager.models import Profile
from django.contrib.auth.decorators import login_required
from mainApp.forms import uploadProfileImgForm


import os

def getProfile(Username):
	user = User.objects.get(username=Username)
	print(user)
	try:
		UserProfile = Profile.objects.get(Custom_User=user)
	except Exception as e:
		UserProfile = None
		print(e)
	return UserProfile

@login_required(login_url='/log_in')
def home(request):
	title = "Home"
	UserProfile = getProfile(request.user.username)
	user = User.objects.get(username=request.user.username)
	return render(request, 'home/home.html', {'UserProfile':UserProfile, 
													"User": user,
													"title":title})

			
@login_required(login_url='/log_in')
def auth_logout(request):
	logout(request)
	return HttpResponseRedirect("/log_in")		

    
@login_required(login_url='/log_in')
def myprofile(requests):
	UserProfile = getProfile(requests.user.username)
	user = User.objects.get(username=requests.user.username)
	title = "My profile"
	
	return render(requests, "myprofile/myprofile.html", {'UserProfile':UserProfile, "User": user, "title" : title})


@login_required(login_url='/log_in')
def uploadProfileImg(request):
	print("asdasd")

	if request.method == 'POST':
		print("request is POST")
		form = uploadProfileImgForm(data=request.POST, files=request.FILES)
	
		if form.is_valid():
			print("sdfdsf")
			UserProfile = getProfile(request.user.username)
			UserProfile.profile_image = form.cleaned_data["avatarimage"]
			UserProfile.save()
	
			return HttpResponseRedirect("myprofile")

		else:
			print("Alarm")
			print(form.errors)

	return HttpResponseRedirect("myprofile")