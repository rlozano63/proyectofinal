from __future__ import unicode_literals

from django.db import models
import datetime
from base.models import producto, proveedor
from facturacion.models import factura

# Create your models here.

class inventario(models.Model):
	"""docstring for inventario"""
	fecha_creacion = models.DateTimeField(default=datetime.datetime.now())
	factualizacion = models.DateTimeField(default=datetime.datetime.now())
	valor_total = models.IntegerField(default=0)

class inventario_detalle(models.Model):
	"""docstring for inventario"""
	inventario = models.ForeignKey(inventario)
	producto = models.ForeignKey(producto)
	cantidad = models.IntegerField()
	costo = models.IntegerField()
	valor_total = models.IntegerField()


class tipo_movimiento(models.Model):
	detalle = models.TextField(max_length=50)
	slug = models.TextField(max_length=50,unique=True,blank=True,null=True)

	def __str__(self):
		return self.detalle

class movimiento(models.Model):
	"""docstring for movimiento"""
	fecha_creacion = models.DateTimeField(default=datetime.datetime.now())
	proveedor = models.ForeignKey(proveedor, blank=True,null=True)
	tipo = models.ForeignKey(tipo_movimiento)
	factualizacion = models.DateTimeField(default=datetime.datetime.now())
	factura = models.ForeignKey(factura, blank=True,null=True)
	valor_total = models.IntegerField(default=0)

class movimiento_detalle(models.Model):
	"""docstring for movimiento"""
	movimiento = models.ForeignKey(movimiento)
	producto = models.ForeignKey(producto)
	cantidad = models.IntegerField()
	valor = models.IntegerField()
	valor_total = models.IntegerField()
