# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-17 19:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emmang', '0004_empleado_descripcion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='log',
            name='empleado',
        ),
        migrations.RemoveField(
            model_name='comentario',
            name='archivo',
        ),
        migrations.RemoveField(
            model_name='subcomentario',
            name='archivo',
        ),
        migrations.DeleteModel(
            name='Log',
        ),
    ]