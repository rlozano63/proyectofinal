from django import forms

from catalogo.models import catalogo, catalogo_detalle

class catalogoForm(forms.ModelForm):
	class Meta:
		model = catalogo
		fields = "__all__"
		exclude = ["factualizacion"]
		widgets = {}
		labels = {}

	def __init__(self, *args, **kwargs):
		super(catalogoForm, self).__init__(*args, **kwargs)
		self.fields['fecha_creacion'].label = "Fecha"
		self.fields['fecha_creacion'].widget.attrs.update({'v-model' : 'catalogo.forms.create.fecha_creacion'})


class catalogoDetalleForm(forms.ModelForm):
	#cantidad = forms.IntegerField(label='cantidad')
	#costo = forms.IntegerField(label='costo')
	#valor_total = forms.IntegerField(label='valor_total')
	class Meta:
		model = catalogo_detalle
		fields = "__all__"
		#widgets = {}
		#labels = {}
		widgets = {
			'cantidad': forms.NumberInput(attrs={'min': '0', 'pattern' : "^[1-9]\d*$"}),
			'valor': forms.NumberInput(attrs={'min': '0', 'pattern' : "^[1-9]\d*$"}),
			'valor_total': forms.NumberInput(attrs={'min': '0', 'pattern' : "^[1-9]\d*$"}),
		}

	def __init__(self, *args, **kwargs):
		super(catalogoDetalleForm, self).__init__(*args, **kwargs)
		self.fields['producto'].label = "Producto"
		self.fields['producto'].widget.attrs.update({'v-model' : 'catalogo.forms.create.deta.producto'})
		self.fields['cantidad'].label = "Cantidad"
		self.fields['cantidad'].widget.attrs.update({'v-model' : 'catalogo.forms.create.deta.cantidad'})
		self.fields['valor'].label = "Valor"
		self.fields['valor'].widget.attrs.update({'v-model' : 'catalogo.forms.create.deta.valor'})
		self.fields['valor_total'].label = "Valor Total"
		self.fields['valor_total'].widget.attrs.update({'readonly':True, 'v-model' : 'catalogo.forms.create.deta.valor_total'})
