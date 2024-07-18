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

'''
    Registro da tabela "Produto" na área administrativa.
'''
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    
    '''
        Criação das colunas da tabela "Produto" na área administrativa.
    '''
    list_display = ['get_nome', 'get_preco', 'get_estoque']

    '''
        Renomeando o nome das colunas.
    '''
    def get_nome(self, obj):
        return obj.nome
    get_nome.short_description = 'Nome do Produto'

    def get_preco(self, obj):
        return obj.preco
    get_preco.short_description = 'Preço do Produto'

    def get_estoque(self, obj):
        return obj.estoque
    get_estoque.short_description = 'Quantidade em Estoque'

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):

    list_display = ['get_nome', 'get_sobrenome', 'get_email']

    def get_nome(self, obj):
        return obj.nome
    get_nome.short_description = 'Nome do Cliente'

    def get_sobrenome(self, obj):
        return obj.sobrenome
    get_sobrenome.short_description = 'Sobrenome do Cliente'

    def get_email(self, obj):
        return obj.email
    get_email.short_description = 'Email do Cliente'

