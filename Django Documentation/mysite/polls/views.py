from django.db.models import F
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from polls.models import Question, Choice, Casa, Empresa, Profissao, Pagina



def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def results(request, question_id):
   question = get_object_or_404(Question, pk=question_id)
   return render(request,"polls/results.html", {"question": question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError,Choice.DoesNotExist):
        return render(request,"polls/detail.html",{"question": question, "error_message": "Você não selecionou uma escolha."})
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Não há na tabela Question id com esse número! \nCrie mais Questions em Question.")
    context = {"question" : question}
    return render(request, "polls/detail.html", context)



def casa(request):
    if request.method == 'POST':
        casa_nova_nome = request.POST.get('nome')
        casa_nova_idade = request.POST.get('idade')
        
        empresa_id = request.POST.get('empresa')
        profissao_id = request.POST.get('profissao')

        casa_nova_empresa = Empresa.objects.get(pk=empresa_id)
        casa_nova_profissao = Profissao.objects.get(pk=profissao_id)
        nova_casa = Casa(nome=casa_nova_nome, idade=casa_nova_idade, empresa=casa_nova_empresa, profissao=casa_nova_profissao)
        nova_casa.save()
        
        return HttpResponseRedirect('/cadastro/')

    casas = Casa.objects.all()
    empresas = Empresa.objects.all()
    profissaos = Profissao.objects.all()
    context = {'casas': casas, 'empresas': empresas, 'profissaos': profissaos}
    return render(request, "polls/casa.html", context)

def pagina(request):
    lista_paginas = Pagina.objects.values('link','link1')
    context = {'lista_paginas':lista_paginas}
    return render(request,"polls/pagina.html", context)

def outraum(request,numero):
    return HttpResponse('Chocolate da Fantástica Fábrica de Chocolate.')

def outradois(request,numero):
    return HttpResponse('Eu não gosto de chocolate.')

def outratres(request,numero):
    return HttpResponse('Eu prefiro salgadinho.')