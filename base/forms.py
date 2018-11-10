from django import forms
from base.models import producto, distribuidor, cliente, proveedor

class ProductoForm(forms.ModelForm):
	class Meta:
		model = producto
		fields = "__all__"
		widgets = {
			'fecha': forms.DateInput(attrs={'type': 'date'}),
			'cantidad': forms.NumberInput(attrs={'min': '0', 'pattern' : "^[1-9]\d*$"}),
			'precio': forms.NumberInput(attrs={'min': '0', 'pattern' : "^[1-9]\d*$"}),
		}

class DistribuidorForm(forms.Form):
	class Meta:
		model = distribuidor
		fields = "__all__"

class ClienteForm(forms.Form):
	class Meta:
		model = cliente
		fields = "__all__"
		widgets = {

		}
class ProveedorForm(forms.Form):
	class Meta:
		model = proveedor
		fields = "__all__"

