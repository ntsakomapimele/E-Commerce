from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
# Create your views here.

def homepage(request):
    products = Product.objects.all()

    return render(request, 'home.html', {'products':products})



def About(request):
        return render(request, 'About.html',{})


def login_person(request):
        if request.method == "POST":
               username = request.POST['username']
               password = request.POST['password']

               user =authenticate(request, username =username, password = password)
               print(f"Username: {username}, Password: {password}, Authenticated User: {user}")
               if user is not None:
                      login(request, user)
                      messages.success(request, ("Successfully logged in"))
                      return redirect('home')
               else:
                       messages.success(request, ("Login unsucessful"))
                       return redirect('login')

        else:
                return render(request, 'login.html',{})

def logout_person(request):
        logout(request)
        messages.success(request, ("logged out"))
        return redirect('home')


def registration(request):
        return render(request, 'registration.html',{})
