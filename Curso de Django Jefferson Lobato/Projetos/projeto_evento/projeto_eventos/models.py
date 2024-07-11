from django.db import models # type: ignore
from django.contrib.auth.models import User

class Organizador(models.Model):
    nome = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=200, blank=True)
    ddd = models.CharField(max_length=2, blank=True)
    telefone = models.CharField(max_length=15, blank=True)
    nick = models.CharField(max_length=30, unique=True, blank=True)

    def __str__(self):
        return f'{self.id} - {self.nome}'
    
    class Meta:
        verbose_name = 'Organizador'
        verbose_name_plural = 'Organizadores'
        ordering = ['id']
    
class Categoria(models.Model):
    nome = models.CharField(max_length=50, unique=True, blank=True)
    descricao = models.CharField(max_length=1000, default='', blank=True)
    ativo_inativo = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return f'{self.id} - {self.nome}'
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']

class Evento(models.Model):
    titulo = models.CharField(max_length=50, unique=True, blank=True)
    descricao = models.CharField(max_length=1000, blank=True)
    rua = models.CharField(max_length=50, blank=True)
    bairro = models.CharField(max_length=50, blank=True)
    numero = models.IntegerField(blank=True)
    cidade = models.CharField(max_length=50, blank=True)
    estado = models.CharField(max_length=2, blank=True)
    pais = models.CharField(max_length=50, blank=True)
    data = models.DateTimeField(blank=True)
    imagem = models.ImageField(null=True, blank=True, upload_to="imagem_pics/")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.id} - {self.data} - {self.titulo}'
    
    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        ordering = ['data']

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensagem de {self.nome} em {self.data_envio.strftime('%Y-%m-%d %H:%M:%S')}"