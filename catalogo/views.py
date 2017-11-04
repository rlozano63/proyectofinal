from django.shortcuts import render

from base.views import AjaxableResponseMixin

from catalogo.forms import *
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


from django.core.urlresolvers import reverse_lazy



# Create your views here.

class CatalogoList(LoginRequiredMixin,AjaxableResponseMixin,ListView):
	model = catalogo
	template_name = 'catalogo/listar.html'
	fields = "__all__"
	success_url = reverse_lazy('listar_productos')

	def get_context_data(self,**kwargs):
		context = super(CatalogoList, self).get_context_data(**kwargs)
		return context

@login_required
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
		objcatalogo = catalogo.objects.get(pk=kwargs["pkcatalogo"])
		queryset = catalogo_detalle.objects.get(catalogo=objcatalogo)
		return queryset
"""
class CatalogoCreation(LoginRequiredMixin,AjaxableResponseMixin,CreateView):
	model = catalogo
	template_name = 'catalogo/create.html'
	#form_class = facturaForm
	fields = "__all__"
	success_url = reverse_lazy('listar_productos')

	def get_context_data(self,**kwargs):
		context = super(CatalogoCreation, self).get_context_data(**kwargs)
		context['form_detalle'] = catalogoDetalleForm()
		context['url'] = "/catalogo/crear/"
		context['url_detalle'] = "/catalogo/detalle/crear/"
		return context

class CatalogoUpdate(LoginRequiredMixin,AjaxableResponseMixin,UpdateView):
	model = catalogo
	template_name = 'catalogo/create.html'
	#form_class = facturaForm
	fields = "__all__"
	success_url = reverse_lazy('listar_productos')

	def get_context_data(self,**kwargs):
		context = super(CatalogoUpdate, self).get_context_data(**kwargs)
		context['form_detalle'] = catalogoDetalleForm()
		context['url'] = "/catalogo/editar/" + self.kwargs["pk"]
		context['url_detalle'] = "/catalogo/detalle/editar/" + self.kwargs["pk"]
		return context

class CatalogoDetaleCreation(LoginRequiredMixin,AjaxableResponseMixin,CreateView):
	model = catalogo_detalle
	#template_name = 'factura/detalle_crear.html'
	#form_class = facturaForm
	fields = "__all__"
	success_url = reverse_lazy('listar_productos')

class CatalogoDetaleUpdate(LoginRequiredMixin,AjaxableResponseMixin,UpdateView):
	model = catalogo_detalle
	#template_name = 'factura/detalle_crear.html'
	#form_class = facturaForm
	fields = "__all__"
	success_url = reverse_lazy('listar_productos')

class BorrarCatalogo(LoginRequiredMixin,AjaxableResponseMixin, CreateView):
	"""docstring for BorrarCatalogo"""
	model = catalogo
	template_name = 'catalogo/borrar.html'
	fields = "__all__"
	success_url = reverse_lazy('listar_catalogo')
	