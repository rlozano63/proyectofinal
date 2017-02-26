from django import forms

from catalogo.models import catalogo, catalogo_detalle

class catalogoForm(forms.ModelForm):
	class Meta:
		model = factura
		fields = "__all__"
		widgets = {}
		labels = {}

class catalogoDetalleForm(forms.ModelForm):
	#cantidad = forms.IntegerField(label='cantidad')
	#costo = forms.IntegerField(label='costo')
	#valor_total = forms.IntegerField(label='valor_total')
	class Meta:
		model = catalogo_detalle
		fields = "__all__"
		#widgets = {}
		#labels = {}
