from __future__ import unicode_literals

from django.db import models

# Create your models here.

class inventario(models.Model):
	"""docstring for inventario"""
	fecha_creacion = models.DateTimeField()
	factualizacion = models.DateTimeField()
	valor_total = models.IntegerField()

	def __init__(self, arg):
		super(inventario, self).__init__()
		self.arg = arg

