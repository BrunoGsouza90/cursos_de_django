from django.shortcuts import render, get_object_or_404 # type: ignore
from projeto_eventos.models import Evento, Organizador, Categoria, Contato
from django.http import HttpResponseRedirect
from django.urls import reverse

def home(request):
    categorias = Categoria.objects.all()
    lista_eventos = Evento.objects.all().order_by('data')[:12]
    context = {'lista_eventos' : lista_eventos, 'categorias': categorias}
    return render(request,'projeto_eventos/home.html', context)

def contato(request):

    if request.method == 'POST':
        nome = request.POST.get('name')
        email = request.POST.get('email')
        mensagem = request.POST.get('message')
        mensagem_contato = Contato(nome=nome, email=email, mensagem=mensagem)
        mensagem_contato.save()

        return HttpResponseRedirect(reverse('sucesso'))

    return render(request, 'projeto_eventos/contato.html')

def categorias(request, categoria_id):
    categorias = Categoria.objects.all()
    categoria = get_object_or_404(Categoria, id=categoria_id)
    eventos = Evento.objects.filter(categoria=categoria)
    context = {'categorias': categorias, 'categoria': categoria, 'eventos': eventos}
    return render(request,'projeto_eventos/categorias.html', context)

def sucesso(request):
    return render(request,'projeto_eventos/sucesso.html')

def mensagens(request):
    categorias = Categoria.objects.all()
    msg = Contato.objects.all().order_by('-data_envio')
    context = {'msg': msg, 'categorias': categorias}
    return render(request, 'projeto_eventos/mensagem.html', context)

def sobre(request):
    categorias = Categoria.objects.all()
    context = {'categorias': categorias}
    return render(request,'projeto_eventos/sobre.html', context)