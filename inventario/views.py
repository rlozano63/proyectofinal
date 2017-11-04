from django.shortcuts import render

from base.views import LoginRequiredMixin,AjaxableResponseMixin

from inventario.forms import *
from base.forms import producto
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def MovimientoHistorial(request,id):
	objproducto = producto.objects.get(id=id)
	movimientosdetalle = movimiento_detalle.objects.filter(producto=objproducto)
	context = {
		'producto': objproducto,
		'movimientosdetalle': movimientosdetalle,
	}
	return render(request, 'movimiento/historial.html', context)

# Create your views here.
class InventarioList(LoginRequiredMixin,AjaxableResponseMixin,ListView):
	model = inventario
	template_name = 'inventario/listar.html'
	fields = "__all__"
	success_url = reverse_lazy('listar_productos')

	def get_context_data(self,**kwargs):
		context = super(InventarioList, self).get_context_data(**kwargs)
		return context
	
@login_required
def InventarioDetail(request, pkinventario):
	objinventario = inventario.objects.get(pk=pkinventario)
	queryset = inventario_detalle.objects.filter(inventario=objinventario)
	context = {"inventario":objinventario,"detalle":queryset}
	return render(request,"inventario/detalle.html",context)



class InventarioCreation(LoginRequiredMixin,AjaxableResponseMixin,CreateView):
	model = inventario
	template_name = 'inventario/crear.html'
	form_class = inventarioForm
	#fields = "__all__"
	success_url = reverse_lazy('listar_productos')

	def get_context_data(self,**kwargs):
		context = super(InventarioCreation, self).get_context_data(**kwargs)
		context['form_detalle'] = inventarioDetalleForm()
		return context

class InventarioDetaleCreation(LoginRequiredMixin,AjaxableResponseMixin,CreateView):
	model = inventario_detalle
	#template_name = 'inventario/detalle_crear.html'
	#form_class = inventarioForm
	fields = "__all__"
	success_url = reverse_lazy('listar_productos')
	def form_valid(self, form):

		deta = form.instance
		tipo_movimiento = 1 # Entrada
		calcular_cantidad(deta.producto.pk,tipo_movimiento,deta.cantidad)

		deta.inventario.valor_total += (deta.cantidad*deta.costo)
		deta.inventario.save()

		return super(InventarioDetaleCreation, self).form_valid(form)

# Create your views here.

class MovimientoCreation(LoginRequiredMixin,AjaxableResponseMixin,CreateView):
	model = movimiento
	template_name = 'movimiento/crear.html'
	form_class = movimientoForm
	# fields = "__all__"
	success_url = reverse_lazy('listar_productos')

	def get_context_data(self,**kwargs):
		context = super(MovimientoCreation, self).get_context_data(**kwargs)
		context['form_detalle'] = movimientoDetalleForm()
		return context

class MovimientoDetaleCreation(LoginRequiredMixin,AjaxableResponseMixin,CreateView):
	model = movimiento_detalle
	#template_name = 'movimiento/detalle_crear.html'
	#form_class = movimientoForm
	fields = "__all__"
	success_url = reverse_lazy('listar_productos')

	def form_valid(self, form):
		deta = form.instance
		calcular_cantidad(deta.producto.pk,deta.movimiento.tipo.pk,deta.cantidad)

		return super(MovimientoDetaleCreation, self).form_valid(form)

def calcular_cantidad(pk_producto,pk_tmovi,cantidad):
	objproducto = producto.objects.get(pk=pk_producto)
	if( pk_tmovi == 1 ):
		objproducto.cantidad += cantidad
	else:
		objproducto.cantidad -= cantidad
	objproducto.save()
