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
                        cantidad: null,
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
        }
        
    },
    methods:{
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
            })
        }
    },
    watch:{
        /* Facturacion */
        'facturacion.forms.create.productos': {
            handler: function (newValue) {
                console.log("hola")
                var form = this.facturacion.forms.create
                console.log(form.productos)
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
                console.log("hola")
                var form = this.movimientos.forms.create
                console.log(form.productos)
                form.valor_total = form.productos.reduce((n, obj) => n + obj.valor_total, 0)
            },
            deep: true
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
                    }
                })
            }

        },
        'movimientos.forms.create.deta.valor': function () {
            var form = this.movimientos.forms.create.deta
            form.valor_total = form.valor * form.cantidad
        },
    }
})