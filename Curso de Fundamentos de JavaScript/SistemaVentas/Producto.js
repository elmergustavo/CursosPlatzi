class Producto {
  static contadorProducto = 0;

  constructor(nombre, precio) {
    this._idProducto = ++Producto.contadorProducto;
    this._nombre = nombre;
    this._precio = precio;
  }

  get idProducto() {
    return this._idProducto;
  }

  get nombre() {
    return this._nombre;
  }

  get precio() {
    return this._precio;
  }

  set nombre(nombre) {
    this._nombre = nombre;
  }

  set precio(precio) {
    this._precio = precio;
  }

  toString() {
    return `id Producto: ${this._idProducto}
    nombre: ${this._nombre}
    precio: $${this._precio}
    `;
  }
}

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

let producto1 = new Producto('Maiz', 2000);
let producto2 = new Producto('Platano', 4000);

let orden1 = new Orden();
orden1.agregarProducto(producto1);
orden1.agregarProducto(producto2);

orden1.mostrarOrden();
