# Generated by Django 5.0.6 on 2024-07-06 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projeto_eventos', '0003_categoria_organizador_alter_evento_bairro_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias'},
        ),
        migrations.AlterModelOptions(
            name='evento',
            options={'verbose_name': 'Evento', 'verbose_name_plural': 'Eventos'},
        ),
        migrations.AlterModelOptions(
            name='organizador',
            options={'verbose_name': 'Organizador', 'verbose_name_plural': 'Organizadores'},
        ),
    ]
