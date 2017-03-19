from django.shortcuts import render

from base.views import AjaxableResponseMixin

from facturacion.forms import *
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy

from inventario.views import calcular_cantidad



# Create your views here.

class FacturaList(AjaxableResponseMixin,ListView):
	model = factura
	template_name = 'factura/listar.html'
	fields = "__all__"
	success_url = reverse_lazy('listar_factura')

	def get_context_data(self,**kwargs):
		context = super(FacturaList, self).get_context_data(**kwargs)
		return context
def FacturaDetail(request, pkfactura):
	objfactura = factura.objects.get(pk=pkfactura)
	queryset = factura_detalle.objects.filter(factura=objfactura)
	context = {"factura":objfactura,"detalle":queryset}
	return render(request,"factura/detalle.html",context)


class FacturaCreation(AjaxableResponseMixin,CreateView):
	model = factura
	template_name = 'factura/create.html'
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
	def form_valid(self, form):

		deta = form.instance
		tipo_movimiento = 2 # Salida
		calcular_cantidad(deta.producto.pk,tipo_movimiento,deta.cantidad)

		return super(FacturaDetaleCreation, self).form_valid(form)
