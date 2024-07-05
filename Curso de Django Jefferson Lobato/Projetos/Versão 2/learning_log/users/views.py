from django.shortcuts import render # type: ignore
from django.http import HttpResponseRedirect # type: ignore
from django.urls import reverse # type: ignore
from .forms import LoginForm
from django.contrib.auth import authenticate, login # type: ignore

def login_view(request):
    if request.method != 'POST':
        form = LoginForm()
    else:
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                error_message = "Login incorreto. Por favor, verifique seu login e senha."
                context = {'form': form, 'error_message': error_message}
                return render(request, 'users/login.html', context)

    context = {'form': form}
    return render(request, 'users/login.html', context)