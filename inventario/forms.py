from django import forms

from inventario.models import inventario, inventario_detalle

class inventarioForm(forms.Form):
	class Meta:
		model = inventario
		fields = "__all__"
		widgets = {}
		labels = {}

class inventarioDetalleForm(forms.Form):
	#cantidad = forms.IntegerField(label='cantidad')
	#costo = forms.IntegerField(label='costo')
	#valor_total = forms.IntegerField(label='valor_total')
	class Meta:
		model = inventario_detalle
		fields = "__all__"
		widgets = {}
		labels = {}
