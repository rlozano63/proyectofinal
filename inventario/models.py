from __future__ import unicode_literals

from django.db import models

# Create your models here.

class inventario(models.Model):
	"""docstring for inventario"""
	fecha_creacion = DateTimeField()
	factualizacion = DateTimeField()
	valor_total = IntegerField(max_length=20)
	
	def __init__(self, arg):
		super(inventario, self).__init__()
		self.arg = arg
		