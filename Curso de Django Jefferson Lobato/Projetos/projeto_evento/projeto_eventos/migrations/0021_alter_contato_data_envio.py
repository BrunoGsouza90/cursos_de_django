# Generated by Django 5.0.6 on 2024-07-07 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projeto_eventos', '0020_alter_contato_data_envio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='data_envio',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
