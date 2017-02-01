from django.shortcuts import render

from inventario.forms import *
from django.views.generic.edit import CreateView


# Create your views here.

class InventarioCreation(CreateView):
	model = inventario
	template_name = 'inventario/crear.html'
	#form_class = inventarioForm
	fields = "__all__"

	def get_context_data(self,**kwargs):
		context = super(InventarioCreation, self).get_context_data(**kwargs)
		#context['inventario_detalle'] = inventario_detalle()
		return context