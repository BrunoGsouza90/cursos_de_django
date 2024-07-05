from django.contrib.auth.models import User  # type: ignore
from django import forms # type: ignore

class LoginForm(forms.Form):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'placeholder': ''}))
    password = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={'placeholder': ''}))
