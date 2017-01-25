from django.shortcuts import render

from django.views.generic.edit import CreateView

from django.core.urlresolvers import reverse_lazy

from base.models import producto
from base.forms import ProductoForm

class ProductoCreation(CreateView):
    model = producto
    template_name = 'productos/create.html'
    fields = '__all__'
    #form_class = ProductoForm
    #success_url = reverse_lazy('')

