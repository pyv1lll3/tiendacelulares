# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-07 17:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='precio',
            name='descripcion',
            field=models.CharField(default='Detalle del precio', max_length=50),
        ),
    ]