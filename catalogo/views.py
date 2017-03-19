from django.shortcuts import render

from base.views import AjaxableResponseMixin

from catalogo.forms import *
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView




from django.core.urlresolvers import reverse_lazy



# Create your views here.

class CatalogoList(AjaxableResponseMixin,ListView):
	model = catalogo
	template_name = 'catalogo/listar.html'
	fields = "__all__"
	success_url = reverse_lazy('listar_productos')

	def get_context_data(self,**kwargs):
		context = super(CatalogoList, self).get_context_data(**kwargs)
		return context
def CatalogoDetail(request, pkcatalogo):
	objcatalogo = catalogo.objects.get(pk=pkcatalogo)
	queryset = catalogo_detalle.objects.filter(catalogo=objcatalogo)
	context = {"catalogo":objcatalogo,"detalle":queryset}
	return render(request,"catalogo/detalle.html",context)

	

"""class CatalogoDetail(AjaxableResponseMixin,ListView):
	model = catalogo_detalle
	template_name = 'catalogo/detalle.html'
	fields = "__all__"
	success_url = reverse_lazy('listar_productos')

	def get_context_data(self,**kwargs):
		context = super(CatalogoDetail, self).get_context_data(**kwargs)
		objcatalogo = catalogo.objects.get(pk=kwargs["pk"])
		context["catalogo"] = objcatalogo
		return context

	def get_queryset(self,**kwargs):
		print "-------------"
		print kwargs
		print "-------------"
		objcatalogo = catalogo.objects.get(pk=kwargs["pkcatalogo"])
		queryset = catalogo_detalle.objects.get(catalogo=objcatalogo)
		return queryset
"""
class CatalogoCreation(AjaxableResponseMixin,CreateView):
	model = catalogo
	template_name = 'catalogo/create.html'
	#form_class = facturaForm
	fields = "__all__"
	success_url = reverse_lazy('listar_productos')

	def get_context_data(self,**kwargs):
		context = super(CatalogoCreation, self).get_context_data(**kwargs)
		context['form_detalle'] = catalogoDetalleForm()
		print context['form_detalle']
		return context

class CatalogoDetaleCreation(AjaxableResponseMixin,CreateView):
	model = catalogo
	#template_name = 'factura/detalle_crear.html'
	#form_class = facturaForm
	fields = "__all__"
	success_url = reverse_lazy('listar_productos')

	deta = form.instance
		#tipo_movimiento = 1 # Entrada

		calculo_cantidad(deta.producto.pk,deta.cantidad)

		deta.inventario.valor_total += (deta.cantidad*deta.costo)
		deta.inventario.save()

		return super(CatalogoDetaleCreation, self).form_valid(form)



class BorrarCatalogo(AjaxableResponseMixin, CreateView):
	"""docstring for BorrarCatalogo"""
	model = catalogo
	template_name = 'catalogo/borrar.html'
	fields = "__all__"
	success_url = reverse_lazy('listar_catalogo')

		
def calculo_cantidad(pk_producto,cantidad):
	objproducto = producto.objects.get(pk=pk_producto)
		objproducto.cantidad += cantidad
	