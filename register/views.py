from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login, logout
from library.models import Request, ReviewWarning
from datetime import date, timedelta
from django.contrib import messages

def register(request):
    logout(request)
    form = RegisterForm()
    if request.method == 'POST':
        messages.success(request, 'Your account has been created, now please continue to login.')
    return render(request, 'register.html', {"form":form,'curruser': request.user})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('/')
        else:
            form = AuthenticationForm()
            messages.warning(request, 'Login failed!')
            return render(request, 'login.html',{"form":form,'curruser': request.user})

    else:
        if request.user.is_authenticated:
            form = 'AlreadyLoggedIn'
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {"form":form,'curruser': request.user})

def logout_view(request):
    logout(request)
    messages.success(request, 'Logout successful!')
    return redirect('/')

def profile(request):
    if not request.user.is_authenticated:
        messages.info(request, 'You must be logged in to access profile.')
        return redirect('/login')
    else:
        if request.method=='POST':
            if not request.POST.get('requestid') == None:
                requestid = request.POST.get('requestid')
                currreq = Request.objects.get(id=requestid)
                currreq.seen = True
                if not request.POST.get('accept'+ requestid) == None:
                    currreq.accepted = True
                currreq.save()
            elif not request.POST.get('accreqid') == None:
                accreqid = request.POST.get('accreqid')
                currreq = Request.objects.get(id=accreqid)
                newfrom = currreq.todate
                newto = newfrom + timedelta(days=7)
                newreq = Request(fromdate=newfrom, todate= newto, user=request.user, book=currreq.book, seen=False, accepted=False)
                newreq.save()
                messages.success(request, 'Sent extension request.')
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
