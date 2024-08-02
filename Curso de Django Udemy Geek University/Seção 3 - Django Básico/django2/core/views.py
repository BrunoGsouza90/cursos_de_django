from django.shortcuts import render
from core.models import Produto
from django.shortcuts import get_object_or_404

'''
    Biblioteca responsável por iterar templates. Nesse caso
        específicamos a função de carregar os templates.
'''
from django.template import loader

'''
    Importação da biblioteca responsável por gerar requisições e
        respostas HTTP. No caso mencionamos o HttpResponse que
        redirecionára uma resposta HTTP.
'''
from django.http import HttpResponse

def index(request):

    '''
        Criação de uma variável recebendo todos os campos(dados)
            da tabela "Produto" do Banco de Dados.
    '''
    produtos = Produto.objects.all()

    context= {'curso': 'Progamação Web com Django Framework.',
              'outro': 'Django é massa!',
              'produtos': produtos,
              }

    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

'''
    Criação de uma função iterando em um Objeto Individual
        (Query String).
'''
def produto(request, produto_pk):

    '''
        Criação de uma variável recebendo os dados do campo
            identificado pelo "id" igual o número do URL.
        Caso o objeto não exista será retornado uma página
            com o status HTTP 404 de página não encontrada.
    '''
    produto = get_object_or_404(Produto, id=produto_pk)
    context = {'produto': produto}
    return render(request, 'produto.html', context)

'''
    Criação da função responsável por gerar uma página de erro
        de página não encontra 404.
    O parâmetro "exception" carrega informações adicionais do
        erro ocorrido.
'''
def error404(request, exception):
    template = loader.get_template('404.html')

    '''
        Retorno da função responde a renderização do template
            404.html com os caractéres "UTF-8 e um status HTTP
            404 de página não encontrada."
    '''
    return HttpResponse(content=template.render(), content_type='text/html, charset=utf8', status=404)

'''
    Em casos de erro do servidor não é necessário mencionar o
        parâmetro "exception".
'''
def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html, charset=utf8', status=500)