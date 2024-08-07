from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def cadastro(request):
    if request.method == 'POST':
        usuario = request.POST.get('username')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        if(senha != confirmar_senha):
            messages.error(request, 'As senhas precisam ser iguais.')
            return redirect('/cadastro/')
    return render(request,'cadastro.html')