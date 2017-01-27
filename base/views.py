from django.shortcuts import render

from django.views.generic.edit import CreateView

from django.core.urlresolvers import reverse_lazy

from base.models import producto, distribuidor, cliente
from base.forms import ProductoForm, DistribuidorForm, ClienteForm

class ProductoCreation(CreateView):
    model = producto
    template_name = 'productos/create.html'
    fields = '__all__'
    #form_class = ProductoForm
    #success_url = reverse_lazy('')

class DistribuidorCreation(CreateView):
	model = distribuidor
	template_name = 'distribuidores/createDistri.html'
	fields = '__all__'

class ClienteCreation(CreateView):
	model = cliente 
	template_name = 'clientes/createCliente.html'
	fields = '__all__'