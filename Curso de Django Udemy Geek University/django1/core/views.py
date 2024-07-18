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
        Estamos verificando via terminal todos os comandos que a
            variável "request" nos possibilita para trabalhar emcima
            dela própria.
    '''
    print((f'\nComandos que o "request" permiti: {dir(request)}\n'))

    '''
        Aqui verificamos via terminal qual o método HTTP de requisição
            o cliente enviou pelo método "request".
    '''
    print(f'\nMétodo: {request.method}\n')

    '''
        Aqui verificamos informações completas do usuário.
    '''
    print(f'\nInformações Gerais do Cliente: {request.headers}\n')

    '''
        Aqui verificamos informações do navegador e informações 
            básica do sistema do cliente.
    '''
    print(f'\nNavegador/Sistema: {request.headers['User-Agent']}\n')

    '''
        Aqui verificamos qual usuário está logado no sistema.
    '''
    print(f'\nUsuário Online: {request.user}')
    
    '''
        Só conseguimos ver essas informações com o usuário logado.
        Pois usuários anônimos não possuem essas informações, por
            isso os comandos estão comentados.
    '''
    #print(f'Nome do Usuário: {request.user.first_name}')
    #print(f'Email do Usuário: {request.user.email}\n')

    if request.user.is_anonymous:
        status = 'Usuário Deslogado!'
        nome_do_usuario = ''
    else:
        nome_do_usuario = request.user.first_name
        status = 'Usuário Logado!'

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
              'nomes': ['Bruno', 'Jorge', 'Maria', 'João'],
              'nome_do_usuario': nome_do_usuario,
              'status': status,
              }

    '''
        Aqui estamos retornando a renderização de um template HTML
            como resposta a requisição HTTP com um contexto.
    '''
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')