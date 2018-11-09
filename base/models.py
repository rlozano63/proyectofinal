from __future__ import unicode_literals
#from catalogo.models import catalogo
from django.db import models
from django.contrib.auth.models import User

from django.core.validators import MinValueValidator

class unidades(models.Model):
	nombre = models.CharField(max_length=45)
	def __str__(self):
		return self.nombre
	def natural_key(self):
		return {
			"nombre" : self.nombre
		}

class producto(models.Model):
	"""docstring for producto"""

	nombre = models.CharField(max_length=45)
	cantidad = models.IntegerField(validators=[MinValueValidator(0)])
	precio = models.IntegerField(validators=[MinValueValidator(0)])
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
	nombre = models.CharField(max_length=45)
	apellido = models.CharField(max_length=45)
	cedula = models.CharField(max_length=45)
	usuario = models.ForeignKey(User,blank=True,null=True,default=None)
	direccion = models.CharField(max_length=45)
	telefono = models.CharField(max_length=45)
	#catalogo = models.ForeignKey(catalogo)

	def __str__(self):
		return self.nombre

class proveedor(models.Model):
	"""docstring for ClassName"""
	nombre = models.CharField(max_length=45)
	apellido = models.CharField(max_length=45)
	cedula = models.CharField(max_length=45)
	empresa = models.CharField(max_length=45)
	direccion = models.CharField(max_length=45)
	telefono = models.CharField(max_length=45)

	def __str__(self):
		return self.nombre

class bodegas(models.Model):
	"""docstring for ClassName"""
	nombre = models.CharField(max_length=45)
	direccion = models.CharField(max_length=45)
	telefono = models.CharField(max_length=45)
	pos_x = models.CharField(max_length=50)
	pos_y = models.CharField(max_length=50)

	def __str__(self):
		return self.nombre


class cliente(models.Model):
	class Meta:
		ordering = ['orden_ruta']

	"""docstring for cliente"""
	nombre = models.CharField(max_length=45)
	apellido = models.CharField(max_length=45)
	nombre_tienda = models.CharField(max_length=45)
	regimen = models.CharField(max_length=45)
	direccion = models.CharField(max_length=45)
	telefono = models.CharField(max_length=45)


	orden_ruta = models.IntegerField()
	pos_x = models.CharField(max_length=50)
	pos_y = models.CharField(max_length=50)

	ruta_activa = models.CharField(max_length=1,default=1)


	def __str__(self):
		return self.nombre
