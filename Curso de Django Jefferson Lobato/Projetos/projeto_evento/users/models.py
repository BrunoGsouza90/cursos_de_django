from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    sobre_voce = models.TextField(blank=True, verbose_name='Sobre você')
    foto = models.ImageField(upload_to='profile_photos/', blank=True, null=True, verbose_name='Foto')
    foto_de_capa = models.ImageField(upload_to='cover_photos/', blank=True, null=True, verbose_name='Foto de capa')
    primeiro_nome = models.CharField(max_length=30, verbose_name='Primeiro nome')
    ultimo_nome = models.CharField(max_length=150, verbose_name='Último nome')
    email = models.EmailField(verbose_name='Endereço de email')
    pais = models.CharField(max_length=100, verbose_name='País')
    cidade = models.CharField(max_length=100, verbose_name='Cidade')
    endereco = models.CharField(max_length=255, verbose_name='Endereço')
    telefone = models.CharField(max_length=20, verbose_name='Número de telefone')

    def __str__(self):
        return self.username