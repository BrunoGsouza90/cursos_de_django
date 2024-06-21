from django.contrib import admin # type: ignore
from exatas_cadastros.models import Cadastro, Categoria, Conta

admin.site.register(Cadastro)
admin.site.register(Categoria)
admin.site.register(Conta)