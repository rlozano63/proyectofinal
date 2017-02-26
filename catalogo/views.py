from django.shortcuts import render

from base.views import AjaxableResponseMixin

from catalogo.forms import *
from django.views.generic.edit import CreateView

from django.core.urlresolvers import reverse_lazy



# Create your views here.

class CatalogoCreation(AjaxableResponseMixin,CreateView):
	model = catalogo
	template_name = 'catalogo/crear.html'
	#form_class = facturaForm
	fields = "__all__"
	success_url = reverse_lazy('listar_productos')

	def get_context_data(self,**kwargs):
		context = super(CatalogoCreation, self).get_context_data(**kwargs)
		context['form_detalle'] = catalogoDetalleForm()
		print context['form_detalle']
		return context

class CatalogoDetaleCreation(AjaxableResponseMixin,CreateView):
	model = catalogo_detalle
	#template_name = 'factura/detalle_crear.html'
	#form_class = facturaForm
	fields = "__all__"
	success_url = reverse_lazy('listar_productos')

