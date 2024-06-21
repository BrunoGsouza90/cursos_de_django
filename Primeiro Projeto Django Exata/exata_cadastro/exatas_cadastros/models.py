from django.db import models # type: ignore

class Conta(models.Model):
    registros = models.CharField(max_length=40,null='False')

    def __str__(self):
        return self.registros

class Categoria(models.Model):
    registros = models.CharField(max_length=40,null=False)

    def __str__(self):
        return self.registros

class Cadastro(models.Model):
    descricao = models.CharField(max_length=80, null=False)
    valor = models.DecimalField(max_digits=10,decimal_places=2,null=False)
    data = models.DateField(null=False)
    conta = models.ForeignKey(Conta,on_delete=models.CASCADE,default= 1)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE,default= 2)

    def __str__(self):
        return f'{self.id} - {self.conta}'
