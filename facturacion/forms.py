from django import forms

from facturacion.models import factura, factura_detalle

class facturaForm(forms.ModelForm):
	class Meta:
		model = factura
		fields = "__all__"
		widgets = {}
		labels = {}

class facturaDetalleForm(forms.ModelForm):
	#cantidad = forms.IntegerField(label='cantidad')
	#costo = forms.IntegerField(label='costo')
	#valor_total = forms.IntegerField(label='valor_total')
	class Meta:
		model = factura_detalle
		fields = "__all__"
		#widgets = {}
		#labels = {}
