from django.conf.urls import url
from inventario.views import *

urlpatterns = [
	url(r'^inventario/crear/$', InventarioCreation.as_view(), name="inventario"),
	url(r'^inventario/detalle/crear/$', InventarioDetaleCreation.as_view(), name="inventario_detalle"),
]
