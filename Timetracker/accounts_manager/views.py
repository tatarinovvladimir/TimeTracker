from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm, uploadProfileImgForm
from django.contrib.auth.decorators import login_required
from .models import Profile
import os
from datetime import datetime, date, time


# def log_in(request):


#     return render(request, 'log_in/log_in.html')

def log_in(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect("home")

	if request.POST:
		auth_form = LoginForm(request.POST)

        # If all of fields are valid
		if auth_form.is_valid():
			username = auth_form.cleaned_data['username'];
			password = auth_form.cleaned_data['password'];
			auth_user = authenticate(username=username, password=password)
          
            # if login or password is invalid
			if auth_user is None:
				print('ferferfer')
				error = [" ",
				         'Login or password is incorect.']
				return render(request, 'log_in/log_in.html', {'error': error, 
					                                  'username': request.POST['username']})

			login(request, auth_user)
			return HttpResponseRedirect("home")
		# If any field is blank
		else:                
			print("Sdfsdf")     
			error = [None, None]
			error[0] = auth_form['username'].errors
			error[1] = auth_form['password'].errors
			return render(request, 'log_in/log_in.html', {'error': error, 
				                                  'username': request.POST['username']})
	else:
		return render(request, 'log_in/log_in.html')

	return HttpResponseRedirect("")


def sign_up(request):
	# If I authentificated, I go to main page
	if request.POST:
		
		user = RegisterForm(request.POST)

		# HERE I check all field of post request
		if user.is_valid():
			print("good")

			# HERE I create new user with cleaned field from post request
			new_user = User.objects.create_user(user.cleaned_data['username'], 
				                                user.cleaned_data['email'], 
				                                user.cleaned_data['password']                            
				                                )
			
		
			profile = Profile()
			new_user.first_name = user.cleaned_data['first_name']
			new_user.last_name = user.cleaned_data['last_name']
			new_user.save()
			profile.Custom_User = new_user
			
			profile.date_of_birth = user.cleaned_data['date_of_birth']
			profile.user_function = user.cleaned_data['user_function']
			profile.save()
			log_user = authenticate(username=user.cleaned_data['username'], password=user.cleaned_data['password'])
			login(request, log_user)
			return HttpResponseRedirect("home")
		else:
			print("not good")
		
			# Procces errors
			


			fusername = user['username'].value()
			femail = user['email'].value()
			fname = user['first_name'].value()
			fsurname = user['last_name'].value()
			fdate = user['date_of_birth'].value()
			ffunction = user['user_function'].value()

			username_error = user['username'].errors 
			email_error = user['email'].errors 
			password_error = user['password'].errors 
			first_name_error = user['first_name'].errors
			last_name_error = user['last_name'].errors
			date_of_birth_error = user['date_of_birth'].errors
			user_function_error = user['user_function'].errors
			error = [username_error, email_error, password_error, first_name_error, last_name_error, date_of_birth_error, user_function_error]

			return render(request, 'log_in/sign_up.html', {'error': error, 'fusername' : fusername, 'femail' : femail, 'fname' : fname, 
				'fsurname' : fsurname, 'fdate' : fdate, 'ffunction' : ffunction})
				                                     

	else:


		return render(request, 'log_in/sign_up.html',)
	



