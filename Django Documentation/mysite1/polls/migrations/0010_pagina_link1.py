# Generated by Django 5.0.6 on 2024-06-14 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_pagina'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagina',
            name='link1',
            field=models.CharField(default='', max_length=200),
        ),
    ]
