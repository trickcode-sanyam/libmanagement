from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate,login, logout
from library.models import Request, ReviewWarning
from datetime import date
def register(request):
    logout(request)
    form = RegisterForm()
    return render(request, 'register.html', {"form":form,'curruser': request.user})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            form = AuthenticationForm()
            return render(request, 'login.html',{"form":form,'curruser': request.user})
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

def profile(request):
    if request.method=='POST':
        if not request.POST.get('requestid') == None:
            requestid = request.POST.get('requestid')
            currreq = Request.objects.get(id=requestid)
            currreq.seen = True
            if not request.POST.get('accept'+ requestid) == None:
                currreq.accepted = True
            currreq.save()
        else:
            warningid = request.POST.get('warningid')
            ReviewWarning.objects.get(id = warningid).delete()
    reqset = None
    if request.user.profile.isLibrarian:
        reqset = reversed(Request.objects.all())
    else:
        if not request.user.is_staff:
            reqset = reversed(Request.objects.filter(user=request.user))
            acceptedreqs = Request.objects.filter(user=request.user,accepted=True)
            warningset = reversed(ReviewWarning.objects.filter(user=request.user))
            return render(request, 'profile.html', {'curruser': request.user, 'reqset': reqset, 'acceptedreqs': acceptedreqs, 'warningset': warningset,  'today': date.today()})
    return render(request, 'profile.html', {'curruser': request.user, 'reqset': reqset, 'today': date.today()})
