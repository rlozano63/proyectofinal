from django import forms
from base.models import producto, distribuidor, cliente

class ProductoForm(forms.Form):
    class Meta:
        model = producto
        fields = "__all__"

class DistribuidorForm(forms.Form):
	class Meta:
		model = distribuidor
		fields = "__all__"
		
class ClienteForm(forms.Form):
	class Meta:
		model = cliente
		fields = "__all__"
			
	
