from django.conf.urls import url
from inventario.views import *

urlpatterns = [
	url(r'^inventario/crear/$', InventarioCreation.as_view(), name="inventario_crear"),
	url(r'^inventario/$', InventarioList.as_view(), name="inventario"),
	url(r'^inventario/(?P<pkinventario>\d+)$', InventarioDetail, name="ver_inventario_detalle"),
	url(r'^inventario/detalle/crear/$', InventarioDetaleCreation.as_view(), name="inventario_detalle"),
	url(r'^movimiento/crear/$', MovimientoCreation.as_view(), name="movimiento"),
	url(r'^movimiento/detalle/crear/$', MovimientoDetaleCreation.as_view(), name="movimiento_detalle"),
]
