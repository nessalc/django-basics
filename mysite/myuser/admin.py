from django.contrib import admin
from django.contrib.auth.models import Group
from .models import MyUser

# Register your models here.
admin.site.register(MyUser)
admin.site.unregister(Group)
