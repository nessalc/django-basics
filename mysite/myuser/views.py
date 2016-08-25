from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import login
from .forms import UserCreationForm
#from django.contrib.auth.forms import UserCreationForm

def register_user(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return HttpResponseRedirect('/polls/')
    else:
        form=UserCreationForm()
    return render(request,'myuser/register.html',{'form':form})
