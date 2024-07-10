from django.urls import reverse # type: ignore
from django.shortcuts import render, HttpResponseRedirect # type: ignore
from django.contrib.auth import authenticate, login, logout # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from .forms import LoginForm

def login_view(request):
    error = False
    categorias = Cate

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