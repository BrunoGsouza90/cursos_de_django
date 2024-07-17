'''
    Aqui faremos a configuração do nosso ambiente de administração
        criado pelo próprio Django Framework.
    Para criar uma conta administradora e ter acesso inicial ao
        ambiente administrativo utilize o comando "python manage.py
        createsuperuser" .
'''

'''
    Importação da biblioteca responsável pela criação do ambiente
        administrativo.
'''
from django.contrib import admin

'''
    Importação da biblioteca de modelos do Banco de Dados e suas
        respectivas colunas.
'''
from core.models import Produto, Cliente

'''
    Adicionando as colunas do Banco de Dados ao ambiente
        administrativo.
'''
admin.site.register(Produto)
admin.site.register(Cliente)
