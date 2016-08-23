from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import authenticate, login

# Create your views here.
def login_view(request):
    username=request.POST['username']
    password=request.POST['password']
    user=authenticate(username=username,password=password)
    if user is not None:
        login(request,user)
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        return redirect('/login')

def logout_view(request):
    logout(request)