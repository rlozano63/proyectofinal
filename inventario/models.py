from __future__ import unicode_literals

from django.db import models

from base.models import producto, proveedor

# Create your models here.

class inventario(models.Model):
	"""docstring for inventario"""
	fecha_creacion = models.DateTimeField()
	factualizacion = models.DateTimeField()
	valor_total = models.IntegerField(default=0)

class inventario_detalle(models.Model):
	"""docstring for inventario"""
	producto = models.ForeignKey(producto)
	cantidad = models.IntegerField()
	costo = models.IntegerField()
	valor_total = models.IntegerField()


class tipo_movimiento(models.Model):
	detalle = models.TextField(max_length=50)

class movimiento(models.Model):
	"""docstring for movimiento"""
	fecha_creacion = models.DateTimeField()
	proveedor = models.ForeignKey(proveedor)
	tipo = models.ForeignKey(tipo_movimiento)
	factualizacion = models.DateTimeField()
	valor_total = models.IntegerField(default=0)

class movimiento_detalle(models.Model):
	"""docstring for movimiento"""
	producto = models.ForeignKey(producto)
	cantidad = models.IntegerField()
	valor = models.IntegerField()
	valor_total = models.IntegerField()
