# Generated by Django 5.0.6 on 2024-07-06 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projeto_eventos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='eventos_imagens/'),
        ),
    ]
