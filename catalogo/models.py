from __future__ import unicode_literals

from django.db import models
import datetime
from base.models import producto,distribuidor

from django.core.validators import MinValueValidator

# Create your models here.

class catalogo(models.Model):
	"""docstring for factura"""
	fecha_creacion = models.DateTimeField(default=datetime.datetime.now())
	factualizacion = models.DateTimeField(default=datetime.datetime.now())
	distribuidor = models.ForeignKey(distribuidor)


class catalogo_detalle(models.Model):
	"""docstring for factura"""
	catalogo = models.ForeignKey(catalogo)
	producto = models.ForeignKey(producto,related_name="item")
	cantidad = models.IntegerField(validators=[MinValueValidator(0)])
	valor = models.IntegerField(validators=[MinValueValidator(0)])
	valor_total = models.IntegerField(validators=[MinValueValidator(0)])


