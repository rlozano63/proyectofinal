# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-10 20:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='unida',
            field=models.CharField(max_length=20),
        ),
        migrations.DeleteModel(
            name='unidades',
        ),
    ]
