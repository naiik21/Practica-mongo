import pymongo

def dbFilms():
    try:
        return pymongo.MongoClient("mongodb://localhost:27017/").M07
    except Exception as e:
        print(f"ERROR: {e}")