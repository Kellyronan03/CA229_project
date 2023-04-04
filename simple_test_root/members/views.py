from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
import datetime

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.success(request, ("There was an error logging in. Please try again."))
            return redirect('login')
    
    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You are currently logged out."))
    return redirect('/')


def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)            
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, "Registration was successful.")
            return redirect('/')
    else:
        form = RegisterUserForm()
    return render(request, 'members/register.html', {'form': form})
