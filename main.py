from conexion import get_connection, initDb
from fastapi import FastAPI, Depends
from sqlite3 import Connection
from armasmanager import armasmanager2
from modelos import arma1, arma2
from fastapi.middleware.cors import CORSMiddleware


ArmasMa = armasmanager2()

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       
    allow_credentials=True,      
    allow_methods=["*"],         
    allow_headers=["*"],         
)

@app.on_event("startup")
def startup():
    print("iniciamos db")
    initDb()

@app.post("/agregar")
def postProduct(arma: arma1, conexion: Connection = Depends(get_connection)):
    return ArmasMa.AgregarArma(arma, conexion)

@app.get("/leer_armas")
def getproductos(conexion: Connection = Depends(get_connection)):
    return ArmasMa.leerArma(conexion)

@app.delete("/eliminar_armas/{id}")
def deletproductos(id: int, conexion: Connection = Depends(get_connection)):
    return ArmasMa.eliminar(id, conexion)

@app.put("/actualizararmas")
def actualizarproducto(arma: arma2, conexion: Connection = Depends(get_connection)):
    return ArmasMa.actualizar(arma, conexion) 

@app.get("/leer_daño")
def getdaño(daño: int, conexion: Connection = Depends(get_connection)):
    return ArmasMa.leerDaño(conexion, daño)

@app.get("/leer_precio")
def getdaño(precio: int, conexion: Connection = Depends(get_connection)):
    return ArmasMa.LeerPrecio(conexion, precio)

@app.get("/")
def read_root():
    return {"mensaje": "CORS configurado correctamente"}
