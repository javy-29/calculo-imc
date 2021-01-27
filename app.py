from typing import Optional
from fastapi import FastAPI, Path
from pydantic import BaseModel
from ConexionBDA import get_db 
import sqlite3


app = FastAPI()

class ItemIMC(BaseModel):
    nombre: str
    peso: int
    estatura: float


@app.get("/")
def read_root_get():
    return {"Hola": "Mundo"} 

@app.post("/calcula-imc")
def calcula_imc(item: ItemIMC):
    resultado = item.peso/item.estatura**2
    cursor = get_db()
    cursor.execute("Insert into imc (nombre, peso, estatura, resultado) values (?,?,?,?)", (item.nombre,item.peso,item.estatura,resultado))
    cursor.commit()
    return {"Hola": item.nombre, "Su IMC es:" : resultado} 

@app.get("/consulta-imc")
def get_consulta_imc():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, nombre, peso, estatura, resultado FROM imc"
    cursor.execute(query)
    lista = cursor.fetchall()
    resultados = []
    for elemento in lista:
        ##Iterar sobre las variables de la lista
        dato = {
            "id" : elemento[0], 
            "nombre" : elemento[1],
            "peso" : elemento[2],
            "estatura" : elemento[3],
            "resultado" : elemento[4]
        }
        resultados.append(dato) 

    return {"Historial" : resultados}


@app.get("/consulta-imc/{id}")
def get_consulta_imc_id(id : int):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, nombre, peso, estatura, resultado FROM imc where id = ?"
    cursor.execute(query, (id,))
    lista = cursor.fetchall()
    resultados = []
    for elemento in lista:
        ##Iterar sobre las variables de la lista
        dato = {
            "id" : elemento[0], 
            "nombre" : elemento[1],
            "peso" : elemento[2],
            "estatura" : elemento[3],
            "resultado" : elemento[4]
        }
        resultados.append(dato) 

    return {"Historial" : resultados}
