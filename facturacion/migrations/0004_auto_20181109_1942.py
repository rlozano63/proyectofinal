# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-11-09 19:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0003_auto_20181026_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='factualizacion',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 9, 19, 42, 8, 709832)),
        ),
        migrations.AlterField(
            model_name='factura',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 9, 19, 42, 8, 709799)),
        ),
    ]
