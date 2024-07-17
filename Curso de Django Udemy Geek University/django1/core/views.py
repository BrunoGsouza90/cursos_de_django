'''
    Aqui nesse arquivo processaremos as requisições HTTP e/ou
        enviaremos resposta HTTP.
'''

'''
    Essa biblioteca é responsável por renderizar os templates 
        HTML.
'''
from django.shortcuts import render

'''
    Criação de uma função recebendo o parámetro de requisições
        HTTP. Todas as requisições HTTP ficam guardadas no modo
        request.
'''
def index(request):

    '''
        Criação de uma variável recebendo um dicionário que é um
            contexto em Django Framework que será adicionado na
            renderização.
        Esse contexto pode ser mencionado no template, como
        {{ curso }} , neste caso pois é uma queryString.
        Caso seja um arquivo de lista com mais de um item deve
            ser usado dentro de um Loop For, pois é um
            querySet:
        
        {% variavel in variaveis %}
            {{ variavel }}
        {% endfor %}

        Confira o template index.html.
        
    '''
    context= {'curso': 'Progamação Web com Django Framework.',
              'outro': 'Django é massa!',
              'nomes': ['Bruno', 'Jorge', 'Maria', 'João']}

    '''
        Aqui estamos retornando a renderização de um template HTML
            como resposta a requisição HTTP com um contexto.
    '''
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')