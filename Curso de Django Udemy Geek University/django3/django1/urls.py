from django.contrib import admin
from django.urls import path, include
from core import views

'''
    Importação da biblioteca responsável por oferecer uma opção
        personalizada de página de erro do status HTTP 404 e 500.'
'''
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('painel/', admin.site.urls),
    path('', include('core.urls')),
]

'''
    Criação de uma variável recebendo a função personalizada de
        página 404. Essa função poderá ser mencionada dentro de
        views.py.
'''
handler404 = views.error404
handler500 = views.error500