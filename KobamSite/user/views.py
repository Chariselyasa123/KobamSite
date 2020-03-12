from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User,auth

# Create your views here.
def register(request):

    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            email=form.cleaned_data.get('email')
            messages.success(request, f'Akun sudah di buat untuk {username}!')
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request, 'users/register.html', {'form' :form})

def my_view_login(request):
    if request.method=='POST':
        form=AuthenticationForm(request.POST)
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('about-home')

    else:
        form=AuthenticationForm()
    return render(request, 'users/login.html', {'form' :form})

def my_view_logout(request):
    logout(request)
    return redirect('login')

def profile(request):
    return render(request, 'users/profile.html')