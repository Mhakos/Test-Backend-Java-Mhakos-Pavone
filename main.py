from fastapi import FastAPI
import json
from libros import Libros, ListBook
import uvicorn
from fastapi import status
from config.database import Session, engine, Base
#from models.libros import Libros as LibroModel
app = FastAPI()

table_Book = []

Base.metadata.create_all(bind=engine)

@app.get("/all_Book",status_code=status.HTTP_200_OK, response_model=ListBook, tags={"BOOK"})
def sample_all_Book():

        """
 ## ARG
        --Books: List(Book)
 ## RESPONSE
             name: str
             id: int 
        
         """
        return ListBook(libros=table_Book)

@app.get("/{id}",status_code=status.HTTP_200_OK, response_model=Libros, summary="this endpoint sample a book", tags={"BOOK"})
def Sample_Book(id: int):

    """
 ## ARG
        --libros: Libros
 ## RESPONSE
             name: str
             id: int 
        
    """

    for Book in table_Book:
        if Book.id == id:
            return Book
    return {}

@app.post("/create_Book", status_code=status.HTTP_201_CREATED, response_model=Libros, summary="this endpoint create a book", tags={"BOOK"})
def create_Libros(libros: Libros):

    """
  ## ARG
        --libros: Libros
  ## RESPONSE
        --libros: Libros
        name: str
        price: float 
        id: int 
        description: str 
    """
    db = Session()
    new_libros = LibrosModel(** libros.dict())
    db.add(new_libros)
    db.commit()
    return{}

@app.delete("/{id}",status_code=status.HTTP_200_OK, response_model=Libros, summary="this endpoint delete a book", tags={"BOOK"})
def Delete_Book(id: int):

    """
 ## ARG
        --libros: Libros
 ## RESPONSE
             name: str
             id: int 
        
    """
    for Book in table_Book:
        if Book["id"] == id:
            Book_del = Book
            table_Book.remove(Book)
            return Book_del
    return {}



@app.patch("/{id}",status_code=status.HTTP_200_OK, response_model=Libros, summary="this endpoint update a book", tags={"BOOK"})
def Update_Book(id: int, name: str):
    """
 ## ARG
        --libros: Libros
 ## RESPONSE
             name: str
             id: int 
        
    """

    for Book in table_Book:
        if Book["id"] == id:
            Book["name"] = name
            return Book
    return {}


