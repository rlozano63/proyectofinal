from django.conf.urls import url
from catalogo.views import *

urlpatterns = [
	# url(r'^catalogos/$', CatalogoList.as_view(), name="catalogos"),
	url(r'^catalogo/(?P<pkcatalogo>\d+)$', CatalogoDetail, name="ver_catalogo_detalle"),
	url(r'^catalogo/borrar/(?P<pkcatalogo>\d+)$', BorrarCatalogo.as_view(), name="borrar_catalogo"),
	url(r'^catalogo/crear/$', CatalogoCreation.as_view(), name="catalogo"),
	url(r'^catalogo/detalle/crear/$', CatalogoDetaleCreation.as_view(), name="catalogo_detalle"),
	url(r'^catalogo/editar/(?P<pk>\d+)$', CatalogoUpdate.as_view(), name="catalogo_update"),
	url(r'^catalogo/detalle/editar/(?P<pk>\d+)$', CatalogoDetaleUpdate.as_view(), name="catalogo_detalle_update"),
]
