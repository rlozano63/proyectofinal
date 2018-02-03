from django.conf.urls import url
from base.views import *



urlpatterns = [
	url(r'^$', Dashboard, name="dashboard"),

	url(r'^productos/$', ListarProductos.as_view(), name="listar_productos"),
	url(r'^productos/crear/$', ProductoCreation.as_view(), name="crear_producto"),
	url(r'^productos/actualizar/(?P<pk>\d+)$', ActualizarProducto.as_view(), name="actualizar_producto"),
	url(r'^productos/borrar/(?P<pk>\d+)$', BorrarProducto.as_view(), name="borrar_producto"),

	url(r'^api/product/(?P<id>\d+)$', GetProduct, name="get_product"),

	url(r'^clientes/$', ListarCliente, name="listar_clientes"),
	url(r'^clientes/crear/$', ClienteCreation.as_view(), name="crear_cliente"),
	url(r'^clientes/actualizar/(?P<pk>\d+)$', ActualizarCliente.as_view(), name="actualizar_cliente"),
	url(r'^clientes/borrar/(?P<pk>\d+)$', BorrarCliente.as_view(), name="borrar_cliente"),
	url(r'^clientes/positions/$', getClientesPositions, name="get_positions_clientes"),
	url(r'^clientes/(?P<pk>\d+)/ruta/set/status/$', setStatusRuta, name="set_status_ruta_cliente"),
	url(r'^clientes/(?P<pk>\d+)/ruta/set/orden/(?P<orden>\d+)$', setOrdenRuta, name="set_orden_ruta_cliente"),


	url(r'^distribuidores/$', ListarDistribuidor.as_view(), name="listar_distribuidores"),
	url(r'^distribuidores/crear/$', DistribuidorCreation.as_view(), name="crear_distribuidor"),
	url(r'^distribuidores/actualizar/(?P<pk>\d+)$', ActualizarDistribuidor.as_view(), name="actualizar_distribuidor"),
	url(r'^distribuidores/borrar/(?P<pk>\d+)$', BorrarDistribuidor.as_view(), name="borrar_distribuidor"),
	url(r'^distribuidor/catalogo/$', ListarCatalogoDistribuidor.as_view(), name="distribuidor_catalogo"),

	url(r'^proveedores/$', ListarProveedor.as_view(), name="listar_proveedores"),
	url(r'^proveedores/crear/$', ProveedorCreation.as_view(), name="crear_proveedor"),
	url(r'^proveedores/actualizar/(?P<pk>\d+)$', ActualizarProveedor.as_view(), name="actualizar_proveedor"),
	url(r'^proveedores/borrar/(?P<pk>\d+)$', BorrarProveedor.as_view(), name="borrar_proveedor"),

]
