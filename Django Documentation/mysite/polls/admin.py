from django.contrib import admin
from .models import Question, Choice, Casa, Empresa, Profissao, Pagina

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Casa)
admin.site.register(Empresa)
admin.site.register(Profissao)
admin.site.register(Pagina)