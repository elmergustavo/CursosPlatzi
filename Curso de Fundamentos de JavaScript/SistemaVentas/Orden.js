class Orden {
  static get MAX_PRODUCTOS() {
    return 5;
  }

  static contadorOrdenes = 0;

  constructor() {
    this._idOrden = ++Orden.contadorOrdenes;
    //Inicializamos la variable productos con un array vacio, esto hara referencia a que es un array
    this._productos = [];
    this._contadorProductosAgregados = 0;
  }

  get idOrden() {
    return this._idOrden;
  }

  agregarProducto(producto) {
    this._productos.length < Orden.MAX_PRODUCTOS
      ? (this._productos.push(producto), ++this._contadorProductosAgregados)
      : console.log(' No se pueden agregar más productos');

    // if (this._productos.length < Orden.MAX_PRODUCTOS) {
    //   this._productos.push(producto);
    //   ++this._contadorProductosAgregados;
    // }
  }

  calcularTotal() {
    let totalVenta = 0;
    for (let producto of this._productos) {
      totalVenta += producto.precio;
    }
    return totalVenta;
  }

  mostrarOrden() {
    let productosOrden = '';
    for (let producto of this._productos) {
      productosOrden += producto.toString() + ' ';
    }

    console.log(
      `Orden: ${
        this._idOrden
      }, Total: ${this.calcularTotal()}, Productos: ${productosOrden}`
    );
  }
}
