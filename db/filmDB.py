from db import clientPM
from bson.objectid import ObjectId
from datetime import datetime
import json

#Schea per poder operar amb l'objecte 
def film_schema(film)->dict:
    return {"id": str(film["_id"]),
            "title": film["title"],
            "director": film["director"],
            "year": film["year"],
            "genere": film["genere"],
            "rating": film["rating"],
            "country": film["country"],
    }
    
def films_schema(films) ->dict:
    return[film_schema(film) for film in films]


    
def consulta():
    try:    
        conn= clientPM.dbFilms()
        data=conn.films.find()
        result =films_schema(data)
        return result
    except Exception as e:
        return f'Erroe conexió {e}'
    
def consultaGenere(genere):
    try:    
        conn= clientPM.dbFilms()
        #Pasem el valor de genere com a "genere"
        data=conn.films.find({"genere": genere})
        result =films_schema(data)
        return result
    except Exception as e:
        return f'Erroe conexió {e}'
    
def consultaOrder(field, order):
    try:    
        conn= clientPM.dbFilms()
        data=conn.films.find().sort(field, order)
        result =films_schema(data)
        return result
    except Exception as e:
        return f'Erroe conexió {e}'
    
def consultaLimit(limit):
    try:    
        conn= clientPM.dbFilms()
        data=conn.films.find().limit(limit)
        result =films_schema(data)
        return result
    except Exception as e:
        return f'Erroe conexió {e}'
        

def consultaId(id):
    try:
        conn= clientPM.dbFilms()
        data=conn.films.find_one({"_id" : ObjectId(id)})
        result =film_schema(data)
        return result
    except Exception as e:
        return f'Error conexió {e}'
            

def createFilm(film):
    try:
        conn= clientPM.dbFilms()
        now = datetime.now() #Data i hora en el moment de l'execució
        data={
            "title": film.title,
            "director": film.director,
            "year": film.year,
            "genere": film.genere,
            "rating": film.rating,
            "country": film.country,
            "created_at": now,
            "update_at": now
        }
        id=conn.films.insert_one(data).inserted_id
        return {"OK": str(id)}
    except Exception as e:
        return f'Error conexió {e}'
        
        
        
def deleteFilm(id):
    try:
        conn= clientPM.dbFilms()
        conn.films.delete_one({"_id" : ObjectId(id)})
        return "Film eliminada"
    except Exception as e:
        return f'Error conexió {e}'
        
        
def updateFilms(id, film):
    try:
        conn= clientPM.dbFilms()
        now = datetime.now()
        data={
            "title": film.title,
            "director": film.director,
            "year": film.year,
            "genere": film.genere,
            "rating": film.rating,
            "country": film.country,
            "created_at": now,
            "update_at": now
        }  
        conn.films.update_one({"_id" : ObjectId(id)}, {"$set": data})
        return 'Pelicula actualitzat'
    except Exception as e:

        return f'Error conexió {e}'

