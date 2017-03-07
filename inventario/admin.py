from django.contrib import admin

from inventario.models import *

admin.site.register(inventario)
admin.site.register(inventario_detalle)
admin.site.register(tipo_movimiento)
admin.site.register(movimiento)
admin.site.register(movimiento_detalle)