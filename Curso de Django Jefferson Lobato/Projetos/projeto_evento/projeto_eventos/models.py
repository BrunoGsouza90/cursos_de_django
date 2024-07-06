from django.db import models # type: ignore

class Evento(models.Model):
    titulo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=1000)
    rua = models.CharField(max_length=50)
    bairro = models.CharField(max_length=30)
    numero = models.IntegerField()
    cidade = models.CharField(max_length=30)
    estado = models.CharField(max_length=2)
    pais = models.CharField(max_length=30)
    data = models.DateField()