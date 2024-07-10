from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ddd = models.CharField(max_length=3)
    telefone = models.CharField(max_length=10)
    nickname = models.CharField(max_length=30, blank=True, null=True)
    sobre_voce = models.TextField(blank=True, null=True)
    foto = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    foto_de_capa = models.ImageField(upload_to='cover_pics/', blank=True, null=True)

    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()