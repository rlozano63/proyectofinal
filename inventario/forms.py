from django import forms

from inventario.models import *

class inventarioForm(forms.ModelForm):
	class Meta:
		model = inventario
		fields = "__all__"
		exclude = ["factualizacion"]
		widgets = {
			'valor_total': forms.NumberInput(attrs={'min': '0', 'pattern' : "^[1-9]\d*$"}),
		}

	def __init__(self, *args, **kwargs):
		super(inventarioForm, self).__init__(*args, **kwargs)
		self.fields['fecha_creacion'].label = "Fecha"
		self.fields['fecha_creacion'].widget.attrs.update({'v-model' : 'inventarios.forms.create.fecha_creacion'})
		self.fields['valor_total'].label = "Total"
		self.fields['valor_total'].widget.attrs.update({'readonly':True, 'v-model' : 'inventarios.forms.create.valor_total'})

class inventarioDetalleForm(forms.ModelForm):
	class Meta:
		model = inventario_detalle
		fields = "__all__"
		exclude = ["inventario"]
		widgets = {
			'cantidad': forms.NumberInput(attrs={'min': '0', 'pattern' : "^[1-9]\d*$"}),
			'costo': forms.NumberInput(attrs={'min': '0', 'pattern' : "^[1-9]\d*$"}),
			'valor_total': forms.NumberInput(attrs={'min': '0', 'pattern' : "^[1-9]\d*$"}),
		}

	def __init__(self, *args, **kwargs):
		super(inventarioDetalleForm, self).__init__(*args, **kwargs)
		self.fields['producto'].label = "Producto"
		self.fields['producto'].widget.attrs.update({'v-model' : 'inventarios.forms.create.deta.producto'})
		self.fields['cantidad'].label = "Cantidad"
		self.fields['cantidad'].widget.attrs.update({'v-model' : 'inventarios.forms.create.deta.cantidad'})
		self.fields['costo'].label = "Costo"
		self.fields['costo'].widget.attrs.update({'v-model' : 'inventarios.forms.create.deta.costo'})
		self.fields['valor_total'].label = "Valor Total"
		self.fields['valor_total'].widget.attrs.update({'readonly':True, 'v-model' : 'inventarios.forms.create.deta.valor_total'})

class movimientoForm(forms.ModelForm):
	class Meta:
		model = movimiento
		fields = "__all__"
		exclude = ["factura", "factualizacion"]
		widgets = {
			'valor_total': forms.NumberInput(attrs={'min': '0', 'pattern' : "^[1-9]\d*$"}),
		}

	def __init__(self, *args, **kwargs):
		super(movimientoForm, self).__init__(*args, **kwargs)
		self.fields['fecha_creacion'].label = "Fecha"
		self.fields['fecha_creacion'].widget.attrs.update({'v-model' : 'movimientos.forms.create.fecha_creacion'})
		self.fields['proveedor'].label = "Proveedor"
		self.fields['proveedor'].widget.attrs.update({'v-model' : 'movimientos.forms.create.proveedor'})
		self.fields['tipo'].label = "Tipo"
		self.fields['tipo'].widget.attrs.update({'v-model' : 'movimientos.forms.create.tipo'})
		self.fields['valor_total'].label = "Valor Total"
		self.fields['valor_total'].widget.attrs.update({'readonly':True, 'v-model' : 'movimientos.forms.create.valor_total'})


class movimientoDetalleForm(forms.ModelForm):
	class Meta:
		model = movimiento_detalle
		fields = "__all__"
		exclude = ["movimiento"]
		widgets = {
			'cantidad': forms.NumberInput(attrs={'min': '0', 'pattern' : "^[1-9]\d*$"}),
			'valor': forms.NumberInput(attrs={'min': '0', 'pattern' : "^[1-9]\d*$"}),
			'valor_total': forms.NumberInput(attrs={'min': '0', 'pattern' : "^[1-9]\d*$"}),
		}

	def __init__(self, *args, **kwargs):
		super(movimientoDetalleForm, self).__init__(*args, **kwargs)
		self.fields['producto'].label = "Producto"
		self.fields['producto'].widget.attrs.update({'v-model' : 'movimientos.forms.create.deta.producto'})
		self.fields['cantidad'].label = "Cantidad"
		self.fields['cantidad'].widget.attrs.update({'v-model' : 'movimientos.forms.create.deta.cantidad'})
		self.fields['valor'].label = "Valor"
		self.fields['valor'].widget.attrs.update({'v-model' : 'movimientos.forms.create.deta.valor'})
		self.fields['valor_total'].label = "Valor Total"
		self.fields['valor_total'].widget.attrs.update({'readonly':True, 'v-model' : 'movimientos.forms.create.deta.valor_total'})
