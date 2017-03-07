from django.conf.urls import url
from catalogo.views import *

urlpatterns = [
	url(r'^catalogo/crear/$', CatalogoCreation.as_view(), name="catalogo"),
	url(r'^catalogo/detalle/crear/$', CatalogoDetaleCreation.as_view(), name="catalogo_detalle"),
]
