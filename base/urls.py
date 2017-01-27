from django.conf.urls import url
from base.views import ProductoCreation, DistribuidorCreation, ClienteCreation

urlpatterns = [
	url(r'^create/', ProductoCreation.as_view(), name="producto_creation"),
	url(r'^create/', DistribuidorCreation.as_view(), name="distribuidor_creation"),
	url(r'^create/', ClienteCreation.as_view(), name="cliente_creation")

]