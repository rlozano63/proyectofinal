from django import forms

from facturacion.models import factura, factura_detalle

class facturaForm(forms.ModelForm):
	class Meta:
		model = factura
		fields = "__all__"

	def __init__(self, *args, **kwargs):
		super(facturaForm, self).__init__(*args, **kwargs)

		self.fields['fecha_creacion'].widget.attrs.update({'v-model' : 'facturacion.forms.create.fecha_creacion'})
		self.fields['factualizacion'].widget.attrs.update({'v-model' : 'facturacion.forms.create.factualizacion'})
		self.fields['valor_total'].widget.attrs.update({'v-model' : 'facturacion.forms.create.valor_total'})
		self.fields['cliente'].widget.attrs.update({'readonly':True, 'v-model' : 'facturacion.forms.create.cliente'})

class facturaDetalleForm(forms.ModelForm):
	class Meta:
		model = factura_detalle
		fields = "__all__"

	def __init__(self, *args, **kwargs):
		super(facturaDetalleForm, self).__init__(*args, **kwargs)

		self.fields['producto'].widget.attrs.update({'v-model' : 'facturacion.forms.create.deta.producto'})
		self.fields['cantidad'].widget.attrs.update({'v-model' : 'facturacion.forms.create.deta.cantidad'})
		self.fields['valor'].widget.attrs.update({'v-model' : 'facturacion.forms.create.deta.valor'})
		self.fields['valor_total'].widget.attrs.update({'readonly':True, 'v-model' : 'facturacion.forms.create.deta.valor_total'})