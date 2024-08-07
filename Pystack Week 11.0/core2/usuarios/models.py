from django.db import models

class a(models.Model):

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''

    def __str__(self):
        return f''