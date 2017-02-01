from django.conf.urls import url
from inventario.views import InventarioCreation

urlpatterns = [
	url(r'^crear/$', InventarioCreation.as_view(), name="inventario"),
]
