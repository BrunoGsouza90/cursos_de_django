from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from projeto_eventos.models import Evento, Categoria

class LoginForm(forms.Form):
    username = forms.CharField(label='Usuário')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

    def limpar_login(self):
        nome = self.cleaned_data['login']
        return nome

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        label="Primeiro Nome",
        widget=forms.TextInput(attrs={
            'class': 'block w-full px-3 py-2 border border-blue-500 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-xl',
            'placeholder': 'Digite seu primeiro nome',
        })
    )
    last_name = forms.CharField(
        label="Último Nome",
        widget=forms.TextInput(attrs={
            'class': 'block w-full px-3 py-2 border border-blue-500 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-xl',
            'placeholder': 'Digite seu sobrenome',
        })
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={
            'class': 'block w-full px-3 py-2 border border-blue-500 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-xl',
            'placeholder': 'Digite seu email',
        })
    )
    username = forms.CharField(
        label="Nome de Usuário",
        widget=forms.TextInput(attrs={
            'class': 'block w-full px-3 py-2 border border-blue-500 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-xl',
            'placeholder': 'Digite seu nome de usuário',
        })
    )
    ddd = forms.CharField(
        label="DDD",
        max_length=3,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'block w-full px-3 py-2 border border-blue-500 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-xl',
            'placeholder': 'Digite o DDD',
        })
    )
    telefone = forms.CharField(
        label="Telefone",
        max_length=10,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'block w-full px-3 py-2 border border-blue-500 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-xl',
            'placeholder': 'Digite o telefone',
        })
    )
    nickname = forms.CharField(
        label="Apelido",
        max_length=30,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'block w-full px-3 py-2 border border-blue-500 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-xl',
            'placeholder': 'Digite seu apelido',
        })
    )
    sobre_voce = forms.CharField(
        label="Sobre Você",
        widget=forms.Textarea(attrs={
            'class': 'block w-full px-3 py-2 border border-blue-500 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-xl',
            'placeholder': 'Conte um pouco sobre você',
            'rows': 4,
        }),
        required=False
    )
    foto = forms.ImageField(
        label="Foto de Perfil",
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'block w-full px-3 py-2 border border-blue-500 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-xl',
        })
    )
    foto_de_capa = forms.ImageField(
        label="Foto de Capa",
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'block w-full px-3 py-2 border border-blue-500 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-xl',
        })
    )

    password1 = forms.CharField(
        label="Senha",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'block w-full px-3 py-2 border border-blue-500 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-xl',
            'placeholder': 'Digite sua senha',
        }),
    )
    password2 = forms.CharField(
        label="Confirmar Senha",
        widget=forms.PasswordInput(attrs={
            'class': 'block w-full px-3 py-2 border border-blue-500 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-xl',
            'placeholder': 'Confirme sua senha',
        }),
        strip=False,
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

            profile = Profile.objects.get_or_create(user=user)[0]
            profile.ddd = self.cleaned_data['ddd']
            profile.telefone = self.cleaned_data['telefone']
            profile.nickname = self.cleaned_data.get('nickname', '')
            profile.sobre_voce = self.cleaned_data.get('sobre_voce', '')

            if self.cleaned_data.get('foto'):
                profile.foto = self.cleaned_data['foto']

            if self.cleaned_data.get('foto_de_capa'):
                profile.foto_de_capa = self.cleaned_data['foto_de_capa']

            profile.save()

        return user

class EventoForm(forms.ModelForm):
    titulo = forms.CharField(widget=forms.TextInput(attrs={'class': 'block w-full px-3 py-2 border border-blue-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'}))
    descricao = forms.CharField(widget=forms.Textarea(attrs={'class': 'block w-full px-3 py-2 border border-blue-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'}))
    rua = forms.CharField(widget=forms.TextInput(attrs={'class': 'block w-full px-3 py-2 border border-blue-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'}))
    bairro = forms.CharField(widget=forms.TextInput(attrs={'class': 'block w-full px-3 py-2 border border-blue-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'}))
    numero = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'block w-full px-3 py-2 border border-blue-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'}))
    cidade = forms.CharField(widget=forms.TextInput(attrs={'class': 'block w-full px-3 py-2 border border-blue-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'}))
    estado = forms.CharField(widget=forms.TextInput(attrs={'class': 'block w-full px-3 py-2 border border-blue-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'}))
    pais = forms.CharField(widget=forms.TextInput(attrs={'class': 'block w-full px-3 py-2 border border-blue-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'}))
    data = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'block w-full px-3 py-2 border border-blue-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'}))
    imagem = forms.ImageField(required=False)

    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), empty_label="Selecione uma categoria", widget=forms.Select(attrs={'class': 'block w-full px-3 py-2 border border-blue-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'}))

    class Meta:
        model = Evento
        fields = ['titulo', 'descricao', 'rua', 'bairro', 'numero', 'cidade', 'estado', 'pais', 'data', 'imagem', 'categoria']