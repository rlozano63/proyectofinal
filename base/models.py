from __future__ import unicode_literals

from django.db import models

# Create your models here.
class producto(models.Model):
	"""docstring for producto"""
	
	nombre = models.TextField(max_length=50)
	cantidad = models.IntegerField()
	precio = models.IntegerField()
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
	cedula = models.IntegerField()
	
	#def __init__(self, arg):
	#	super(ClassName, self).__init__()
	#	self.arg = arg
		
	def __str__(self):
		return self.nombre		
		

class cliente(object):
	"""docstring for cliente"""
	nombre = models.TextField(max_length=20)
	apellido = models.TextField(max_length=20)
	nombre_tienda = models.TextField(max_length=20)
	regimen = models.TextField(max_length=20)
	direccion = models.CharField(max_length=20)
	#def __init__(self, arg):
		#super(cliente, self).__init__()
		#self.arg = arg
		
	def __str__(self):
		return self.nombre