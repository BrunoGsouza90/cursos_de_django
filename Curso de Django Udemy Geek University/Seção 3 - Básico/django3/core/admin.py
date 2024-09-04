from django.contrib import admin
from core.models import Produto, Cliente

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    
    list_display = ['get_nome', 'get_preco', 'get_estoque']

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

