from django.conf.urls import url
from facturacion.views import *

urlpatterns = [
	url(r'^factura/crear/$', FacturaCreation.as_view(), name="factura"),
	url(r'^factura/detalle/crear/$', FacturaDetaleCreation.as_view(), name="factura_detalle"),
]
