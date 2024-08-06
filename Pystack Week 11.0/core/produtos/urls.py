from django.urls import path
from . import views

urlpatterns = [
    # produtos/
    path('cadastrar/', views.cadastrar , name='cadastrar'),
    path('listar/', views.listar, name='listar'),
    path('atualizar_produto/<int:pk>/', views.atualizar_produto, name='atualizar_produto'),
    path('excluir/<int:pk>/', views.excluir, name='excluir'),
]