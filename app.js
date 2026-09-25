/* https://fastapi.tiangolo.com/tutorial/cors/ */
/* https://developer.mozilla.org/es/docs/Web/API/Fetch_API/Using_Fetch */
/* https://github.com/rumman-ahmar/Todo-app-in-FastAPI-and-JS/blob/main/static/main.js */

var api = "http://127.0.0.1:8000"
var armas = []
var armasprecio = []

function renderizarTabla(listaArmas) {
    var tabla = document.getElementById("tabla")
    tabla.innerHTML = ""

    for (var i = 0; i < listaArmas.length; i++) {
        tabla.innerHTML += "<tr>" +
            "<td>" + listaArmas[i].id + "</td>" +
            "<td>" + listaArmas[i].nombre + "</td>" +
            "<td>" + listaArmas[i].potencia + "</td>" +
            "<td>" + listaArmas[i].precio + "</td>" +
            "<td><button id='borrar" + listaArmas[i].id + "'>Borrar</button></td>" +
            "</tr>"
    }

    for (var j = 0; j < listaArmas.length; j++) {
        document.getElementById("borrar" + listaArmas[j].id).onclick = function () {
            borrar(this.id.replace("borrar", ""))
        }
    }

    document.getElementById("mensaje").textContent =
        "Se cargaron " + listaArmas.length + " armas."
}

function cargarArmas() {
    fetch(api + "/leer_armas")
        .then(function (respuesta) { return respuesta.json() })
        .then(function (datos) {
            armas = datos
            renderizarTabla(armas)
        })
        .catch(function () {
            document.getElementById("mensaje").textContent = "No hay conexion con la api"
        })
}

function LeerPrecio() {
    var precio = document.getElementById("filtroPrecio").value
    fetch(api + "/leer_precio?precio=" + precio)
        .then(function (respuesta) { return respuesta.json() })
        .then(function (datos) {
            armasprecio = datos
            renderizarTabla(armasprecio)
        })
        .catch(function () {
            document.getElementById("mensaje").textContent = "No hay conexion con la api"
        })
}

function leerDaño() {
    var daño = document.getElementById("filtroDaño").value
    fetch(api + "/leer_daño?daño=" + daño)
        .then(function (respuesta) { return respuesta.json() })
        .then(function (datos) {
            var armasDaño = datos
            renderizarTabla(armasDaño)
        })
        .catch(function () {
            document.getElementById("mensaje").textContent = "No hay conexion con la api"
        })
}

function agregarArma() {
    var arma = {
        nombre: document.getElementById("nombre").value,
        potencia: Number(document.getElementById("potencia").value),
        velocidad: Number(document.getElementById("velocidad").value),
        capacidad: Number(document.getElementById("capacidad").value),
        precio: Number(document.getElementById("precio").value)
    }

    fetch(api + "/agregar", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(arma)
    }).then(function () {
        document.querySelector("form").reset()
        cargarArmas()
    })
}

function borrar(id) {
    if (confirm("¿Borrar esta arma?")) {
        fetch(api + "/eliminar_armas/" + id, { method: "DELETE" })
            .then(function () { cargarArmas() })
    }
}

document.getElementById("cargar").onclick = cargarArmas
document.getElementById("agregar").onclick = agregarArma

document.getElementById("buscarPrecio").onclick = LeerPrecio
document.getElementById("buscarDaño").onclick = leerDaño
