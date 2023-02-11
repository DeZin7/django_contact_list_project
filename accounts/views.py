from django.contrib import messages
from django.shortcuts import render


def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    return render(request, 'accounts/logout.html')


def register(request):
    print(request.POST)
    return render(request, 'accounts/register.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')

# Create your views here.
