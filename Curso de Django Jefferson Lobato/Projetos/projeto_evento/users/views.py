from django.urls import reverse # type: ignore
from django.shortcuts import render, HttpResponseRedirect # type: ignore
from django.contrib.auth import authenticate, login, logout # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from .forms import LoginForm
from projeto_eventos.models import Categoria
from .forms import CustomUserCreationForm

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
                # Redirecione para a página desejada após o login
                return HttpResponseRedirect(reverse('home'))
            else:
                # Trate o erro de credenciais inválidas aqui
                error = "Login ou senha incorretos. Por favor, tente novamente."
                context['form'] = form
                context['error'] = error
        else:
            context['form'] = form
    else:
        form = LoginForm()
        context['form'] = form  # Defina context mesmo fora do POST

    return render(request, 'users/login.html', context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('home'))
    
    else:
        form = CustomUserCreationForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)