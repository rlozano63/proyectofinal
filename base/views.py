from django.shortcuts import render

from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView

from django.core.urlresolvers import reverse_lazy

from base.models import producto, distribuidor, cliente
from base.forms import ProductoForm, DistribuidorForm, ClienteForm
from django.core import serializers
from django.http import JsonResponse



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
				'object': serializers.serialize("json", [self.object],use_natural_foreign_keys=True, use_natural_primary_keys=True)
			}
			return JsonResponse(data)
		else:
			return response

def Dashboard(request):
	context = {}
	return render(request, 'dashboard.html', context)


class BorrarProducto(DeleteView):
	model = producto
	success_url = reverse_lazy('listar_productos')
	template_name = 'productos/borrar.html'

class ActualizarProducto(UpdateView):
	model = producto
	fields = '__all__'
	template_name = 'productos/actualizar.html'
	success_url = reverse_lazy('listar_productos')

class ListarProductos(ListView):

	model = producto
	template_name = 'productos/listar.html'


class ProductoCreation(CreateView):
    model = producto
    template_name = 'productos/create.html'
    fields = '__all__'
    #form_class = ProductoForm
    success_url = reverse_lazy('listar_productos')



class ClienteCreation(CreateView):
	model = cliente
	template_name = 'clientes/create.html'
	fields = '__all__'
	success_url = reverse_lazy('listar_clientes')

class BorrarCliente(DeleteView):
	model = cliente
	success_url = reverse_lazy('listar_clientes')
	template_name = 'clientes/borrar.html'

class ActualizarCliente(UpdateView):
	model = cliente
	fields = '__all__'
	template_name = 'clientes/actualizar.html'
	success_url = reverse_lazy('listar_clientes')

class ListarCliente(ListView):

	model = cliente
	template_name = 'clientes/listar.html'


class DistribuidorCreation(CreateView):
	model = distribuidor
	template_name = 'distribuidores/create.html'
	fields = '__all__'
	success_url = reverse_lazy('listar_distribuidores')

class BorrarDistribuidor(DeleteView):
	model = distribuidor
	success_url = reverse_lazy('listar_distribuidores')
	template_name = 'distribuidores/borrar.html'

class ActualizarDistribuidor(UpdateView):
	model = distribuidor
	fields = '__all__'
	template_name = 'distribuidores/actualizar.html'
	success_url = reverse_lazy('listar_distribuidores')

class ListarDistribuidor(ListView):

	model = distribuidor
	template_name = 'distribuidores/listar.html'
