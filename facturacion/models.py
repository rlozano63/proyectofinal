from __future__ import unicode_literals

from django.db import models

from base.models import producto, distribuidor

# Create your models here.

class factura(models.Model):
	"""docstring for factura"""
	fecha_creacion = models.DateTimeField()
	factualizacion = models.DateTimeField()
	valor_total = models.IntegerField(default=0)

class factura_detalle(models.Model):
	"""docstring for factura"""
	producto = models.ForeignKey(producto)
	cantidad = models.IntegerField()
	valor = models.IntegerField()
	valor_total = models.IntegerField()



class catalogo(models.Model):
	"""docstring for catalogo"""
	nombre = models.TextField(max_length=20)
	distribuidor = models.ForeignKey(distribuidor)

class catalogo_detalle(models.Model):
	"""docstring for catalogo"""
	catalogo = models.ForeignKey(catalogo)
	producto = models.ForeignKey(producto)

