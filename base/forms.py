from django import forms
from base.models import producto

class ProductoForm(forms.Form):
    class Meta:
        model = producto
        fields = "__all__"

