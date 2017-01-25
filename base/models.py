from __future__ import unicode_literals

from django.db import models

# Create your models here.
class producto(models.Model):
	"""docstring for producto"""
	
	nombre = models.TextField(max_length=20)
	cantidad = models.IntegerField(max_length=50)
	precio = models.IntegerField(max_length=20)
	fecha = models.DateTimeField()

	#def __init__(self, arg):
	#	super(producto, self).__init__()
	#	self.arg = arg

	def __str__(self):
		return self.nombre

class distribuidor(models.Model):
	"""docstring for ClassName"""
	nombre = models.TextField(max_length=20)
	apellido = models.TextField(max_length=20)
	cedula = models.IntegerField(max_length=20)
	
	#def __init__(self, arg):
	#	super(ClassName, self).__init__()
	#	self.arg = arg
		
	def __str__(self):
		return self.nombre		
		
		