from django.urls import path # type: ignore
from . import views # type: ignore

urlpatterns = [
    path('', views.home, name='home'),
    path('contato/', views.contato, name='contato'),
    path('sobre/', views.sobre, name='sobre'),
    path('sucesso/', views.sucesso, name='sucesso'),
    path('categorias/<categoria_id>/', views.categorias, name='categorias'),
    path('mensagens/', views.mensagens, name='mensagens'),
    path('detalhes_evento/<int:detalhes_id>/', views.detalhes_evento, name='detalhes_evento'),
]