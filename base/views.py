from django.shortcuts import render
import json
import os
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.views.decorators.csrf import csrf_exempt

from django.core.urlresolvers import reverse_lazy

from base.models import producto, distribuidor, cliente, proveedor, bodegas
from catalogo.models import catalogo, catalogo_detalle
from base.forms import ProductoForm, DistribuidorForm, ClienteForm, ProveedorForm
from django.core import serializers
from django.http import JsonResponse

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


@csrf_exempt
@login_required
def GetProduct(request,id):
	p = producto.objects.get(id = id)
	response = serializers.serialize('json', [p])
	response = json.loads(response)[0]
	return JsonResponse(response,safe=False)

class AjaxableResponseMixin(object):
	"""
	Mixin to add AJAX support to a form.
	Must be used with an object-based FormView (e.g. CustomCreateView)
	"""
	def form_invalid(self, form):
		response = super(AjaxableResponseMixin, self).form_invalid(form)
		if self.request.is_ajax():
			data = {
				'error':True,
				'message':'Ocurrio un Error al realizar el Proceso.',
				'errors':form.errors,
			}
			return JsonResponse(data, status=400)
		else:
			return response

	def form_valid(self, form):
		# We make sure to call the parent's form_valid() method because
		# it might do some processing (in the case of CustomCreateView, it will
		# call form.save() for example).
		response = super(AjaxableResponseMixin, self).form_valid(form)
		if self.request.is_ajax():
			message = "OK"
			data = {
				'message':message,
				'object': serializers.serialize("json", [self.object],use_natural_foreign_keys=True, use_natural_primary_keys=True),
				'json': json.loads(serializers.serialize("json", [self.object],use_natural_foreign_keys=True, use_natural_primary_keys=True))[0],
			}
			return JsonResponse(data)
		else:
			return response

@login_required
def Dashboard(request):
	escazes = []
	for objproducto in producto.objects.all():
		if objproducto.cantidad < objproducto.stock_minimo:
			escazes.append(objproducto)

	context = {"escazes":escazes}
	return render(request, 'dashboard.html', context)

@login_required
def getClientesPositions(request):
	clientes = cliente.objects.filter(ruta_activa=1)
	bodega = bodegas.objects.get()
	positions = []
	bodegadata = {
		"name":bodega.nombre,
		"direccion":bodega.direccion,
		"telefono":bodega.telefono,
		"position":{"lat":bodega.pos_x,"lng":bodega.pos_y}
	}
	for ocliente in clientes:
		positions.append({
			"name":"%s %s" % (ocliente.nombre,ocliente.apellido),
			"direccion":ocliente.direccion,
			"telefono":ocliente.telefono,
			"position":{"lat":ocliente.pos_x,"lng":ocliente.pos_y}
			})
	return JsonResponse({
		"positions":positions,
		"bodega":bodegadata,
	})

@csrf_exempt
@login_required
def setStatusRuta(request, pk):
	clienteobj = cliente.objects.filter(id=pk).get()
	if ( clienteobj.ruta_activa == '1' ):
		clienteobj.ruta_activa = 0
	else:
		clienteobj.ruta_activa = 1
	clienteobj.save()
	return JsonResponse(
		json.loads(serializers.serialize("json", [clienteobj],use_natural_foreign_keys=True, use_natural_primary_keys=True))[0]
	)

@csrf_exempt
@login_required
def setOrdenRuta(request, pk, orden):
	clienteobj = cliente.objects.filter(id=pk).get()
	clienteobj.orden_ruta = orden
	clienteobj.save()
	return JsonResponse(
		json.loads(serializers.serialize("json", [clienteobj],use_natural_foreign_keys=True, use_natural_primary_keys=True))[0]
	)

class BorrarProducto(LoginRequiredMixin,DeleteView):
	model = producto
	success_url = reverse_lazy('listar_productos')
	template_name = 'productos/borrar.html'

class ActualizarProducto(LoginRequiredMixin,UpdateView):
	model = producto
	fields = '__all__'
	template_name = 'productos/actualizar.html'
	success_url = reverse_lazy('listar_productos')

class ListarProductos(LoginRequiredMixin,ListView):

	model = producto
	template_name = 'productos/listar.html'

class ProductoCreation(LoginRequiredMixin,CreateView):
    model = producto
    template_name = 'productos/create.html'
    fields = '__all__'
    #form_class = ProductoForm
    success_url = reverse_lazy('listar_productos')

class ClienteCreation(LoginRequiredMixin,CreateView):
	model = cliente
	template_name = 'clientes/create.html'
	fields = '__all__'
	success_url = reverse_lazy('listar_clientes')

class BorrarCliente(LoginRequiredMixin,DeleteView):
	model = cliente
	success_url = reverse_lazy('listar_clientes')
	template_name = 'clientes/borrar.html'

class ActualizarCliente(LoginRequiredMixin,UpdateView):
	model = cliente
	fields = '__all__'
	template_name = 'clientes/actualizar.html'
	success_url = reverse_lazy('listar_clientes')

"""
class ListarCliente(LoginRequiredMixin,ListView):

	model = cliente
	template_name = 'clientes/listar.html'
"""

@login_required
def ListarCliente(request,):
	ruta_limpiada = os.environ.get('CLEAR')
	print(ruta_limpiada)

	clientes = cliente.objects.all()
	return render(request,'clientes/listar.html',{'object_list':clientes})

class DistribuidorCreation(LoginRequiredMixin,CreateView):
	model = distribuidor
	template_name = 'distribuidores/create.html'
	fields = '__all__'
	success_url = reverse_lazy('listar_distribuidores')

class BorrarDistribuidor(LoginRequiredMixin,DeleteView):
	model = distribuidor
	success_url = reverse_lazy('listar_distribuidores')
	template_name = 'distribuidores/borrar.html'

class ActualizarDistribuidor(LoginRequiredMixin,UpdateView):
	model = distribuidor
	fields = '__all__'
	template_name = 'distribuidores/actualizar.html'
	success_url = reverse_lazy('listar_distribuidores')

class ListarDistribuidor(LoginRequiredMixin,ListView):

	model = distribuidor
	template_name = 'distribuidores/listar.html'

class ProveedorCreation(LoginRequiredMixin,CreateView):
	model = proveedor
	template_name = 'proveedores/create.html'
	fields = '__all__'
	success_url = reverse_lazy('listar_proveedores')

class BorrarProveedor(LoginRequiredMixin,DeleteView):
	model = proveedor
	success_url = reverse_lazy('listar_proveedores')
	template_name = 'proveedores/borrar.html'

class ActualizarProveedor(LoginRequiredMixin,UpdateView):
	model = proveedor
	fields = '__all__'
	template_name = 'proveedores/actualizar.html'
	success_url = reverse_lazy('listar_proveedores')

class ListarProveedor(LoginRequiredMixin,ListView):

	model = proveedor
	template_name = 'proveedores/listar.html'

class ListarCatalogoDistribuidor(LoginRequiredMixin,ListView):

	model = catalogo_detalle
	template_name = 'distribuidores/catalogo.html'

	def get_queryset(self):
		dist = distribuidor.objects.get(usuario=self.request.user)
		catalogo_user = catalogo.objects.filter(distribuidor=dist)
		catalogo_det = catalogo_detalle.objects.filter(catalogo=catalogo_user)
		return catalogo_det
