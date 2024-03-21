
**1.  Crear un entorn amb FastAPI**
    
Utilitzar el framework fastapi per crear una api rest

[https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)

  

**2.  Crear una bases de dades amb MongoDB i tingui una colecció que es digui films. Aquesta tindrà la següent estructura**
    

    {
    "title": “str”,
    "director": “str”,
    "year": int,
    "genre": “str”,
    "rating":number ,
    "country": “str”,
    "created_at": “date”,
    "update_at": “date”,
    }

  

**3.  Les funcionalitats que ens demanen el client:**
    

 1. CRUD Films: (7 punts)
    
	-   Ruta:  /films/
   		*Tipus de petició*: Get
   		
		*Funcionament*: Retorna **un objecte json que contindrà** “status”:1 i “data”: una llista d’objectes json amb tota la informació dels films.

		En cas d’error **retornarà un objecte  json** que contindrà “status” : -1 i “messatge”: missatge amb l’error que s’ha produït.
  
	-   Ruta:  /film/{id}
    *Tipus de petició*: Get

		*Funcionament:* Retorna **un objecte json** que contindrà “status”:1 i “data”: un objecte json amb la informació del film que la id de la bases de dades coincideix amb la id que ens arribar per paràmetre.

		En cas d’error retornarà **un objecte  json** que contindrà “status” : -1 i “message”: missatge amb l’error que s’ha produït.

  

	-   Ruta:  /film/
    *Tipus de petició:* Post

		*Funcionament:* Permet afegir un nou film a la BBDD

		Retorna **un objecte json que contindrà** “status”:1 i “data”: un objecte json  amb la informació del nou film que s’ha afegit amb la id.

		En cas d’error **retornarà un objecte** que contindrà “status” : -1 i “message”: missatge amb l’error que s’ha produït.



	 -  Ruta:  /film/{id}
    *Tipus de petició:* Put

		*Funcionament:* Permet modificar qualsevol informació d’un film concret a la BBDD definit per la id que arriba per paràmetre.

		Retorna **un objecte json que contindrà** “status”:1 i “message”: “El film s’ha actualitzat correctament”.

		En cas d’error r**etornarà un objecte** que contindrà status : -1 i “message”: missatge amb l’error que s’ha produït.

  

	-   Ruta:  /film/{id}
    *Tipus de petició:* Delete

		*Funcionament:* Permet eliminar un producte de la BBDD

		Retorna **un objecte json que contindrà** “status”:1 i “messatge”: “El film s’ha eliminat correctament”.

		En cas d’error **retornarà un objecte** que contindrà status : -1 i “message”: missatge amb l’error que s’ha produït.



2.  Consultes avançades (3 punt)
    

	Fer servir query parameters per fer les següents consultes:

	Us podeu ajudar de la documentació: [https://fastapi.tiangolo.com/tutorial/query-params/](https://fastapi.tiangolo.com/tutorial/query-params/)

-   ?genre= (str)
    
	-   valor genre=”Action” | ”Drama” | ”Romance” | ”Thriller” | ”Comedy” | ”Horror” | ”Documentary” | ”Animation”
    
	-   Retorna **una llista d’objectes json** dels films segons el genre.
    
	-   Exemple ruta amb query parameters: ?genre=Comedy
    

-   ?field=(str)&order=(str)
   
	-   valor field= “title” | “director” | “year”
    
	-   valor order: “asc” | “desc”
    
	-   Retorna **una llista json** ordenada ascendent o descendent segons el camp de field.
    
	-   Exemple ruta amb query parameters: ?field=title&orderby=asc
    

-   ?limit=(int)
    
	-   Valor: 1 - 100
    
	-   Retorna **una objecte json** amb:
    

		-   “row_count”: número total de registres
    
		-   “data”: una llista d’objectes json segons el límit definit en el query parameter.
    

	-   Exemple ruta amb query parameters: ?limit=1
