from django.shortcuts import render

def home(request):
    return render(request, 'home/home.html')

def myprofile(requests):
    return render(requests, 'myprofile/myprofile.html')
# Create your views here.
