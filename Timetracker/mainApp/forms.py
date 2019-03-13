from django import forms
from django.contrib.auth.models import User

class uploadProfileImgForm(forms.Form):
	avatarimage = forms.ImageField()


	
