from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.shortcuts import redirect, render

from .models import ContactForm


def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')
    
    user = request.POST.get('user')
    password = request.POST.get('password')

    user_check = auth.authenticate(request, username=user, password=password)

    if not user_check:
        messages.error(request, 'Invalid user or password.')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user_check)
        messages.success(request, 'You have successfully logged in.')
        return redirect('dashboard') 



def logout(request):
    auth.logout(request)
    return redirect('index')


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

@login_required(redirect_field_name='login') #in case that the user isn't logged in, the user will be redirected to login
def dashboard(request):
    if request.method != 'POST':
        form = ContactForm()
        return render(request, 'accounts/dashboard.html', {'form': form})
    
    form = ContactForm(request.POST, request.FILES)

    if not form.is_valid():
        messages.error(request, 'Error submitting form.')
        form = ContactForm(request.POST)
        return render(request, 'accounts/dashboard.html', {'form': form})
    
    description = request.POST.get('description')

    if len(description) < 5:
        messages.error(request, 'Error submitting form.')
        form = ContactForm(request.POST)
        return render(request, 'accounts/dashboard.html', {'form': form})
    
    form.save()
    messages.success(request, f'Contact {request.POST.get("name")} saved.')
    return redirect('dashboard')


# Create your views here.
