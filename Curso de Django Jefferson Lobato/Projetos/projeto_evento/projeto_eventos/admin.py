from django.contrib import admin # type: ignore
from projeto_eventos.models import Evento, Organizador, Categoria, Contato

admin.site.register(Evento)
admin.site.register(Organizador)
admin.site.register(Categoria)
admin.site.register(Contato)