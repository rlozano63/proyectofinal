# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-22 23:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10)),
                ('apellido', models.CharField(max_length=10)),
                ('nombre_tienda', models.CharField(max_length=10)),
                ('regimen', models.CharField(max_length=10)),
                ('direccion', models.CharField(max_length=10)),
                ('telefono', models.CharField(max_length=10)),
                ('orden_ruta', models.IntegerField()),
                ('pos_x', models.CharField(max_length=50)),
                ('pos_y', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='distribuidor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('cedula', models.IntegerField()),
                ('usuario', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('cantidad', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('fecha', models.DateTimeField()),
                ('stock_minimo', models.IntegerField(default=10)),
                ('stock_maximo', models.IntegerField(default=200)),
            ],
        ),
        migrations.CreateModel(
            name='proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('cedula', models.IntegerField()),
                ('empresa', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='unidades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='unida',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.unidades'),
        ),
    ]
