from django.shortcuts import render # type: ignore
from projeto_eventos.models import Evento, Organizador, Categoria

def home(request):
    lista_eventos = Evento.objects.values('titulo','organizador','categoria','data','imagem').order_by('-data')
    context = {'lista_eventos' : lista_eventos}
    return render(request,'projeto_eventos/home.html', context)

def contato(request):
    return render(request, 'projeto_eventos/contato.html')
