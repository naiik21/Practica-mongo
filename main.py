from typing import Union
from fastapi import FastAPI, UploadFile
from Model.Film import Film
from db import clientPM
from db import filmDB

app = FastAPI()
conn= clientPM.dbFilms()

@app.get("/")
def red_root():
    clientPM.dbFilms()
    return {"Hello":"World"}


@app.get("/films")
def getProducts():
    clientPM.dbFilms()
    data= filmDB.consulta()
    return data

#Filtrem per genere, en aquest cas com a predeterminat Comedy
@app.get("/filmsGenere")
def getProducts(genere: str = "Comedy"):
    clientPM.dbFilms()
    data= filmDB.consultaGenere(genere)
    return data

#Ordenem la taula per title de manera ascendent
@app.get("/filmsOrder")
def getProducts(field: str = "title", order: str = "asc"):
    clientPM.dbFilms()
    # Convertir el parámetro de orden a la orden de ordenamiento de MongoDB
    mongo_order = 1 if order == "asc" else -1
    data = filmDB.consultaOrder(field, mongo_order)
    return data

#En retornara només les 10 primeres 
@app.get("/filmsLimit")
def consultaLimit(limit: int = "10"):
    clientPM.dbFilms()
    data = filmDB.consultaLimit(limit)
    return data
    

@app.get("/film/{id}")
def getProductId(id):
    clientPM.dbFilms()
    data= filmDB.consultaId(id)
    return data


@app.post("/film/")
def createFilm(film: Film):
    data=filmDB.createFilm(film)
    return data


@app.put("/film/{id}")
def updateProduct(id, film:Film):
    clientPM.dbFilms()
    data=filmDB.updateFilms(id, film)
    return data


@app.delete("/film/{id}")
def deleteProduct(id):
    clientPM.dbFilms()
    data=filmDB.deleteFilm(id)
    return data

