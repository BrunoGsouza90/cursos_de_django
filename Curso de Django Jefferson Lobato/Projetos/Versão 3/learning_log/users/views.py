from django.shortcuts import render # type: ignore
from django.http import HttpResponseRedirect # type: ignore
from django.urls import reverse # type: ignore
from .forms import LoginForm
from django.contrib.auth import authenticate, login # type: ignore

def login_view(request):

    error = False

    if request.method != 'POST':
        form = LoginForm()
    else:
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('login')
            password = request.POST.get('senha')
            user = authenticate(username=username, password=password)
            
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                error = True

    context = {'form': form, 'error': error}
    return render(request, 'users/login.html', context)