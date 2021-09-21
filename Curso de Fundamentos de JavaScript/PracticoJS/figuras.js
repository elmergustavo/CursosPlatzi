// Cuadrado

let ladoC = 5;

const calcularPerimetroCuadrado = (lado) => {
  let perimetroCuadrado = lado * 4;
  return perimetroCuadrado;
};

let perimetroCuadrado = calcularPerimetroCuadrado(ladoC);
console.log(perimetroCuadrado + ' cm');

const calcularAreaCuadrado = (lado) => {
  let areaCuadrado = lado * lado;
  return areaCuadrado;
};

let areaCuadrado = calcularAreaCuadrado(ladoC);

console.log(areaCuadrado + ' cm^2');

// Triangulo

let ladoTriangulo1 = 6;
let ladoTriangulo2 = 6;
let baseTriangulo = 4;
let alturaTriangulo = 5.5;

const calcularPerimetroTriangulo = (
  ladoTriangulo1,
  ladoTriangulo2,
  baseTriangulo,
  alturaTriangulo
) => {
  let perimetro = ladoTriangulo1 + ladoTriangulo2 + baseTriangulo;
  return perimetro;
};
