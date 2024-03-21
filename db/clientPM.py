import pymongo

#Conexió de la bbdd
def dbFilms():
    try:
        return pymongo.MongoClient("mongodb://localhost:27017/").M07 #M07 el nom de la bbdd
    except Exception as e:
        print(f"ERROR: {e}")