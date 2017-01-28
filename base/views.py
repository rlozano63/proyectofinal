from django.shortcuts import render

from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView

from django.core.urlresolvers import reverse_lazy

from base.models import producto, distribuidor, cliente
from base.forms import ProductoForm, DistribuidorForm, ClienteForm




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

class BorrarCliente(DeleteView):
	model = cliente
	success_url = reverse_lazy('listar_productos')
	template_name = 'clientes/borrar.html'

class ActualizarCliente(UpdateView):
	model = cliente
	fields = '__all__'
	template_name = 'clientes/actualizar.html'

class ListarCliente(ListView):

	model = cliente
	template_name = 'clientes/listar.html'


class DistribuidorCreation(CreateView):
	model = distribuidor
	template_name = 'distribuidores/create.html'
	fields = '__all__'