# Generated by Django 5.0.6 on 2024-07-06 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projeto_eventos', '0007_alter_organizador_ddd_alter_organizador_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizador',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]