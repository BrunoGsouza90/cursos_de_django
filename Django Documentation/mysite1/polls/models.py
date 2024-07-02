import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    
class Empresa(models.Model):
    registro = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.registro}'

class Profissao(models.Model):
    registro = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.registro}'
    
class Casa(models.Model):
    nome = models.CharField(max_length=200,default='')
    idade = models.IntegerField()
    profissao = models.ForeignKey(Profissao,on_delete=models.CASCADE, default='')
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, default='')

    def __str__(self):
        return f'{self.id} - {self.nome}'
    
class Pagina(models.Model):
    link = models.CharField(max_length=200, default='')
    link1 = models.CharField(max_length=200, default='')

    def __str__(self):
        return f'{self.link} - {self.link1}'
