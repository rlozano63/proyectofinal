from django.shortcuts import render

from base.views import AjaxableResponseMixin

from facturacion.forms import *
from django.views.generic.edit import CreateView

from django.core.urlresolvers import reverse_lazy



# Create your views here.

class FacturaCreation(AjaxableResponseMixin,CreateView):
	model = factura
	template_name = 'factura/crear.html'
	#form_class = facturaForm
	fields = "__all__"
	success_url = reverse_lazy('listar_productos')

	def get_context_data(self,**kwargs):
		context = super(FacturaCreation, self).get_context_data(**kwargs)
		context['form_detalle'] = facturaDetalleForm()
		print context['form_detalle']
		return context

class FacturaDetaleCreation(AjaxableResponseMixin,CreateView):
	model = factura_detalle
	#template_name = 'factura/detalle_crear.html'
	#form_class = facturaForm
	fields = "__all__"
	success_url = reverse_lazy('listar_productos')

