from django.conf.urls import include,url,static
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from . import views

app_name='myuser'
urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name':'myuser/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name':'myuser/logout.html'}, name='logout'),
    url(r'^register/$', views.register_user, name='register'),
    url(r'^activate/$', views.activate_user, name='activate'),
    url(r'^password_reset/$', auth_views.PasswordResetView.as_view(template_name='myuser/password_reset.html',success_url=reverse_lazy('myuser:password_reset_done'),email_template_name='myuser/password_reset_email.html'), name='password_reset'),
    url(r'^password_reset_done/$', auth_views.PasswordResetDoneView.as_view(template_name='myuser/password_reset_done.html'), name='password_reset_done'),
    url(r'^password_reset_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.PasswordResetConfirmView.as_view(template_name='myuser/password_reset_confirm.html',success_url=reverse_lazy('myuser:password_reset_complete')), name='password_reset_confirm'),
    url(r'^password_reset_complete/$', auth_views.PasswordResetCompleteView.as_view(template_name='myuser/password_reset_complete.html'), name='password_reset_complete'),
    url(r'^password_change/$', auth_views.PasswordChangeView.as_view(template_name='myuser/password_change.html',success_url=reverse_lazy('myuser:password_change_done')),name='password_change'),
    url(r'^password_change_done/$', auth_views.PasswordChangeDoneView.as_view(template_name='myuser/password_change_done.html'),name='password_change_done'),
]
