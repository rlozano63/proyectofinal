from django.shortcuts import render

from base.views import AjaxableResponseMixin
from base.models import distribuidor

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



from django.db.models import Sum

def reportes(request):
	distribuidores = distribuidor.objects.all()
	return render(request,"reportes/index.html",{"distribuidores":distribuidores})

def ReporteVentasDistribuidor(request,id_distribuidor):
	pass

def ReporteVentasTotal(request):
	fini = request.POST.get("fini")
	ffin = request.POST.get("ffin")
	distribuidor_id = request.POST.get("distribuidor")
	facturas = factura.objects.filter(fecha_creacion__date__gte=fini,fecha_creacion__date__lte=ffin)
	vttotal = factura.objects.filter(fecha_creacion__date__gte=fini,fecha_creacion__date__lte=ffin).aggregate(Sum("valor_total"))["valor_total__sum"]
	print vttotal
	for fac in facturas:
		fac.detalle = factura_detalle.objects.filter(factura = fac)


	context = {"facturas":facturas,"vttotal":vttotal}
	return render(request,"reportes/ventasTotal.html",context)
	