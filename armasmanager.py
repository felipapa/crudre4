import sqlite3
from modelos import arma1, arma2

class armasmanager2:
    def __init__(self):
        pass

    def AgregarArma(self, arma: arma1, conexion: sqlite3.Connection):
        conexion.execute(
            "INSERT INTO armas (nombre, potencia, velocidad, capacidad, precio) VALUES (?, ?, ?, ?, ?)",
            (arma.nombre, arma.potencia, arma.velocidad, arma.capacidad, arma.precio),
        )
        return "arma agregada"

    def leerArma(self, conexion: sqlite3.Connection):
        res = conexion.execute("SELECT * FROM armas").fetchall()
        return [dict(item) for item in res]

    def eliminar(self, id, conexion: sqlite3.Connection):
        conexion.execute("DELETE FROM armas WHERE id = ?", (id,))
        return f"se elimino {id}"

    def actualizar(self, arma: arma2, conexion: sqlite3.Connection):
        nuevonombre = arma.nombre 
        nuevapotencia = arma.potencia
        nuevavelocidad = arma.velocidad 
        nuevacapacidad = arma.capacidad
        nuevoprecio = arma.precio
        id = arma.id
        conexion.execute(
            "UPDATE armas SET nombre = ?, potencia = ?, velocidad = ?, capacidad = ?, precio = ? WHERE id = ?", 
            (nuevonombre, nuevapotencia, nuevavelocidad, nuevacapacidad, nuevoprecio, id)
        )
        return f"se actualizo {id}"

    def leerDaño(self, conexion: sqlite3.Connection, daño: int):
        consulta = conexion.execute(
        "SELECT * FROM armas WHERE potencia >= ?",
        (daño,)
    )
        res = consulta.fetchall()
        return [dict(item) for item in res]

    def LeerPrecio(self, conexion: sqlite3.Connection, precio: int):
        consulta = conexion.execute(
        "SELECT * FROM armas WHERE precio >= ?",
        (precio,)
    )
        res = consulta.fetchall()
        return [dict(item) for item in res]


        