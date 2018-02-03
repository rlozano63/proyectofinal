from django.db.models import Sum
from django.core import serializers
from django.shortcuts import render

from base.views import AjaxableResponseMixin
from base.models import distribuidor, cliente, producto

from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
import json

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
from django.db.models import Sum
from django.db.models.functions import TruncMonth


@login_required

def reportes(request):
	clientes = cliente.objects.all()
	return render(request,"reportes/index.html",{"clientes":clientes})
@login_required

def ReporteVentasDistribuidor(request,id_distribuidor):
	pass
@login_required

def ReporteVentasTotal(request):
	fini = request.GET.get("fini")
	ffin = request.GET.get("ffin")

	cliente_id = request.GET.get("cliente")
	clienteobj = None
	if ( cliente_id == None or cliente_id == '' ):
		facturas = factura.objects.filter(fecha_creacion__date__gte=fini,fecha_creacion__date__lte=ffin)
		vttotal = factura.objects.filter(fecha_creacion__date__gte=fini,fecha_creacion__date__lte=ffin).aggregate(Sum("valor_total"))["valor_total__sum"]
	else:
		clienteobj = cliente.objects.filter(id=cliente_id).get
		facturas = factura.objects.filter(fecha_creacion__date__gte=fini,fecha_creacion__date__lte=ffin,cliente__id=cliente_id)
		vttotal = factura.objects.filter(fecha_creacion__date__gte=fini,fecha_creacion__date__lte=ffin,cliente__id=cliente_id).aggregate(Sum("valor_total"))["valor_total__sum"]

	for fac in facturas:
		fac.detalle = factura_detalle.objects.filter(factura = fac)


	context = {
		"facturas":facturas,
		"vttotal":vttotal,
		"config":{
			"cliente": clienteobj,
			"fini": fini,
			"ffin": ffin,
		}
	}
	return render(request,"reportes/ventasTotal.html",context)

def ReporteMasVendidos(request):
	fini = request.GET.get("fini")
	ffin = request.GET.get("ffin")

	cliente_id = request.GET.get("cliente")
	clienteobj = None
	productos = producto.objects.all()

	data = []
	for pro in productos:
		if ( cliente_id == None or cliente_id == '' ):

			pro.detalles = factura_detalle.objects.filter(producto = pro)
		else:
			clienteobj = cliente.objects.filter(id=cliente_id).get
			pro.detalles = factura_detalle.objects.filter(producto = pro,factura__cliente__id=cliente_id)

		pro.cantidad = len(pro.detalles)
		data.append([pro.nombre,pro.cantidad])

	context = {
		"productos":productos,
		"json":json.dumps(data),
		"config":{
			"cliente": clienteobj,
			"fini": fini,
			"ffin": ffin,
		}
	}
	return render(request,"reportes/masVendidos.html",context)


