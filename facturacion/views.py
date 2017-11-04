from django.shortcuts import render

from base.views import AjaxableResponseMixin
from base.models import distribuidor, cliente

from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt

from facturacion.forms import *
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy

from inventario.views import calcular_cantidad

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.

class FacturaList(LoginRequiredMixin,AjaxableResponseMixin,ListView):
	model = factura
	template_name = 'factura/listar.html'
	fields = "__all__"
	success_url = reverse_lazy('listar_factura')

	def get_context_data(self,**kwargs):
		context = super(FacturaList, self).get_context_data(**kwargs)
		return context

@login_required
def FacturaDetail(request, pkfactura):
	objfactura = factura.objects.get(pk=pkfactura)
	queryset = factura_detalle.objects.filter(factura=objfactura)
	context = {"factura":objfactura,"detalle":queryset}
	return render(request,"factura/detalle.html",context)


class FacturaCreation(LoginRequiredMixin,AjaxableResponseMixin,CreateView):
	model = factura
	template_name = 'factura/create.html'
	form_class = facturaForm
	#fields = "__all__"
	success_url = reverse_lazy('listar_productos')

	def get_context_data(self,**kwargs):
		context = super(FacturaCreation, self).get_context_data(**kwargs)
		context['form_detalle'] = facturaDetalleForm()
		return context

	def form_valid(self, form):
		deta = form.instance
		verificacion_ventas_cliente(deta.cliente.id)

		return super(FacturaCreation, self).form_valid(form)

class FacturaDetaleCreation(LoginRequiredMixin,AjaxableResponseMixin,CreateView):
	model = factura_detalle
	#template_name = 'factura/detalle_crear.html'
	#form_class = facturaForm
	fields = "__all__"
	success_url = reverse_lazy('listar_productos')
	def form_valid(self, form):
		tipo_movimiento = 2 # salida
		deta = form.instance
		#calcular_cantidad(deta.producto.pk,tipo_movimiento,deta.cantidad)

		deta.factura.valor_total += (deta.cantidad*deta.valor)
		deta.factura.save()

		return super(FacturaDetaleCreation, self).form_valid(form)



from django.db.models import Sum
from django.core import serializers

def verificacion_ventas_cliente(cliente_id = None):
	compra_minima_cliente = 0
	response = []
	if cliente_id:
		oclientes = [cliente.objects.get(id=cliente_id)]
	else:
		oclientes = cliente.objects.all()

	for ocliente in oclientes:
		total_ventas_cliente = factura.objects.filter(cliente=ocliente).aggregate(Sum("valor_total"))["valor_total__sum"]
		ocliente.ruta_activa = 1
		if total_ventas_cliente < compra_minima_cliente:
			ocliente.ruta_activa = 0
		ocliente.save()
	response = serializers.serialize('json', cliente.objects.all())
	return response

@csrf_exempt
@login_required
def url_verificacion_ventas_cliente(request):
	response = verificacion_ventas_cliente()
	return JsonResponse(response,safe=False)


@login_required

def reportes(request):
	distribuidores = distribuidor.objects.all()
	return render(request,"reportes/index.html",{"distribuidores":distribuidores})
@login_required

def ReporteVentasDistribuidor(request,id_distribuidor):
	pass
@login_required

def ReporteVentasTotal(request):
	fini = request.POST.get("fini")
	ffin = request.POST.get("ffin")
	distribuidor_id = request.POST.get("distribuidor")
	facturas = factura.objects.filter(fecha_creacion__date__gte=fini,fecha_creacion__date__lte=ffin)
	vttotal = factura.objects.filter(fecha_creacion__date__gte=fini,fecha_creacion__date__lte=ffin).aggregate(Sum("valor_total"))["valor_total__sum"]
	for fac in facturas:
		fac.detalle = factura_detalle.objects.filter(factura = fac)


	context = {"facturas":facturas,"vttotal":vttotal}
	return render(request,"reportes/ventasTotal.html",context)
	

