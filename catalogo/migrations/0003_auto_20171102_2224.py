# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-02 22:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_auto_20171102_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogo',
            name='factualizacion',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 2, 22, 24, 54, 352837)),
        ),
        migrations.AlterField(
            model_name='catalogo',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 2, 22, 24, 54, 352774)),
        ),
    ]
