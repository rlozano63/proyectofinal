from __future__ import unicode_literals

from django.db import models

class producto(models.Model):
	"""docstring for producto"""

	nombre = models.TextField(max_length=50)
	cantidad = models.IntegerField()
	precio = models.IntegerField()
	fecha = models.DateTimeField()

	def __str__(self):
		return self.nombre

class distribuidor(models.Model):
	"""docstring for ClassName"""
	nombre = models.TextField(max_length=20)
	apellido = models.TextField(max_length=20)
	cedula = models.IntegerField()

	def __str__(self):
		return self.nombre

class proveedor(models.Model):
	"""docstring for ClassName"""
	nombre = models.TextField(max_length=20)
	apellido = models.TextField(max_length=20)
	cedula = models.IntegerField()
	empresa = models.TextField(max_length=20)

	def __str__(self):
		return self.nombre


class cliente(models.Model):
	"""docstring for cliente"""
	nombre = models.TextField(max_length=20)
	apellido = models.TextField(max_length=20)
	nombre_tienda = models.TextField(max_length=20)
	regimen = models.TextField(max_length=20)
	direccion = models.CharField(max_length=20)
	
	#orden_ruta = models.IntegerField()
	#pos_x = TextField(max_length=50)
	#pos_y = TextField(max_length=50)


	def __str__(self):
		return self.nombre
