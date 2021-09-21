class Ordenes {
  static contadoOrdenes = 0;

  constructor() {
    this._idOrden = Ordenes.contadoOrdenes;
    this._computadoras = [];
  }

  agregarComputadora(computadora) {
    this._computadoras.push(computadora);
  }

  mostrarOrdenes() {
    let computadorasOrdenes = '';
    this._computadoras.forEach((computadora) => {
      computadorasOrdenes += computadora.toString() + ' ';
    });
  }

  toString() {
    return `id Orden: ${this._idOrden}, computadoras${this._computadoras}`;
  }
}
