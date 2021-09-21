class DispositivoEntrada {
  constructor(tipoEntrada, marca) {
    this._tipoEntrada = tipoEntrada;
    this._marca = marca;
  }

  get tipoEntrada() {
    return this._tipoEntrada;
  }

  set tipoEntrada(tipoEntrada) {
    this._tipoEntrada = tipoEntrada;
  }

  get marca() {
    return this._marca;
  }

  set marca(marca) {
    this._marca = marca;
  }
}

class Raton extends DispositivoEntrada {
  static contadorRatones = 0;

  constructor(tipoEntrada, marca) {
    super(tipoEntrada, marca);
    this._idRaton = ++Raton.contadorRatones;
  }

  toString() {
    return `id Raton: ${this._idRaton}, tipoEntrada: ${this._tipoEntrada}, marca: ${this._marca}`;
  }
}

let raton1 = new Raton('YS', 'Logitec');
let raton2 = new Raton('in', 'Razer');
raton1.tipoEntrada = 'USB';
raton2.tipoEntrada = 'Bluetooth';
console.log(raton1.toString());
console.log(raton2.toString());

class Teclado extends DispositivoEntrada {
  static contadorTeclados = 0;

  constructor(tipoEntrada, marca) {
    super(tipoEntrada, marca);
    this._idTeclado = ++Teclado.contadorTeclados;
  }

  toString() {
    return `id Teclado: ${this._idTeclado}, tipoEntrada: ${this._tipoEntrada}, marca: ${this._marca}`;
  }
}

let teclado1 = new Teclado('tec', 'Razer');
let teclado2 = new Teclado('tec', 'Logitec');
console.log(teclado1.toString());
console.log(teclado2.toString());
