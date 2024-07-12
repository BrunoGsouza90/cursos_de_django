from django.urls import reverse # type: ignore
from django.shortcuts import render, HttpResponseRedirect # type: ignore
from django.contrib.auth import authenticate, login, logout # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from .forms import LoginForm
from django.contrib.auth.forms import UserCreationForm

def login_view(request):
    error = False

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['login']
            password = form.cleaned_data['senha']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                error = True
    else:
        form = LoginForm()

    context = {'form': form, 'error': error}
    return render(request, 'users/login.html', context)

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

def register(request):
    """Faz o cadastro de um novo usuário."""
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            if authenticated_user:
                return HttpResponseRedirect(reverse('index'))
    
    else:
        form = UserCreationForm()

    context = {"form": form}
    return render(request, 'users/register.html', context)