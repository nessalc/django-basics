from django.conf.urls import include,url,static
from django.contrib.auth import views as auth_views

from . import views

app_name='myuser'
urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name':'myuser/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name':'myuser/logout.html'}, name='logout'),
    url(r'^register/$', views.register_user, name='register'),
    url(r'^activate/$', views.activate_user, name='activate'),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    #url(r'^', include('django.contrib.auth.urls')),
]
