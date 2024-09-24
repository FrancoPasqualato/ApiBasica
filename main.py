#FASTAPI - UVICORN
from typing import Optional
from pydantic import BaseModel, EmailSTR

class Persona(BaseModel):
    id: Optional[int]= None
    nombre: str
    edad: int
    email: EmailSTR

#API
