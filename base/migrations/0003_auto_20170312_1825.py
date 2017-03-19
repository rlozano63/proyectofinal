# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-12 23:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20170310_1521'),
    ]

    operations = [
        migrations.CreateModel(
            name='unidades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='producto',
            name='unida',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.unidades'),
        ),
    ]