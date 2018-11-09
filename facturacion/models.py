from __future__ import unicode_literals

from django.db import models

from base.models import producto, distribuidor, cliente
import datetime

from django.core.validators import MinValueValidator

# Create your models here.

class factura(models.Model):
	"""docstring for factura"""
	fecha_creacion = models.DateTimeField(default=datetime.datetime.now())
	factualizacion = models.DateTimeField(default=datetime.datetime.now())
	valor_total = models.IntegerField(default=0, validators=[MinValueValidator(0)])
	cliente = models.ForeignKey(cliente)

class factura_detalle(models.Model):
	"""docstring for factura"""
	factura = models.ForeignKey(factura)
	producto = models.ForeignKey(producto)
	cantidad = models.IntegerField(validators=[MinValueValidator(0)])
	valor = models.IntegerField(validators=[MinValueValidator(0)])
	valor_total = models.IntegerField(validators=[MinValueValidator(0)])
