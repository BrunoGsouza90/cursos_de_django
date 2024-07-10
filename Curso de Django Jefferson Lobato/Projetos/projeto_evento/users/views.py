from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm  # Importe os formulários RegisterForm e LoginForm
from projeto_eventos.models import Categoria

def login_view(request):
    categorias = Categoria.objects.all()
    context = {'categorias': categorias}

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirecionar para a página desejada após o login
            else:
                error = "Login ou senha incorretos. Por favor, tente novamente."
                context['form'] = form
                context['error'] = error
        else:
            context['form'] = form
    else:
        form = LoginForm()
        context['form'] = form

    return render(request, 'users/login.html', context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            sobre_voce = form.cleaned_data.get('sobre_voce', '')
            foto = form.cleaned_data.get('foto', None)
            foto_de_capa = form.cleaned_data.get('foto_de_capa', None)
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

            new_user = form.save(commit=False)
            new_user.email = email
            new_user.first_name = first_name
            new_user.last_name = last_name

            if sobre_voce:
                new_user.sobre_voce = sobre_voce
            if foto:
                new_user.foto = foto
            if foto_de_capa:
                new_user.foto_de_capa = foto_de_capa

            new_user.save()

            authenticated_user = authenticate(username=username, password=password1)
            login(request, authenticated_user)

            return redirect('home')
    else:
        form = RegisterForm()

    context = {"form": form}
    return render(request, 'users/register.html', context)