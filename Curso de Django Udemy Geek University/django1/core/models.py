'''
    Aqui nesse arquivo faremos a criação e/ou menção do nosso Banco
        de Dados.
'''

'''
    Importação da biblioteca Django Framework responsável pelo
        Banco de Dados.
'''
from django.db import models

'''
    Criação de uma tabela no Banco de Dados chamada "Produto".
'''
class Produto(models.Model):

    '''
        Criação de uma coluna no Banco de Dados chamada "nome".
    '''
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', max_digits=15, decimal_places=2)
    estoque = models.IntegerField('Quantidade em Estoque')


class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)

'''
Obs.:
    Após finalizar a criação ou alterações no nosso modelo
        precisamos fazer a criação das migrações usando o
        comando "python manage.py makemigrations".
    Após isso migramos a criação dos modelos para o Banco de
        Dados usando o comando "python manage.py migrate".
'''