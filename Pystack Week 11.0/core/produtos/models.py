from django.db import models

class Produto(models.Model):
    produto = models.CharField(max_length=100)
    preco = models.DecimalField(decimal_places=2, max_digits=10)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return f'{self.produto} →  R$ {str(self.preco).replace(".", ",")}'
