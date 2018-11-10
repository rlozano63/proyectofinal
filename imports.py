from base.models import producto,distribuidor,cliente, proveedor, unidades, bodegas
from facturacion.models import factura, factura_detalle
from django.contrib.auth.models import User

import datetime

from faker import Faker
fake = Faker()

User.objects.all().delete()
bodegas.objects.all().delete()
factura.objects.all().delete()
factura_detalle.objects.all().delete()
cliente.objects.all().delete()
unidades.objects.all().delete()
producto.objects.all().delete()
proveedor.objects.all().delete()
distribuidor.objects.all().delete()

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
	fecha=datetime.datetime(2017, 5, 10),
	unida=u1,
	stock_minimo="50",
	stock_maximo="200",
)

p2 = producto.objects.create(
	nombre="leche",
	cantidad="100",
	precio="12000",
	fecha=datetime.datetime(2017, 5, 10),
	unida=u1,
	stock_minimo="50",
	stock_maximo="200",
)

p3 = producto.objects.create(
	nombre="leche de fresa",
	cantidad="100",
	precio="12000",
	fecha=datetime.datetime(2017, 5, 10),
	unida=u1,
	stock_minimo="50",
	stock_maximo="200",
)

p4 = producto.objects.create(
	nombre="queso",
	cantidad="100",
	precio="12000",
	fecha=datetime.datetime(2017, 5, 10),
	unida=u1,
	stock_minimo="50",
	stock_maximo="200",
)

producto.objects.create(
	nombre="juego",
	cantidad="100",
	precio="12000",
	fecha=datetime.datetime(2017, 5, 10),
	unida=u1,
	stock_minimo="50",
	stock_maximo="200",
)
producto.objects.create(
	nombre="fresas",
	cantidad="100",
	precio="12000",
	fecha=datetime.datetime(2017, 5, 10),
	unida=u1,
	stock_minimo="50",
	stock_maximo="200",
)

producto.objects.create(
	nombre="manzanas",
	cantidad="100",
	precio="12000",
	fecha=datetime.datetime(2017, 5, 10),
	unida=u1,
	stock_minimo="50",
	stock_maximo="200",
)
producto.objects.create(
	nombre="peras",
	cantidad="100",
	precio="12000",
	fecha=datetime.datetime(2017, 5, 10),
	unida=u1,
	stock_minimo="50",
	stock_maximo="200",
)
producto.objects.create(
	nombre="uvas",
	cantidad="100",
	precio="12000",
	fecha=datetime.datetime(2017, 5, 10),
	unida=u1,
	stock_minimo="50",
	stock_maximo="200",
)
producto.objects.create(
	nombre="mandarinas",
	cantidad="100",
	precio="12000",
	fecha=datetime.datetime(2017, 5, 10),
	unida=u1,
	stock_minimo="50",
	stock_maximo="200",
)
producto.objects.create(
	nombre="melocoton",
	cantidad="100",
	precio="12000",
	fecha=datetime.datetime(2017, 5, 10),
	unida=u1,
	stock_minimo="50",
	stock_maximo="200",
)
producto.objects.create(
	nombre="toronja",
	cantidad="100",
	precio="12000",
	fecha=datetime.datetime(2017, 5, 10),
	unida=u1,
	stock_minimo="50",
	stock_maximo="200",
)
producto.objects.create(
	nombre="papas",
	cantidad="100",
	precio="12000",
	fecha=datetime.datetime(2017, 5, 10),
	unida=u1,
	stock_minimo="50",
	stock_maximo="200",
)
producto.objects.create(
	nombre="yuca",
	cantidad="100",
	precio="12000",
	fecha=datetime.datetime(2017, 5, 10),
	unida=u1,
	stock_minimo="50",
	stock_maximo="200",
)
c1 =cliente.objects.create(

	nombre=fake.name(),
	apellido="",
	nombre_tienda=fake.company(),
	regimen ="comun",
	telefono=fake.phone_number(),
	orden_ruta="1",
	pos_x ="4.303876",
	pos_y="-74.805881",
	ruta_activa="1",

)
c2 =cliente.objects.create(

	nombre=fake.name(),
	apellido="",
	nombre_tienda=fake.company(),
	regimen ="comun",
	telefono=fake.phone_number(),
	orden_ruta="2",
	pos_x ="4.303480",
	pos_y="-74.810741",
	ruta_activa="1",

)

c3 =cliente.objects.create(

	nombre=fake.name(),
	apellido="",
	nombre_tienda=fake.company(),
	regimen ="comun",
	telefono=fake.phone_number(),
	orden_ruta="3",
	pos_x ="4.306026",
	pos_y="-74.803811",
	ruta_activa="1",

)
c4 =cliente.objects.create(

	nombre=fake.name(),
	apellido="",
	nombre_tienda=fake.company(),
	regimen ="comun",
	telefono=fake.phone_number(),
	orden_ruta="4",
	pos_x ="4.301576 ",
	pos_y="-74.811879",
	ruta_activa="1",

)
c5 =cliente.objects.create(

	nombre=fake.name(),
	apellido="",
	nombre_tienda=fake.company(),
	regimen ="comun",
	telefono=fake.phone_number(),
	orden_ruta="5",
	pos_x ="4.300098",
	pos_y="-74.801661",
	ruta_activa="1",

)

proveedor.objects.create(
	nombre=fake.name(),
	apellido="",
	cedula="103212312",
	empresa="ARBOLEDA",
	direccion="Dir",
	telefono="000",
)

distribuidor.objects.create(
	nombre=fake.name(),
	apellido="",
	cedula="1231231212",
	usuario=d1,
	direccion="Dir",
	telefono="000",
)
f1 = factura.objects.create(

	fecha_creacion=datetime.datetime(2017, 5, 10),
	factualizacion=datetime.datetime(2017, 5, 10),
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

	fecha_creacion=datetime.datetime(2017, 5, 14),
	factualizacion=datetime.datetime(2017, 5, 14),
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

	fecha_creacion=datetime.datetime(2017, 5, 9),
	factualizacion=datetime.datetime(2017, 5, 9),
	valor_total="24000",
	cliente=c1,

)
factura_detalle.objects.create(

	factura=f3,
	producto=p2,
	cantidad="2",
	valor="24000",
	valor_total="24000",

)

f4 = factura.objects.create(

	fecha_creacion=datetime.datetime(2017, 5, 13),
	factualizacion=datetime.datetime(2017, 5, 13),
	valor_total="24000",
	cliente=c1,

)
factura_detalle.objects.create(

	factura=f4,
	producto=p2,
	cantidad="1",
	valor="13000",
	valor_total="13000",

)

f5 = factura.objects.create(

	fecha_creacion=datetime.datetime(2017, 5, 11),
	factualizacion=datetime.datetime(2017, 5, 11),
	valor_total="26000",
	cliente=c1,

)
factura_detalle.objects.create(

	factura=f5,
	producto=p3,
	cantidad="2",
	valor="26000",
	valor_total="26000",

)

f6 = factura.objects.create(

	fecha_creacion=datetime.datetime(2017, 5, 10),
	factualizacion=datetime.datetime(2017, 5, 10),
	valor_total="500000",
	cliente=c2,

)
factura_detalle.objects.create(

	factura=f6,
	producto=p3,
	cantidad="1",
	valor="12000",
	valor_total="12000",

)
f7 = factura.objects.create(

	fecha_creacion=datetime.datetime(2017, 5, 14),
	factualizacion=datetime.datetime(2017, 5, 14),
	valor_total="12000",
	cliente=c2,

)
factura_detalle.objects.create(

	factura=f7,
	producto=p4,
	cantidad="1",
	valor="12000",
	valor_total="12000",

)
f8 = factura.objects.create(

	fecha_creacion=datetime.datetime(2017, 5, 9),
	factualizacion=datetime.datetime(2017, 5, 9),
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

	fecha_creacion=datetime.datetime(2017, 5, 13),
	factualizacion=datetime.datetime(2017, 5, 13),
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

	fecha_creacion=datetime.datetime(2017, 5, 11),
	factualizacion=datetime.datetime(2017, 5, 11),
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

	fecha_creacion=datetime.datetime(2017, 5, 10),
	factualizacion=datetime.datetime(2017, 5, 10),
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

	fecha_creacion=datetime.datetime(2017, 5, 14),
	factualizacion=datetime.datetime(2017, 5, 14),
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

	fecha_creacion=datetime.datetime(2017, 5, 9),
	factualizacion=datetime.datetime(2017, 5, 9),
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

	fecha_creacion=datetime.datetime(2017, 5, 13),
	factualizacion=datetime.datetime(2017, 5, 13),
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

	fecha_creacion=datetime.datetime(2017, 5, 11),
	factualizacion=datetime.datetime(2017, 5, 11),
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

	fecha_creacion=datetime.datetime(2017, 5, 10),
	factualizacion=datetime.datetime(2017, 5, 10),
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

	fecha_creacion=datetime.datetime(2017, 5, 14),
	factualizacion=datetime.datetime(2017, 5, 14),
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

	fecha_creacion=datetime.datetime(2017, 5, 9),
	factualizacion=datetime.datetime(2017, 5, 9),
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

	fecha_creacion=datetime.datetime(2017, 5, 13),
	factualizacion=datetime.datetime(2017, 5, 13),
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

	fecha_creacion=datetime.datetime(2017, 5, 11),
	factualizacion=datetime.datetime(2017, 5, 11),
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

	fecha_creacion=datetime.datetime(2017, 5, 10),
	factualizacion=datetime.datetime(2017, 5, 10),
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

	fecha_creacion=datetime.datetime(2017, 5, 14),
	factualizacion=datetime.datetime(2017, 5, 14),
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

	fecha_creacion=datetime.datetime(2017, 5, 9),
	factualizacion=datetime.datetime(2017, 5, 9),
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

	fecha_creacion=datetime.datetime(2017, 5, 13),
	factualizacion=datetime.datetime(2017, 5, 13),
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

	fecha_creacion=datetime.datetime(2017, 5, 11),
	factualizacion=datetime.datetime(2017, 5, 11),
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

bodega =bodegas.objects.create(
	nombre="Bodega",
	telefono=fake.phone_number(),
	direccion=fake.address(),
	pos_x ="4.303480",
	pos_y="-74.810741",
)
