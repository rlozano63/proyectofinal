from django.conf.urls import url
from rutas.views import *

urlpatterns = [
	url(r'^rutas/mapa/$', mapa, name="rutas-mapa"),
]
