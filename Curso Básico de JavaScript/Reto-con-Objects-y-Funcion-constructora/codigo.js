const modelos = ["Tesla", "Ford", "Dodge"]
var modelos_tesla = ["Model 3", "Model S", " Model X"]
var modelos_Ford = ["Mustang", "Explorer", "F-150"]
var modelos_dodge = ["Charger", "Challenger", "Durango"]
var anos = [2020, 2019, 2018, 2017, 2016]
baseDatos = [];

function autos_registro(marca, modelo, ano) {
    this.marca = marca;
    this.modelo = modelo;
    this.ano = ano;
}

function capturar() {
    var cantidad_registros = document.getElementById("myText").value;
    console.log(cantidad_registros);


    for (let i = 0; i < cantidad_registros; i++) {

        var random = Math.floor(Math.random() * 3);

        if (random == 0) {
            this["nuevo_registro"] = new autos_registro(modelos[random], modelos_tesla[Math.floor(Math.random() * 3)], anos[Math.floor(Math.random() * 4)]);
            baseDatos.push(this["nuevo_registro"]);
            document.getElementById("tabla").innerHTML += "<td>" + this["nuevo_registro"].marca + "</td>" + "<td>" + this["nuevo_registro"].modelo + "</td>" + "<td>" + this["nuevo_registro"].ano + "</td>";
        } else if (random == 1) {
            this["nuevo_registro"] = new autos_registro(modelos[random], modelos_Ford[Math.floor(Math.random() * 3)], anos[Math.floor(Math.random() * 4)]);
            baseDatos.push(this["nuevo_registro"]);
            document.getElementById("tabla").innerHTML += "<td>" + this["nuevo_registro"].marca + "</td>" + "<td>" + this["nuevo_registro"].modelo + "</td>" + "<td>" + this["nuevo_registro"].ano + "</td>";
        } else {
            this["nuevo_registro"] = new autos_registro(modelos[random], modelos_dodge[Math.floor(Math.random() * 3)], anos[Math.floor(Math.random() * 4)]);
            baseDatos.push(this["nuevo_registro"]);
            document.getElementById("tabla").innerHTML += "<td>" + this["nuevo_registro"].marca + "</td>" + "<td>" + this["nuevo_registro"].modelo + "</td>" + "<td>" + this["nuevo_registro"].ano + "</td>";
        }

    }

}
