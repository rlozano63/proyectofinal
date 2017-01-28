from django.conf.urls import url
from base.views import *

urlpatterns = [
	url(r'^$', Dashboard, name="dashboard"),

	url(r'^productos/$', ListarProductos.as_view(), name="listar_productos"),
	url(r'^productos/crear/$', ProductoCreation.as_view(), name="crear_producto"),
	url(r'^productos/actualizar/(?P<pk>\d+)$', ActualizarProducto.as_view(), name="actualizar_producto"),
	url(r'^productos/borrar/(?P<pk>\d+)$', BorrarProducto.as_view(), name="borrar_producto"),
	

	url(r'^clientes/$', ListarCliente.as_view(), name="listar_clientes"),
	url(r'^clientes/crear/$', ClienteCreation.as_view(), name="crear_cliente"),
	url(r'^clientes/actualizar/(?P<pk>\d+)$', ActualizarCliente.as_view(), name="actualizar_cliente"),
	url(r'^clientes/borrar/(?P<pk>\d+)$', BorrarCliente.as_view(), name="borrar_cliente"),
	


	url(r'^distribuidores/crear/$', DistribuidorCreation.as_view(), name="crear_distribuidor"),
]
