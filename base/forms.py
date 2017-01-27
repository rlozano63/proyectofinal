from django import forms
from base.models import producto, distribuidor, cliente

class ProductoForm(forms.Form):
    class Meta:
        model = producto
        fields = "__all__"

class DistribuidorForm(forms.Form):
	class Meta1:
		model = distribuidor
		fields = "__all__"
		
class ClienteForm(forms.Form):
	class Meta2:
		model = cliente
		fields = "__all__"
			
	
