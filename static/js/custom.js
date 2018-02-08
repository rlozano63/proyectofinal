axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

axios.defaults.headers.common['X-CSRFToken'] = $("[name=csrfmiddlewaretoken]").val();
axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
// axios.defaults.headers.common['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8';

var AppVue = new Vue({
    el: "#vue-root",
    delimiters: ["[[","]]"],
    data:{
        facturacion: {
            forms: {
                create: {
                    fecha_creacion: moment().format("Y-M-D"),
                    factualizacion: moment().format("Y-M-D"),
                    valor_total: 0,
                    cliente: null,
                    deta:{
                        producto: null,
                        cantidad: 1,
                        valor: null,
                        valor_total: null,
                    },
                    productos: [],
                }
            }
        },
        movimientos:{
            forms:{
                create:{
                    fecha_creacion: moment().format("Y-M-D"),
                    proveedor: null,
                    tipo: null,
                    factualizacion: moment().format("Y-M-D"),
                    valor_total: 0,
                    deta:{
                        producto: null,
                        cantidad: null,
                        valor: null,
                        valor_total: null,
                    },
                    productos: []
                }
            }
        },
        inventarios:{
            forms:{
                create:{
                    fecha_creacion: moment().format("Y-M-D"),
                    factualizacion: moment().format("Y-M-D"),
                    valor_total: 0,
                    deta:{
                        producto: null,
                        cantidad: null,
                        valor: null,
                        valor_total: null,
                    },
                    productos: []
                }
            }
        },
        
    },
    methods:{

        facFormCreateReset(){
            this.facturacion = {
                forms: {
                    create: {
                        fecha_creacion: moment().format("Y-M-D"),
                        factualizacion: moment().format("Y-M-D"),
                        valor_total: 0,
                        cliente: null,
                        deta:{
                            producto: null,
                            cantidad: 1,
                            valor: null,
                            valor_total: null,
                        },
                        productos: [],
                    }
                }
            };
        },
        movFormCreateReset() {
            this.movimientos =  {
                forms: {
                    create: {
                        fecha_creacion: moment().format("Y-M-D"),
                        proveedor: null,
                        tipo: null,
                        factualizacion: moment().format("Y-M-D"),
                        valor_total: 0,
                        factura: null,
                        deta:{
                            producto: null,
                            cantidad: null,
                            valor: null,
                            valor_total: null,
                        },
                        productos: []
                    }
                }
            };
        },
        invFormCreateReset() {
            this.inventarios = {
                forms: {
                    create: {
                        fecha_creacion: moment().format("Y-M-D"),
                        factualizacion: moment().format("Y-M-D"),
                        valor_total: 0,
                        deta:{
                            producto: null,
                            cantidad: null,
                            valor: null,
                            valor_total: null,
                        },
                        productos: []
                    }
                }
            };
        },

        getProduct(id){
            return axios.get(`/api/product/${id}`).then(data => data.data)
        },

        /* Facturacion */
        facFormCreateAddDetalle(){
            var form = this.facturacion.forms.create
            var formDeta = this.facturacion.forms.create.deta
            var obj = {
                'producto': formDeta.producto,
                'cantidad': formDeta.cantidad,
                'valor': formDeta.valor,
                'valor_total': formDeta.valor_total,
            }
            var producto_existe = form.productos.some(p => p.producto == obj.producto)
            if ( producto_existe ){
                alert("El producto ya se agrego")
            }else{
                form.productos.push(obj)
            }
        },
        facFormCreateUpdateeVT(productoEdit){
            productoEdit.valor_total = productoEdit.valor * productoEdit.cantidad
        },
        facFormCreateDeleteProducto(productDelete){
            var form = this.facturacion.forms.create
            var index = form.productos.findIndex(item => item.producto = productDelete.producto)
            form.productos.splice(index,1)
        },
        facFormCreateFacturar(){
            var form = this.facturacion.forms.create;
            var data = {
                fecha_creacion: form.fecha_creacion,
                factualizacion: form.factualizacion,
                valor_total: form.valor_total,
                cliente: form.cliente,
            }
            
            axios.post("/factura/crear/", Qs.stringify(data)).then(response => {
                var json = response.data.json
                alert("Factura Creada. \n Ingrese los datos ")
                var productos = form.productos
                productos.forEach(producto => {
                    producto.factura = json.pk
                    axios.post("/factura/detalle/crear/", Qs.stringify(producto)).then(res => {
                        alert("Factura Creada. \n Ingrese los datos ")
                    })
                })


                var formMov = this.movimientos.forms.create;

                formMov.factura = json.pk
                formMov.fecha_creacion = form.fecha_creacion
                formMov.factualizacion = form.factualizacion
                formMov.valor_total = form.valor_total
                // formMov.proveedor
                formMov.tipo = 2
                formMov.productos = form.productos

                this.movFormCreateFacturar();


                this.movFormCreateReset();
                this.facFormCreateReset();
            })
        },

        /* Movimientos */
        movFormCreateAddDetalle(){
            var form = this.movimientos.forms.create
            var formDeta = this.movimientos.forms.create.deta
            var obj = {
                'producto': formDeta.producto,
                'cantidad': formDeta.cantidad,
                'valor': formDeta.valor,
                'valor_total': formDeta.valor_total,
            }
            var producto_existe = form.productos.some(p => p.producto == obj.producto)
            if ( producto_existe ){
                alert("El producto ya se agrego")
            }else{
                form.productos.push(obj)
            }
        },
        movFormCreateUpdateeVT(productoEdit){
            productoEdit.valor_total = productoEdit.valor * productoEdit.cantidad
        },
        movFormCreateDeleteProducto(productDelete){
            var form = this.movimientos.forms.create
            var index = form.productos.findIndex(item => item.producto = productDelete.producto)
            form.productos.splice(index,1)
        },
        movFormCreateFacturar(){
            var form = this.movimientos.forms.create;
            var data = {
                fecha_creacion: form.fecha_creacion,
                factualizacion: form.factualizacion,
                valor_total: form.valor_total,
                proveedor: form.proveedor,
                factura: form.factura,
                tipo: form.tipo,
            }
            
            axios.post("/movimiento/crear/", Qs.stringify(data)).then(response => {
                var json = response.data.json
                alert("Movimiento Creada. \n Ingrese los datos ")
                var productos = form.productos
                productos.forEach(producto => {
                    producto.movimiento = json.pk
                    axios.post("/movimiento/detalle/crear/", Qs.stringify(producto)).then(res => {
                        alert("Movimiento Creada. \n Ingrese los datos ")
                    })
                })
                this.movFormCreateReset();
                
            })
        },

        /* Inventarios */
        invFormCreateAddDetalle() {
            var form = this.inventarios.forms.create
            var formDeta = this.inventarios.forms.create.deta
            var obj = {
                'producto': formDeta.producto,
                'cantidad': formDeta.cantidad,
                'costo': formDeta.costo,
                'valor_total': formDeta.valor_total,
            }
            var producto_existe = form.productos.some(p => p.producto == obj.producto)
            if (producto_existe) {
                alert("El producto ya se agrego")
            } else {
                form.productos.push(obj)
            }
        },
        invFormCreateUpdateeVT(productoEdit) {
            productoEdit.valor_total = productoEdit.costo * productoEdit.cantidad
        },
        invFormCreateDeleteProducto(productDelete) {
            var form = this.inventarios.forms.create
            var index = form.productos.findIndex(item => item.producto = productDelete.producto)
            form.productos.splice(index, 1)
        },
        invFormCreateFacturar() {
            var form = this.inventarios.forms.create;
            var data = {
                fecha_creacion: form.fecha_creacion,
                factualizacion: form.factualizacion,
                valor_total: form.valor_total,
            }

            axios.post("/inventario/crear/", Qs.stringify(data)).then(response => {
                var json = response.data.json
                alert("inventario Creada. \n Ingrese los datos ")
                var productos = form.productos
                productos.forEach(producto => {
                    producto.inventario = json.pk
                    axios.post("/inventario/detalle/crear/", Qs.stringify(producto)).then(res => {
                        alert("inventario Creada. \n Ingrese los datos ")
                    })
                })
                this.invFormCreateReset();
                
            })
        }
    },
    watch:{
        /* Facturacion */
        'facturacion.forms.create.productos': {
            handler: function (newValue) {
                var form = this.facturacion.forms.create
                form.valor_total = form.productos.reduce((n, obj)=> n + obj.valor_total,0)
            },
            deep: true
        },
        'facturacion.forms.create.deta.cantidad': function(){
            var form = this.facturacion.forms.create.deta
            form.valor_total = form.valor * form.cantidad

            if ( form.producto == null ) return 

            this.getProduct(form.producto).then(producto => {
                var cantidad = this.facturacion.forms.create.deta.cantidad
                if (cantidad > producto.fields.cantidad) {
                    alert(`Cantidad inexistente, la cantidad de este producto es ${producto.fields.cantidad}`)
                    producto.fields.cantidad = 0
                }
            })
        },
        'facturacion.forms.create.deta.valor': function(){
            var form = this.facturacion.forms.create.deta
            form.valor_total = form.valor * form.cantidad
        },

        /* Movimientos */
        'movimientos.forms.create.productos': {
            handler: function (newValue) {
                var form = this.movimientos.forms.create
                form.valor_total = form.productos.reduce((n, obj) => n + obj.valor_total, 0)
            },
            deep: true
        },
        'facturacion.forms.create.deta.producto': function (newValue) {
                this.getProduct(newValue).then(producto => {
                    console.log(producto)
                    var form = this.facturacion.forms.create.deta
                    form.valor = producto.fields.precio
                })
        },
        'movimientos.forms.create.deta.cantidad': function () {
            var form = this.movimientos.forms.create
            var formDeta = this.movimientos.forms.create.deta
            formDeta.valor_total = formDeta.valor * formDeta.cantidad

            if (formDeta.producto == null) return

            if (form.tipo == 2 ){
                this.getProduct(formDeta.producto).then(producto => {
                    var cantidad = this.movimientos.forms.create.deta.cantidad
                    if (cantidad > producto.fields.cantidad) {
                        alert(`Cantidad inexistente, la cantidad de este producto es ${producto.fields.cantidad}`)
                        producto.fields.cantidad = 0
                    }
                })
            }

        },
        'movimientos.forms.create.deta.valor': function () {
            var form = this.movimientos.forms.create.deta
            form.valor_total = form.valor * form.cantidad
        },

        /* Innentarios */
        'inventarios.forms.create.productos': {
            handler: function (newValue) {
                var form = this.inventarios.forms.create
                form.valor_total = form.productos.reduce((n, obj) => n + obj.valor_total, 0)
            },
            deep: true
        },
        'inventarios.forms.create.deta.cantidad': function () {
            var form = this.inventarios.forms.create
            var formDeta = this.inventarios.forms.create.deta
            formDeta.valor_total = formDeta.costo * formDeta.cantidad

            if (formDeta.producto == null) return

        },
        'inventarios.forms.create.deta.costo': function () {
            var form = this.inventarios.forms.create.deta
            form.valor_total = form.costo * form.cantidad
        },
    }
})