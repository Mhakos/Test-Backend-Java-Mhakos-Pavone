from pydantic import BaseModel
from typing import List



class Libros(BaseModel):
    name: str = "Casas Muertas"
    price: float = 250,55
    id: int = 1
    description: str = "Crear Libros"



class ListBook(BaseModel):
    libros: List[Libros]