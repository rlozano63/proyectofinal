from __future__ import unicode_literals

from django.db import models

from base.models import producto

# Create your models here.

class catalogo(models.Model):
	"""docstring for factura"""
	fecha_creacion = models.DateTimeField()
	factualizacion = models.DateTimeField()
	

class catalogo_detalle(models.Model):
	"""docstring for factura"""
	producto = models.ForeignKey(producto)
	cantidad = models.IntegerField()
	valor = models.IntegerField()
	valor_total = models.IntegerField()
