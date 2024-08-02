'''
    Aqui nesse arquivo faremos todas as configurações relacionadas
        a rotas de Endpoint's do nosso projeto.
'''

'''
    Importação da biblioteca que faz menção ao modo administrador
        já criado pelo Django Framework, para uma melhor consulta
        em nosso projeto, de maneira rápida e eficaz.
'''
from django.contrib import admin

'''
    Importação da biblioteca de rotas do Django Framework.
'''
from django.urls import path, include

'''
    Importação das nossas views, que são onde ficam os trabalhos
        de requisição e reposta HTTP.
    Em específico estamos importando as funções "index" e "contato"
        da views do app "core",
'''
from core.views import index, contato

'''
    Criação da lista onde serão inseridas as rotas do nosso
        projeto.
'''
urlpatterns = [
    
    #   Criação da rota do django admin pode acessá-la usando o
    #   endpoint 'painel/' .
    #   Por padrão vem como admin/ , mas não é seguro, devemos colocar
    #       uma url mais complexa.
    path('painel/', admin.site.urls),


    #   Essa importação não seria ideal então comentamos...
    #   O correto é criar um arquivo de rotas dentro próprio
    #       aplicativo, e redirecionar a rota principal daqui
    #       para os demais endpoints que serão criados lá.

    #   Criação da rota para a função index criada em views.
    #path('', index),
    #path('contato/', contato),

    #   Criação da rota principal e redirecionamento dos demais
    #       endpoints para o aplicativo "core" no arquivo
    #       "urls.py" criado agora por sua vez no app.
    path('', include('core.urls')),
]
