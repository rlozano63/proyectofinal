from __future__ import unicode_literals

from django.db import models

class unidades(models.Model):
	nombre = models.CharField(max_length=20)
	def natural_key(self):
		return {
			"nombre" : self.nombre
		}

class producto(models.Model):
	"""docstring for producto"""

	nombre = models.CharField(max_length=20)
	cantidad = models.IntegerField()
	precio = models.IntegerField()
	fecha = models.DateTimeField()
	unida = models.ForeignKey(unidades)
	stock_minimo = models.IntegerField(default=10)
	stock_maximo = models.IntegerField(default=200)

	def __str__(self):
		return self.nombre

	def natural_key(self):
		return {
			"nombre" : self.nombre,
			"cantidad" : self.cantidad,
			"precio" : self.precio,
			"fecha" : self.fecha,
			"unida" : self.unida.natural_key(),
			"stock_minimo" : self.stock_minimo,
			"stock_maximo" : self.stock_maximo,
		}

class distribuidor(models.Model):
	"""docstring for ClassName"""
	nombre = models.CharField(max_length=20)
	apellido = models.CharField(max_length=20)
	cedula = models.IntegerField()

	def __str__(self):
		return self.nombre

class proveedor(models.Model):
	"""docstring for ClassName"""
	nombre = models.CharField(max_length=20)
	apellido = models.CharField(max_length=20)
	cedula = models.IntegerField()
	empresa = models.CharField(max_length=20)

	def __str__(self):
		return self.nombre


class cliente(models.Model):
	"""docstring for cliente"""
	nombre = models.CharField(max_length=10)
	apellido = models.CharField(max_length=10)
	nombre_tienda = models.CharField(max_length=10)
	regimen = models.CharField(max_length=10)
	direccion = models.CharField(max_length=10)
	telefono = models.CharField(max_length=10)
	
	
	orden_ruta = models.IntegerField()
	pos_x = models.CharField(max_length=50)
	pos_y = models.CharField(max_length=50)


	def __str__(self):
		return self.nombre
