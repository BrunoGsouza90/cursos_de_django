from django.urls import path # type: ignore
from . import views # type: ignore

urlpatterns = [
    path('', views.home, name='home'),
    path('convidado/', views.home_deslogado, name='home_deslogado'),
    path('contato/', views.contato, name='contato'),
    path('contato_deslogado/', views.contato_deslogado, name='contato_deslogado'),
    path('sobre/', views.sobre, name='sobre'),
    path('sobre_deslogado/', views.sobre_deslogado, name='sobre_deslogado'),
    path('sucesso/', views.sucesso, name='sucesso'),
    path('sucesso_deslogado/', views.sucesso_deslogado, name='sucesso_deslogado'),
    path('categorias/<categoria_id>/', views.categorias, name='categorias'),
    path('categorias_deslogado/<categoria_id>/', views.categorias_deslogado, name='categorias_deslogado'),
    path('mensagens/', views.mensagens, name='mensagens'),
    path('mensagens_deslogado/', views.mensagens_deslogado, name='mensagens_deslogado'),
    path('detalhes_evento/<int:detalhes_id>/', views.detalhes_evento, name='detalhes_evento'),
    path('detalhes_evento_deslogado/<int:detalhes_id>/', views.detalhes_evento_deslogado, name='detalhes_evento_deslogado'),
]