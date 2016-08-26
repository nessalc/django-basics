from django import forms
from django.contrib import admin
from .models import MyUser

class UserCreationForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ('email',)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserActivationForm(forms.Form):
    email=forms.EmailField(label='Email')
    key=forms.CharField(label='Activation Key',max_length=16)
