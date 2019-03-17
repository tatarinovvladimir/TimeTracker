from django import forms
from django.contrib.auth.models import User
from datetime import datetime, date, time

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100, error_messages={'required': 'Username field cannot be blank.',
                                                                'used': 'This username is already taken.'})

    email = forms.EmailField(max_length=100, error_messages={'required': 'Email field cannot be blank.',
                                                             'used': 'This Email is already taken.'})
    password = forms.CharField(max_length=100, error_messages={'invalid': 'Password must to be at least 6 characters.'})

    first_name = forms.CharField(max_length=50, error_messages={'required': 'Name field cannot be blank.',
                                                                'unreal':'Name must contain only A-z letters.'})

    last_name = forms.CharField(max_length=50, error_messages={'required': 'Surname field cannot be blank.',
                                                                'unreal':'Surname must contain only A-z letters.'})

    date_of_birth = forms.DateField(error_messages={'unreal': 'Your date of birth is unreal!'})

    user_function = forms.CharField(max_length=50, error_messages={'required': 'Function field cannot be blank.',
                                                                    'unreal':'Function must contain only A-z letters.',
                                                                    'spaces':'Too much spaces in function.'})
    

    def clean_username(self):
        data = self.cleaned_data['username']
        if User.objects.filter(username=data).exists():
            raise forms.ValidationError(self.fields['username'].error_messages['used'])

        if len(data) == 0:
            raise forms.ValidationError(self.fields['username'].error_messages['required'])
        return data


    def clean_first_name(self):
        data = self.cleaned_data['first_name']

        if not data.isalpha():
            raise forms.ValidationError(self.fields['first_name'].error_messages['unreal'])

        if len(data) == 0:
            raise forms.ValidationError(self.fields['first_name'].error_messages['required'])

        return data

    def clean_last_name(self):
        data = self.cleaned_data['last_name']

        if not data.isalpha():
            raise forms.ValidationError(self.fields['last_name'].error_messages['unreal'])

        if len(data) == 0:
            raise forms.ValidationError(self.fields['last_name'].error_messages['required'])

        return data

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError(self.fields['email'].error_messages['used'])

        if len(data) == 0:
            raise forms.ValidationError(self.fields['email'].error_messages['required'])

        return data

    def clean_password(self):
        data = self.cleaned_data['password']
        if len(data) < 6:
            raise forms.ValidationError(self.fields['password'].error_messages['invalid'])

        return data

    def clean_user_function(self):
        data = self.cleaned_data['user_function']

        if '  ' in  data:
            raise forms.ValidationError(self.fields['user_function'].error_messages['spaces'])   #Check for normal spaces bettween words

        for i in data.split(' '):
            if not i.isalpha():
                raise forms.ValidationError(self.fields['user_function'].error_messages['unreal'])  #Check all words for valid

        if len(data) == 0:
            raise forms.ValidationError(self.fields['user_function'].error_messages['required'])

        return data

    def clean_date_of_birth(self):
        data = self.cleaned_data['date_of_birth']
     
        if date(1900, 1, 1) > data or data > date.today():
            raise forms.ValidationError(self.fields['date_of_birth'].error_messages['unreal'])


        return data
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, error_messages={'required': 'Username field cannot be blank.'})
    password = forms.CharField(max_length=100, error_messages={'required': 'Password field cannot be blank.'})

    def clean_username(self):
        data = self.cleaned_data['username']
        if len(data) == 0:
            raise forms.ValidationError(self.fields['username'].error_messages['required'])
        return data

    def clean_password(self):
        data = self.cleaned_data['password']
        if len(data) == 0:
            raise forms.ValidationError(self.fields['password'].error_messages['required'])
        return data


class uploadProfileImgForm(forms.Form):
    AvatarImage = forms.ImageField()




