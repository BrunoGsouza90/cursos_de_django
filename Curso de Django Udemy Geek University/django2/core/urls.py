from django.urls import path
import core.views as views

urlpatterns = [
    
    #   Aqui estamos identificando a rota com um nome.
    path('', views.index, name='index'),
    path('contato/', views.contato, name='contato'),

    #   Criação de uma rota recebendo um endpoint individual.
    path('produto/<int:produto_pk>/', views.produto, name='produto'),
]