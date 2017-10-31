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
	def __init__(self, *args, **kwargs):
		super(movimientoForm, self).__init__(*args, **kwargs)
		self.fields['fecha_creacion'].widget.attrs.update({'v-model' : 'movimientos.forms.create.fecha_creacion'})
		self.fields['proveedor'].widget.attrs.update({'v-model' : 'movimientos.forms.create.proveedor'})
		self.fields['tipo'].widget.attrs.update({'v-model' : 'movimientos.forms.create.tipo'})
		self.fields['factualizacion'].widget.attrs.update({'v-model' : 'movimientos.forms.create.factualizacion'})
		self.fields['valor_total'].widget.attrs.update({'v-model' : 'movimientos.forms.create.valor_total'})


class movimientoDetalleForm(forms.ModelForm):
	class Meta:
		model = movimiento_detalle
		fields = "__all__"
		
	def __init__(self, *args, **kwargs):
		super(movimientoDetalleForm, self).__init__(*args, **kwargs)
		self.fields['producto'].widget.attrs.update({'v-model' : 'movimientos.forms.create.deta.producto'})
		self.fields['cantidad'].widget.attrs.update({'v-model' : 'movimientos.forms.create.deta.cantidad'})
		self.fields['valor'].widget.attrs.update({'v-model' : 'movimientos.forms.create.deta.valor'})
		self.fields['valor_total'].widget.attrs.update({'v-model' : 'movimientos.forms.create.deta.valor_total'})