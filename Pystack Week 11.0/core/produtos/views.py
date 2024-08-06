from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from produtos.models import Produto
from decimal import Decimal

def cadastrar(request):
    if request.method == 'POST':
        produto = request.POST.get('produto')
        preco = request.POST.get('preco')
        if produto == '' or preco == '':
            messages.error(request, 'Preencha os campos obrigatórios!')
            return redirect('/produtos/cadastrar')
        else:
            prod = Produto(produto=produto, preco=preco)
            prod.save()
            return redirect('/produtos/cadastrar?status=1')
    elif request.method == 'GET':
        status = request.GET.get('status')
        print(status)
        if status == '1':
            messages.success(request, 'Dados cadastrados com sucesso!')
        context = {'status': status}
        return render(request, 'index.html', context)

def listar(request):
    produtos = Produto.objects.all()
    if len(produtos) == 0:
        messages.error(request, 'Nenhum Produto cadastrado!')
        return render(request, 'index.html')
    else:
        context = {'produtos': produtos}
        return render(request, 'lista_produtos.html', context)

def excluir(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    produto.delete()
    return redirect('/produtos/listar')

def atualizar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    
    if request.method == 'POST':
        novo_produto = request.POST.get('produto')
        novo_preco = request.POST.get('preco')
        produto.produto = novo_produto
        preco_formatado = novo_preco.replace(',', '.')
        produto.preco = Decimal(preco_formatado)
        produto.save()
        return redirect('/produtos/listar')
    
    return render(request, 'atualizar_produto.html', {'produto': produto})