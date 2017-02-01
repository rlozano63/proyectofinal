from __future__ import unicode_literals

from django.db import models

from base.models import producto

# Create your models here.

class inventario(models.Model):
	"""docstring for inventario"""
	fecha_creacion = models.DateTimeField()
	factualizacion = models.DateTimeField()
	valor_total = models.IntegerField()

class inventario_detalle(models.Model):
	"""docstring for inventario"""
	producto = models.ForeignKey(producto)
	cantidad = models.IntegerField()
	costo = models.IntegerField()
	valor_total = models.IntegerField()

