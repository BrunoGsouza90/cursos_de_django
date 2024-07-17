'''
    Nesse arquivo serão criados todos os endpoints relacionado ao
        aplicativo "core".
'''

'''
    Importação da biblioteca que gerencia as rotas do Django
        Framework.
'''
from django.urls import path

'''
    Importação da biblioteca de views que é aonde ficam os
        trabalhos relacionados as respostas e requisições
        HTTP.
'''
from . views import index, contato

'''
    Aqui serão criadas nossas rotas (endpoints) do nosso projeto
        relacionados ao app "core".
'''
urlpatterns = [
    path('', index),
    path('contato/', contato)
]