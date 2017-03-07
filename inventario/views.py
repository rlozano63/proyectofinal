from django.shortcuts import render

from base.views import AjaxableResponseMixin

from inventario.forms import *
from django.views.generic.edit import CreateView

from django.core.urlresolvers import reverse_lazy



# Create your views here.

class InventarioCreation(AjaxableResponseMixin,CreateView):
	model = inventario
	template_name = 'inventario/crear.html'
	#form_class = inventarioForm
	fields = "__all__"
	success_url = reverse_lazy('listar_productos')

	def get_context_data(self,**kwargs):
		context = super(InventarioCreation, self).get_context_data(**kwargs)
		context['form_detalle'] = inventarioDetalleForm()
		print context['form_detalle']
		return context

class InventarioDetaleCreation(AjaxableResponseMixin,CreateView):
	model = inventario_detalle
	#template_name = 'inventario/detalle_crear.html'
	#form_class = inventarioForm
	fields = "__all__"
	success_url = reverse_lazy('listar_productos')
		


# Create your views here.

class MovimientoCreation(AjaxableResponseMixin,CreateView):
	model = movimiento
	template_name = 'movimiento/crear.html'
	#form_class = movimientoForm
	fields = "__all__"
	success_url = reverse_lazy('listar_productos')

	def get_context_data(self,**kwargs):
		context = super(MovimientoCreation, self).get_context_data(**kwargs)
		context['form_detalle'] = movimientoDetalleForm()
		print context['form_detalle']
		return context

class MovimientoDetaleCreation(AjaxableResponseMixin,CreateView):
	model = movimiento_detalle
	#template_name = 'movimiento/detalle_crear.html'
	#form_class = movimientoForm
	fields = "__all__"
	success_url = reverse_lazy('listar_productos')

