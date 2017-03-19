# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-12 14:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='inventario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField()),
                ('factualizacion', models.DateTimeField()),
                ('valor_total', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='inventario_detalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('costo', models.IntegerField()),
                ('valor_total', models.IntegerField()),
                ('inventario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.inventario')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.producto')),
            ],
        ),
        migrations.CreateModel(
            name='movimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField()),
                ('factualizacion', models.DateTimeField()),
                ('valor_total', models.IntegerField(default=0)),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='movimiento_detalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('valor', models.IntegerField()),
                ('valor_total', models.IntegerField()),
                ('movimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.movimiento')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.producto')),
            ],
        ),
        migrations.CreateModel(
            name='tipo_movimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalle', models.TextField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='movimiento',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.tipo_movimiento'),
        ),
    ]
