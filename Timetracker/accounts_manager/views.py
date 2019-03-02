from django.shortcuts import render

def log_in(request):
    return render(request, 'log_in/log_in.html')

def sign_up(request):
    return render(request, 'log_in/sign_up.html')
# Create your views here.
