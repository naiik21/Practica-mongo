from db import clientPM
from bson.objectid import ObjectId
from datetime import datetime
import json

keys=['product_id', 'name', 'description', 'company', 'price', 'units', 'subcategory_id', 'created_at', 'updated_at']

def transformJson(datas):
    result=[]
    # Iterar sobre cada diccionario en la lista
    for diccionario in datas:
        # Actualizar el diccionario_resultado con los datos del diccionario actual
        result.append(diccionario)
    return result
    
def consulta():
    try:    
        conn= clientPM.dbFilms()
        data=[]
        for x in conn.films.find():
            data.append(x)    
        resultJson = transformJson(data)
        return resultJson
    except Exception as e:
        return f'Erroe conexió {e}'
        

def consultaId(id):
    try:
        conn= clientPM.dbFilms()
        data=[]
        for x in conn.films.find({"_id":id}):
            data.append(x)    
        resultJson = transformJson(data)
        return resultJson
    except Exception as e:
        return f'Error conexió {e}'
            
        

def createFilm(film):
    try:
        conn= clientPM.dbFilms()
        now = datetime.now()
        data={
            "_id": film.id,
            "title": film.title,
            "director": film.director,
            "year": film.year,
            "genre": film.genre,
            "rating": film.rating,
            "country": film.country,
            "created_at": now,
            "update_at": now
        }
        result=conn.films.insert_one(data)
        inserted_id = result.inserted_id
        
        return inserted_id
    except Exception as e:
        return f'Error conexió {e}'
        
        
        
def deleteFilm(id):
    try:
        conn= clientPM.dbFilms()
        data=[]
        conn.films.delete_one({"_id":id})
        return "Film eliminada"
    except Exception as e:
        return f'Error conexió {e}'
        

   
        
def updateFilms(id, film):
    try:
        conn= clientPM.dbFilms()
        data=[]
        for x in conn.films.find({"_id":id}):
            data.append(x)  
        print(data)
        if (len(data)==0):
            return 'No existeix pelicula amb aquesta id'
        now = datetime.now()
        data={
            "title": film.title,
            "director": film.director,
            "year": film.year,
            "genre": film.genre,
            "rating": film.rating,
            "country": film.country,
            "created_at": now,
            "update_at": now
        }  
        conn.films.update_one({"_id": film.id}, {"$set": data})
        return 'Producte actualitzat'
    except Exception as e:

        return f'Error conexió {e}'

