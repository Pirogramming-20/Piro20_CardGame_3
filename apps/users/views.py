from django.shortcuts import render, redirect
from .forms import userCreate
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from .models import *


def signup(request):
    if request.method == 'POST':
        form = userCreate(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect('users:main')
    else:
        form = userCreate()
        ctx = {
            'form' : form
        }
    return render(request, 'users/user_signup.html', ctx)

def login (request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('users:main')
        else:
            ctx = {
                'form' : form
            }
            return render(request, 'users/user_login.html', ctx)
    else:
        form = AuthenticationForm()
        ctx = {
            'form': form,
        }
        return render(request, 'users/user_login.html', ctx)

def main (request):
    users = User.objects.all()
    ctx = {
        'users' : users
    }
    return render(request, 'users/user_main.html', ctx)