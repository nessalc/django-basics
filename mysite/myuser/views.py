from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import login
from django.core.mail import EmailMultiAlternatives
from .forms import UserCreationForm, UserActivationForm
from .models import MyUser
import hashlib
import random
from django.utils import timezone
import datetime

def register_user(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            activationkey=hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()[:5]
            keyexpiration=timezone.now()+datetime.timedelta(hours=1)
            subject, from_addr, to_addr_list = 'subject','from@example.com',[email]
            plain_text_message = 'This is an *important* message.\n\nYour activation key is '+activationkey
            html_message = '<p>This is an <em>important</em> message.</p><p>Your activation key is '+activationkey+'</p>'
            message = EmailMultiAlternatives(subject,plain_text_message,from_addr,to_addr_list)
            message.attach_alternative(html_message,'text/html')
            message.send()
            user=form.save()
            user.set_activation(activationkey,keyexpiration)
            user.save()
            login(request,user)
            return HttpResponseRedirect('/polls/')
    else:
        form=UserCreationForm()
    return render(request,'myuser/register.html',{'form':form})

def activate_user(request):
    if request.method=='POST':
        form=UserActivationForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            key=form.cleaned_data['key']
            user=MyUser.objects.get(email=email)
            if user.activation_key==key and timezone.now() <= user.key_expiration:
                user.kudos_points+=1
                user.activation_key=''
                user.key_expiration=None
                user.save()
                return HttpResponseRedirect('/polls/')
    else:
        form=UserActivationForm()
    return render(request,'myuser/activate.html',{'form':form})

def redirect_to_login(request):
    return HttpResponseRedirect('/account/login/')
