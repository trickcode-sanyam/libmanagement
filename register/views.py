from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate,login, logout

def register(request):
    form = RegisterForm()
    return render(request, 'register.html', {"form":form,'curruser': request.user})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password'] 
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login( request, user)
            return redirect('/')
        else:
            return render(request, 'login.html',{'curruser': request.user})
            #also add error message

    else:
        if request.user.is_authenticated:
            form = 'AlreadyLoggedIn'
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {"form":form,'curruser': request.user})

def logout_view(request):
    logout(request)
    return redirect('/')

