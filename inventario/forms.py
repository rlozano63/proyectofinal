from django import forms

from inventario.models import *

class inventarioForm(forms.ModelForm):
	class Meta:
		model = inventario
		fields = "__all__"
		widgets = {}
		labels = {}

class inventarioDetalleForm(forms.ModelForm):
	#cantidad = forms.IntegerField(label='cantidad')
	#costo = forms.IntegerField(label='costo')
	#valor_total = forms.IntegerField(label='valor_total')
	class Meta:
		model = inventario_detalle
		fields = "__all__"
		#widgets = {}
		#labels = {}

class movimientoForm(forms.ModelForm):
	class Meta:
		model = movimiento
		fields = "__all__"
		widgets = {}
		labels = {}

class movimientoDetalleForm(forms.ModelForm):
	#cantidad = forms.IntegerField(label='cantidad')
	#costo = forms.IntegerField(label='costo')
	#valor_total = forms.IntegerField(label='valor_total')
	class Meta:
		model = movimiento_detalle
		fields = "__all__"
		#widgets = {}
		#labels = {}
