from django.contrib import messages
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.shortcuts import redirect, render


def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    return render(request, 'accounts/logout.html')


def register(request):
    if request.method != 'POST':
        return render(request, 'accounts/register.html')

    name = request.POST.get('name')
    surname = request.POST.get('surname')
    email = request.POST.get('email')
    user = request.POST.get('user')
    password = request.POST.get('password')
    password2 = request.POST.get('password2')

    if not name or not surname or not email or not user or not password or not password2:
        messages.error(request, 'Fill in all fields')

    try:
        validate_email(email)
    except:
        messages.error(request, 'Invalid email')
        return render(request, 'accounts/register.html')
    
    if len(password) < 6:
        messages.error(request, 'Password must contain at least 6 characters.')
        return render(request, 'accounts/register.html')
    
    if len(user) < 6:
        messages.error(request, 'User must contain at least 6 characters.')
        return render(request, 'accounts/register.html')
    
    if password != password2:
        messages.error(request, 'Passwords dont match.')
        return render(request, 'accounts/register.html')
    
    if User.objects.filter(username=user).exists():
        messages.error(request, 'The user already exists.')
        return render(request, 'accounts/register.html')
    
    if User.objects.filter(email=email).exists():
        messages.error(request, 'This is already being used.')
        return render(request, 'accounts/register.html')

    messages.success(request, 'Successfully registered user. Use the fields below to login.')

    user = User.objects.create_user(username=user, email=email, password=password, first_name=name, last_name=surname)
    user.save()
    return redirect('login')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')

# Create your views here.
