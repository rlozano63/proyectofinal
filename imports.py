from base.models import producto,distribuidor,cliente, proveedor, unidades
from facturacion.models import factura, factura_detalle
from django.contrib.auth.models import User

User.objects.all().delete()
unidades.objects.all().delete()
producto.objects.all().delete()
cliente.objects.all().delete()
proveedor.objects.all().delete()
distribuidor.objects.all().delete()
factura.objects.all().delete()
factura_detalle.objects.all().delete()

d1=User.objects.create_user('root', password='forsales')
d1.is_superuser=True
d1.is_staff=True
d1.save()

d1=User.objects.create_user('foo', password='bar')
d1.is_superuser=False
d1.is_staff=False
d1.save()

u1 = unidades.objects.create(
	nombre="litros",
)

p1 = producto.objects.create(
	nombre="leche deslactosada",
	cantidad="100",
	precio="12000",
	fecha="2017-05-10",
	unida=u1,
	stock_minimo="50",
	stock_maximo="200",
)

c1 =cliente.objects.create(

	nombre="carlos",
	apellido="lunar",
	nombre_tienda="Don lunar",
	regimen ="comun",
	telefono="3122323123", 
	orden_ruta="1",
	pos_x ="4.303876",
	pos_y="-74.805881",
	ruta_activa="1",

)
c2 =cliente.objects.create(

	nombre="michael",
	apellido="sol",
	nombre_tienda="Don myky",
	regimen ="comun",
	telefono="3122323", 
	orden_ruta="2",
	pos_x ="4.303480",
	pos_y="-74.810741",
	ruta_activa="1",

)
c3 =cliente.objects.create(

	nombre="sol",
	apellido="luz",
	nombre_tienda="Don soluz",
	regimen ="comun",
	telefono="312232113", 
	orden_ruta="3",
	pos_x ="4.306026",
	pos_y="-74.803811",
	ruta_activa="1",

)
c4 =cliente.objects.create(

	nombre="solilo",
	apellido="pillo",
	nombre_tienda="pillos",
	regimen ="comun",
	telefono="31223212", 
	orden_ruta="4",
	pos_x ="4.301576 ",
	pos_y="-74.811879",
	ruta_activa="1",

)
c5 =cliente.objects.create(

	nombre="musga",
	apellido="suoll",
	nombre_tienda="musgos",
	regimen ="comun",
	telefono="312232113", 
	orden_ruta="5",
	pos_x ="4.300098",
	pos_y="-74.801661",
	ruta_activa="1",

)

proveedor.objects.create(

	nombre="jose", 
	apellido="manuel",
	cedula="103212312",
	empresa="ARBOLEDA",
)

distribuidor.objects.create(

	nombre="jorge",
	apellido="bermudez",
	cedula="1231231212",
	usuario=d1,
	

)
f1 = factura.objects.create(

	fecha_creacion="2017-05-10 00:00:00",
	factualizacion="2017-05-10 00:00:00",
	valor_total="500000",
	cliente=c1,

)
factura_detalle.objects.create(

	factura=f1, 
	producto=p1,
	cantidad="1", 
	valor="12000",
	valor_total="12000",

)
f2 = factura.objects.create(

	fecha_creacion="2017-05-14 00:00:00",
	factualizacion="2017-05-14 00:00:00",
	valor_total="12000",
	cliente=c1,

)
factura_detalle.objects.create(

	factura=f2, 
	producto=p1,
	cantidad="1", 
	valor="12000",
	valor_total="12000",

)
f3 = factura.objects.create(

	fecha_creacion="2017-05-09 00:00:00",
	factualizacion="2017-05-09 00:00:00",
	valor_total="24000",
	cliente=c1,

)
factura_detalle.objects.create(

	factura=f3, 
	producto=p1,
	cantidad="2", 
	valor="24000",
	valor_total="24000",

)

f4 = factura.objects.create(

	fecha_creacion="2017-05-13 00:00:00",
	factualizacion="2017-05-13 00:00:00",
	valor_total="24000",
	cliente=c1,

)
factura_detalle.objects.create(

	factura=f4, 
	producto=p1,
	cantidad="1", 
	valor="13000",
	valor_total="13000",

)

f5 = factura.objects.create(

	fecha_creacion="2017-05-11 00:00:00",
	factualizacion="2017-05-11 00:00:00",
	valor_total="26000",
	cliente=c1,

)
factura_detalle.objects.create(

	factura=f5, 
	producto=p1,
	cantidad="2", 
	valor="26000",
	valor_total="26000",

)

f6 = factura.objects.create(

	fecha_creacion="2017-05-10 00:00:00",
	factualizacion="2017-05-10 00:00:00",
	valor_total="500000",
	cliente=c2,

)
factura_detalle.objects.create(

	factura=f6, 
	producto=p1,
	cantidad="1", 
	valor="12000",
	valor_total="12000",

)
f7 = factura.objects.create(

	fecha_creacion="2017-05-14 00:00:00",
	factualizacion="2017-05-14 00:00:00",
	valor_total="12000",
	cliente=c2,

)
factura_detalle.objects.create(

	factura=f7, 
	producto=p1,
	cantidad="1", 
	valor="12000",
	valor_total="12000",

)
f8 = factura.objects.create(

	fecha_creacion="2017-05-09 00:00:00",
	factualizacion="2017-05-09 00:00:00",
	valor_total="24000",
	cliente=c2,

)
factura_detalle.objects.create(

	factura=f8, 
	producto=p1,
	cantidad="2", 
	valor="24000",
	valor_total="24000",

)

f9 = factura.objects.create(

	fecha_creacion="2017-05-13 00:00:00",
	factualizacion="2017-05-13 00:00:00",
	valor_total="24000",
	cliente=c2,

)
factura_detalle.objects.create(

	factura=f9, 
	producto=p1,
	cantidad="1", 
	valor="13000",
	valor_total="13000",

)

f10 = factura.objects.create(

	fecha_creacion="2017-05-11 00:00:00",
	factualizacion="2017-05-11 00:00:00",
	valor_total="26000",
	cliente=c2,

)
factura_detalle.objects.create(

	factura=f10, 
	producto=p1,
	cantidad="2", 
	valor="26000",
	valor_total="26000",

)
f11 = factura.objects.create(

	fecha_creacion="2017-05-10 00:00:00",
	factualizacion="2017-05-10 00:00:00",
	valor_total="500000",
	cliente=c3,

)
factura_detalle.objects.create(

	factura=f11, 
	producto=p1,
	cantidad="1", 
	valor="12000",
	valor_total="12000",

)
f12 = factura.objects.create(

	fecha_creacion="2017-05-14 00:00:00",
	factualizacion="2017-05-14 00:00:00",
	valor_total="12000",
	cliente=c3,

)
factura_detalle.objects.create(

	factura=f12, 
	producto=p1,
	cantidad="1", 
	valor="12000",
	valor_total="12000",

)
f13 = factura.objects.create(

	fecha_creacion="2017-05-09 00:00:00",
	factualizacion="2017-05-09 00:00:00",
	valor_total="24000",
	cliente=c3,

)
factura_detalle.objects.create(

	factura=f13, 
	producto=p1,
	cantidad="2", 
	valor="24000",
	valor_total="24000",

)

f14 = factura.objects.create(

	fecha_creacion="2017-05-13 00:00:00",
	factualizacion="2017-05-13 00:00:00",
	valor_total="24000",
	cliente=c3,

)
factura_detalle.objects.create(

	factura=f14, 
	producto=p1,
	cantidad="1", 
	valor="13000",
	valor_total="13000",

)

f15 = factura.objects.create(

	fecha_creacion="2017-05-11 00:00:00",
	factualizacion="2017-05-11 00:00:00",
	valor_total="26000",
	cliente=c3,

)
factura_detalle.objects.create(

	factura=f15, 
	producto=p1,
	cantidad="2", 
	valor="26000",
	valor_total="26000",

)
f16 = factura.objects.create(

	fecha_creacion="2017-05-10 00:00:00",
	factualizacion="2017-05-10 00:00:00",
	valor_total="500000",
	cliente=c4,

)
factura_detalle.objects.create(

	factura=f16, 
	producto=p1,
	cantidad="1", 
	valor="12000",
	valor_total="12000",

)
f17 = factura.objects.create(

	fecha_creacion="2017-05-14 00:00:00",
	factualizacion="2017-05-14 00:00:00",
	valor_total="12000",
	cliente=c4,

)
factura_detalle.objects.create(

	factura=f17, 
	producto=p1,
	cantidad="1", 
	valor="12000",
	valor_total="12000",

)
f18 = factura.objects.create(

	fecha_creacion="2017-05-09 00:00:00",
	factualizacion="2017-05-09 00:00:00",
	valor_total="24000",
	cliente=c4,

)
factura_detalle.objects.create(

	factura=f18, 
	producto=p1,
	cantidad="2", 
	valor="24000",
	valor_total="24000",

)

f19 = factura.objects.create(

	fecha_creacion="2017-05-13 00:00:00",
	factualizacion="2017-05-13 00:00:00",
	valor_total="24000",
	cliente=c4,

)
factura_detalle.objects.create(

	factura=f19, 
	producto=p1,
	cantidad="1", 
	valor="13000",
	valor_total="13000",

)

f20 = factura.objects.create(

	fecha_creacion="2017-05-11 00:00:00",
	factualizacion="2017-05-11 00:00:00",
	valor_total="26000",
	cliente=c4,

)
factura_detalle.objects.create(

	factura=f20, 
	producto=p1,
	cantidad="2", 
	valor="26000",
	valor_total="26000",

)
f21 = factura.objects.create(

	fecha_creacion="2017-05-10 00:00:00",
	factualizacion="2017-05-10 00:00:00",
	valor_total="500000",
	cliente=c5,

)
factura_detalle.objects.create(

	factura=f21, 
	producto=p1,
	cantidad="1", 
	valor="12000",
	valor_total="12000",

)
f22 = factura.objects.create(

	fecha_creacion="2017-05-14 00:00:00",
	factualizacion="2017-05-14 00:00:00",
	valor_total="12000",
	cliente=c5,

)
factura_detalle.objects.create(

	factura=f22, 
	producto=p1,
	cantidad="1", 
	valor="12000",
	valor_total="12000",

)
f23 = factura.objects.create(

	fecha_creacion="2017-05-09 00:00:00",
	factualizacion="2017-05-09 00:00:00",
	valor_total="24000",
	cliente=c5,

)
factura_detalle.objects.create(

	factura=f23, 
	producto=p1,
	cantidad="2", 
	valor="24000",
	valor_total="24000",

)

f24 = factura.objects.create(

	fecha_creacion="2017-05-13 00:00:00",
	factualizacion="2017-05-13 00:00:00",
	valor_total="24000",
	cliente=c5,

)
factura_detalle.objects.create(

	factura=f24, 
	producto=p1,
	cantidad="1", 
	valor="13000",
	valor_total="13000",

)

f25 = factura.objects.create(

	fecha_creacion="2017-05-11 00:00:00",
	factualizacion="2017-05-11 00:00:00",
	valor_total="26000",
	cliente=c5,

)
factura_detalle.objects.create(

	factura=f25, 
	producto=p1,
	cantidad="2", 
	valor="26000",
	valor_total="26000",

)
