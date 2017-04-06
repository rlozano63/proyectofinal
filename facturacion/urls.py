from django.conf.urls import url
from facturacion.views import *

urlpatterns = [
	url(r'^factura/$', FacturaList.as_view(), name="factura"),
	url(r'^factura/(?P<pkfactura>\d+)$', FacturaDetail, name="ver_factura_detalle"),
	url(r'^factura/crear/$', FacturaCreation.as_view(), name="facturacion"),
	url(r'^factura/detalle/crear/$', FacturaDetaleCreation.as_view(), name="factura_detalle"),
	
	url(r'^factura/reportes$', reportes, name="reportes"),

	url(r'^factura/reportes/ventasDistribuidor$', ReporteVentasDistribuidor, name="ReporteVentasDistribuidor"),
	url(r'^factura/reportes/ventasTotal$', ReporteVentasTotal, name="ReporteVentasTotal"),
	
	
	
]

