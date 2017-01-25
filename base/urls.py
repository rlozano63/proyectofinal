from django.conf.urls import url
from base.views import ProductoCreation

urlpatterns = [
	url(r'^create/', ProductoCreation.as_view(), name="producto_creation"),
]