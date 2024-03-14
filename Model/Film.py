from pydantic import BaseModel

class Film(BaseModel):
    id:str
    title:str
    director:str 
    year:int
    genre:str
    rating:int
    country: str
    created_at: str
    update_at: str
    