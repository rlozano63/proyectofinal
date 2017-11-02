# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-02 22:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion', '0003_auto_20171102_2224'),
        ('inventario', '0002_auto_20171102_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='movimiento',
            name='factura',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='facturacion.factura'),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='factualizacion',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 2, 22, 24, 54, 346150)),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 2, 22, 24, 54, 346049)),
        ),
    ]