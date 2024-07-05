from django.db import models

class Topic(models.Model):
    '''Um assunto sobre qual o usuário está aprendendo. '''
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        '''Devolve uma representação em String do modelo.'''
        return self.text

class Entry(models.Model):
    '''Algo específico aprendido sobre um assunto.'''
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    nome = models.CharField(max_length=70, null = False)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        '''Devolve uma represetação en string do modelo.'''
        return f'{self.id} - {self.text[:50] + '...'}'