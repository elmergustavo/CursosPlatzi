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

class Monitor {
  static contadorMonitores = 0;

  constructor(marca, tamaño) {
    this._idMonitor = ++Monitor.contadorMonitores;
    this._marca = marca;
    this._tamaño = tamaño;
  }

  get idMonitor() {
    return this._idMonitor;
  }

  get marca() {
    return this._marca;
  }

  set marca(marca) {
    this._marca = marca;
  }

  get tamaño() {
    return this._tamaño;
  }

  set tamaño(tamaño) {
    this._tamaño = tamaño;
  }

  toString() {
    return `idMonitor: ${this._idMonitor}, marca: ${this._marca}, tamaño: ${this._tamaño}`;
  }
}

class Computadora {
  static contadorComputadoras = 0;

  constructor(nombre, monitor, teclado, raton) {
    this._idComputadora = ++Computadora.contadorComputadoras;
    this._nombre = nombre;
    this._monitor = monitor;
    this._teclado = teclado;
    this._raton = raton;
  }

  get idComputadora() {
    return this._idComputadora;
  }

  get nombre() {
    return this._nombre;
  }

  set nombre(nombre) {
    this._nombre = nombre;
  }

  get monitor() {
    return this._monitor;
  }

  set monitor(monitor) {
    this._monitor = monitor;
  }

  get teclado() {
    return this._teclado;
  }

  set teclado(teclado) {
    this._teclado = teclado;
  }

  get raton() {
    return this._raton;
  }

  set raton(raton) {
    this._raton = raton;
  }

  toString() {
    return `
    idComputadora: ${this._idComputadora},
    nombre: ${this._nombre},
    monitor: ${this._monitor},
    teclado: ${this._teclado},
    raton: ${this._raton}`;
  }
}

class Ordenes {
  static contadorOrdenes = 0;

  constructor() {
    this._idOrden = ++Ordenes.contadorOrdenes;
    this._computadoras = [];
  }

  agregarComputadora(computadora) {
    this._computadoras.push(computadora);
  }

  mostrarOrdenes() {
    let computadorasOrdenes = '';
    this._computadoras.forEach((computadora) => {
      computadorasOrdenes += `\n ${computadora}`;
    });

    console.log(
      `Ordenes: ${this._idOrden}, computadoras: ${computadorasOrdenes}`
    );
  }

  // toString() {
  //   return `Orden: ${this._idOrden}, computadoras: ${this._computadoras}`;
  // }
}

let raton1 = new Raton('in', 'Logitec');
let raton2 = new Raton('in', 'Razer');
let teclado1 = new Teclado('tec', 'Razer');
let teclado2 = new Teclado('tec', 'Logitec');
let monitor1 = new Monitor('Samsung', '22PX');
let monitor2 = new Monitor('LG-G', '24PX');

let computadora1 = new Computadora('MyPC', monitor1, teclado2, raton2);
let computadora2 = new Computadora('MyOtherPC', monitor2, teclado1, raton1);

let orden1 = new Ordenes();
orden1.agregarComputadora(computadora1);
orden1.agregarComputadora(computadora2);

console.log(orden1.mostrarOrdenes());
// console.log(orden1.toString());
