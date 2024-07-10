from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(label='Usuário')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

    def limpar_login(self):
        
        nome = self.cleaned_data['login']

        if not(nome.isalnum()):
            raise ValidationError('O nome de usuário não pode ter caractere especial.')
        
        return nome


class RegisterForm(UserCreationForm):
    sobre_voce = forms.CharField(widget=forms.Textarea, required=False)
    foto = forms.ImageField(required=False)
    foto_de_capa = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'sobre_voce', 'foto', 'foto_de_capa']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)