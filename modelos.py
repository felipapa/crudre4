from pydantic import BaseModel

class arma1(BaseModel):
    nombre: str
    potencia: int
    velocidad: int
    capacidad: int
    precio: float

class arma2(BaseModel):
    id: int
    nombre: str
    potencia: int
    velocidad: int
    capacidad: int
    precio: float