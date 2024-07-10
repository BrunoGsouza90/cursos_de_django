from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class LoginForm(forms.Form):
    username = forms.CharField(label='Usuário')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

    def limpar_login(self):
        
        nome = self.cleaned_data['login']

        if not(nome.isalnum()):
            raise ValidationError('O nome de usuário não pode ter caractere especial.')
        
        return nome
    
CustomUser = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    sobre_voce = forms.CharField(label='Sobre você', widget=forms.Textarea(attrs={'rows': 8}))
    foto = forms.ImageField(label='Foto', required=False)
    foto_de_capa = forms.ImageField(label='Foto de capa', required=False)
    primeiro_nome = forms.CharField(label='Primeiro nome')
    ultimo_nome = forms.CharField(label='Último nome')
    email = forms.EmailField(label='Endereço de email')
    pais = forms.CharField(label='País')
    cidade = forms.CharField(label='Cidade')
    endereco = forms.CharField(label='Endereço')
    telefone = forms.CharField(label='Número de telefone')

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'sobre_voce', 'foto', 'foto_de_capa',
                  'primeiro_nome', 'ultimo_nome', 'email', 'pais', 'cidade', 'endereco', 'telefone')