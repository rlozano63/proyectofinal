# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-02-02 18:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='factualizacion',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 2, 18, 30, 30, 920919)),
        ),
        migrations.AlterField(
            model_name='factura',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 2, 18, 30, 30, 920871)),
        ),
    ]
