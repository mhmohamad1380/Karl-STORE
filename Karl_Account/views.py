from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import *


# Create your views here.
def login_view(request):
    login_form = LoginForm(request.POST or None)
    if request.user.is_authenticated:
        return redirect('/')
    if login_form.is_valid():
        username = login_form.cleaned_data['username']
        password = login_form.cleaned_data['password']
        auth_checker = authenticate(username=username, password=password)
        if auth_checker:
            login(request, auth_checker)
            login_form = LoginForm()
            return redirect('/')
        else:
            login_form.add_error('username', 'Username or Password is Incorrect')

    context = {
        'login_form': login_form
    }
    return render(request, 'login.html', context)


def register_view(request):
    register_form = RegisterForm(request.POST or None)
    if request.user.is_authenticated:
        return redirect('/')
    if register_form.is_valid():
        username = register_form.cleaned_data['username']
        password = register_form.cleaned_data['password']
        email = register_form.cleaned_data['email']

        User.objects.create_user(username=username, password=password, email=email)
        return redirect('/user/login')

    context = {
        'register_form': register_form
    }
    return render(request, 'register.html', context)


def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')
    else:
        raise Http404('You are not Logged in Now')
