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

class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)
    ddd = forms.CharField(required=True)
    telefone = forms.CharField(required=True)
    nickname = forms.CharField(required=False)
    sobre_voce = forms.CharField(widget=forms.Textarea, required=False)
    foto = forms.ImageField(required=False)
    foto_de_capa = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'ddd', 'telefone', 'nickname', 'sobre_voce', 'foto', 'foto_de_capa']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'border-2 border-blue-300 rounded-lg text-lg p-2 w-full'})
        
        if 'instance' in kwargs:
            user = kwargs['instance']
            self.fields['ddd'].initial = user.profile.ddd
            self.fields['telefone'].initial = user.profile.telefone
            self.fields['nickname'].initial = user.profile.nickname
            self.fields['sobre_voce'].initial = user.profile.sobre_voce
            self.fields['foto'].initial = user.profile.foto
            self.fields['foto_de_capa'].initial = user.profile.foto_de_capa

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            profile = user.profile
            profile.ddd = self.cleaned_data['ddd']
            profile.telefone = self.cleaned_data['telefone']
            profile.nickname = self.cleaned_data['nickname']
            profile.sobre_voce = self.cleaned_data['sobre_voce']
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