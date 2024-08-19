from django.db import models

'''
    Importação da biblioteca responsável pela importação
        de imagens no Banco de Dados.
'''
from stdimage.models import StdImageField

'''
    Importação da biblioteca responsável por alterar os dados
        de forma específica antes ou depois deles serem salvos 
        no Banco de Dados.
'''
from django.db.models import signals

'''
    Importação da biblioteca responsável por criar slugs.
'''
from django.template.defaultfilters import slugify

'''
    Aqui estamos criando uma tabela que não será criada no
        Banco de Dados, mas que pode ser herdada em outras
        tabelas que serão criadas no Banco de Dados.
'''
class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativado/Desativado', default=True)

    class Meta:

        '''
            Aqui definimos que a tabela será uma tabela para ser
                herdada. Impedindo que ela seja criada no
                Banco de Dados.
        '''
        abstract = True

'''
    Aqui estamos criando uma tabela no Banco de Dados que está
        herdandos as colunas da tabela "Base".
'''
class Produto(Base):
    
    '''
        Aqui estamos criando uma coluna na tabela chamada nome
            que pode receber até 100 caractéres.
    '''
    nome = models.CharField('Nome', max_length=100)

    '''
        Aqui estamos criando um coluna na tabela chamada preco
            que vai ser decimal. Poderão ser inseridos até 8
            dígitos, e terá 2 casas decimais.
    '''
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    estoque = models.IntegerField('Estoque')

    '''
        Aqui estamos criando uma coluna na tabela do Banco de
            Dados para inserção de imagens.
        As imagens serão salvas na pasta "produtos" e terá uma
            variação de tamanho de 124 x 124.
    '''
    imagem = StdImageField('Imagem', upload_to='produtos', variations={'thumb': (124, 124)})
    
    '''
        Aqui estamos criando uma coluna na tabela do Banco de
            Dados para os slugs que serão criados na URL
            (endpoints). Eles não poderão ser editados.
    '''
    slug  = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome

'''
    Aqui determinamos o que será realizado antes dos dados da
        tabela "Produto" ser salva no Banco de Dados.
'''
def produto_pre_save(signal, instance, sender, **kwargs):
    
    '''
        Aqui estamos salvando o slug (endpoint) com o nome do
            produto e só depois salvando os dados no Banco
            de Dados.
    '''
    instance.slug = slugify(instance.nome)

'''
    Aqui chamamos a função de Sinais do Django e específicamos
        em qual tabela do Banco de Dados ela será atuada.
'''
signals.pre_save.connect(produto_pre_save, sender=Produto)
