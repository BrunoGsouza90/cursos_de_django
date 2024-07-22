import datetime
from django.contrib import admin
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField('Pergunta', max_length=200)
    pub_date = models.DateTimeField('Data / Horário de criação')
    
    def __str__(self):
        return self.question_text
    
    @admin.display(
            boolean = True,
            ordering = 'pub_date',
            description = 'Publicado recentemente?'
    )
    def publicacoes_recentes(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Selecione a Pergunta')
    choice_text = models.CharField('Escolha', max_length=200)
    votes = models.IntegerField('Quantidade de votos', default=0)

    def __str__(self):
        return self.choice_text