from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm, EventoForm
from projeto_eventos.models import Categoria, Evento
from django.contrib.auth.models import User
from .models import Profile
from django.contrib import messages

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
                return redirect('home')
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
            nickname = form.cleaned_data.get('nickname', '')
            ddd = form.cleaned_data['ddd']
            telefone = form.cleaned_data['telefone']

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

            new_user.profile.ddd = ddd
            new_user.profile.telefone = telefone
            new_user.profile.nickname = nickname
            new_user.profile.save()

            authenticated_user = authenticate(username=username, password=password1)
            if authenticated_user is not None:
                login(request, authenticated_user)
                return redirect('home')
    else:
        form = RegisterForm()

    context = {"form": form}
    return render(request, 'users/register.html', context)

@login_required
def editar_perfil(request, username):
    categorias = Categoria.objects.all()
    usuario = get_object_or_404(User, username=username)
    profile = usuario.profile

    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            user = form.save(commit=False)
            profile.ddd = form.cleaned_data['ddd']
            profile.telefone = form.cleaned_data['telefone']
            profile.nickname = form.cleaned_data['nickname']
            profile.sobre_voce = form.cleaned_data['sobre_voce']

            if form.cleaned_data.get('foto'):
                profile.foto = form.cleaned_data['foto']

            if form.cleaned_data.get('foto_de_capa'):
                profile.foto_de_capa = form.cleaned_data['foto_de_capa']

            user.save()
            profile.save()
            return redirect('editar_perfil', username=usuario.username)
    else:
        initial_data = {
            'first_name': usuario.first_name,
            'last_name': usuario.last_name,
            'email': usuario.email,
            'username': usuario.username,
            'ddd': profile.ddd,
            'telefone': profile.telefone,
            'nickname': profile.nickname,
            'sobre_voce': profile.sobre_voce,
            'foto': profile.foto,
            'foto_de_capa': profile.foto_de_capa,
        }
        form = RegisterForm(instance=usuario, initial=initial_data)

    context = {'usuario': usuario, 'form': form, 'categorias': categorias}
    return render(request, 'users/editar_perfil.html', context)

@login_required
def meus_eventos(request, username):
    eventos = Evento.objects.filter(usuario=request.user).all()
    categorias = Categoria.objects.all()
    usuario = get_object_or_404(User, username=username)

    if request.method == 'POST':
        form = EventoForm(request.POST, request.FILES)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.usuario = request.user
            evento.save()
            messages.success(request, 'Evento cadastrado com sucesso!')
            return redirect('meus_eventos', username=request.user.username)
        else:
            messages.error(request, 'Erro ao cadastrar o evento. Verifique os dados informados.')
    else:
        form = EventoForm()
    
    context = {'form': form, 'categorias': categorias, 'usuario': usuario, 'eventos': eventos}
    return render(request, 'users/meus_eventos.html', context)