from django import forms

from facturacion.models import factura, factura_detalle

class facturaForm(forms.ModelForm):
	class Meta:
		model = factura
		fields = "__all__"
		exclude = ["factualizacion"]

	def __init__(self, *args, **kwargs):
		super(facturaForm, self).__init__(*args, **kwargs)

		
		self.fields['fecha_creacion'].widget.attrs.update({'v-model' : 'facturacion.forms.create.fecha_creacion'})
		self.fields['fecha_creacion'].label = "Fecha"
				
		self.fields['valor_total'].widget.attrs.update({'readonly':True,'v-model' : 'facturacion.forms.create.valor_total'})
		self.fields['valor_total'].label = "Total"
		
		self.fields['cliente'].widget.attrs.update({ 'v-model' : 'facturacion.forms.create.cliente'})
		self.fields['cliente'].label= "Cliente"
class facturaDetalleForm(forms.ModelForm):
	class Meta:
		model = factura_detalle
		fields = "__all__"
		exclude = ["factura"]

	def __init__(self, *args, **kwargs):
		super(facturaDetalleForm, self).__init__(*args, **kwargs)

		self.fields['producto'].label = "Producto"
		self.fields['producto'].widget.attrs.update({'v-model' : 'facturacion.forms.create.deta.producto'})
		
		self.fields['cantidad'].label = "Cantidad"
		self.fields['cantidad'].widget.attrs.update({'v-model' : 'facturacion.forms.create.deta.cantidad' , 'min':0 })
		
		self.fields['valor'].label = "Valor Unitario"
		self.fields['valor'].widget.attrs.update({'v-model' : 'facturacion.forms.create.deta.valor'})

		self.fields['valor_total'].label = "Valor Total"
		self.fields['valor_total'].widget.attrs.update({'readonly':True,'readonly':True, 'v-model' : 'facturacion.forms.create.deta.valor_total'})