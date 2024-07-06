from django.db import models # type: ignore

class Organizador(models.Model):
    nome = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=200, unique=True, null=True, blank=True)
    ddd = models.CharField(max_length=2, null=True, blank=True)
    telefone = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f'{self.id} - {self.nome}'
    
    class Meta:
        verbose_name = 'Organizador'
        verbose_name_plural = 'Organizadores'
    
class Categoria(models.Model):
    nome = models.CharField(max_length=30, unique=True, null=True, blank=True)
    descricao = models.CharField(max_length=1000, null=True, blank=True)
    ativo_inativo = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return f'{self.id} - {self.nome}'
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Evento(models.Model):
    titulo = models.CharField(max_length=30, null=True, blank=True)
    descricao = models.CharField(max_length=1000, null=True, blank=True)
    rua = models.CharField(max_length=50, null=True, blank=True)
    bairro = models.CharField(max_length=30, null=True, blank=True)
    numero = models.IntegerField(null=True, blank=True)
    cidade = models.CharField(max_length=30, null=True, blank=True)
    estado = models.CharField(max_length=2, null=True, blank=True)
    pais = models.CharField(max_length=30, null=True, blank=True)
    data = models.DateField(null=True, blank=True)
    imagem = models.ImageField(upload_to='eventos_imagens/', null=True, blank=True)
    organizador = models.ForeignKey(Organizador,on_delete=models.SET_NULL, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.id} - {self.titulo}'
    
    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
