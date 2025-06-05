from pydantic import BaseModel
from typing import Literal, Union


# Cuando el usuario es de tipo = 1 indica que es un estudiante
# Cuando el usuario es de tipo = 2 indica que es un maestro
# El tipo de usuario en formato numerico nos permite la compatibilidad con el id que este tenga en base de datos

class Usuario(BaseModel):
    nombre: str
    apellidos: str
    correo: str
    contrasena: str
    
class Estudiante(Usuario):
    curp: str
    tipo: Literal[1] = 1
    
class Maestro(Usuario):
    tipo: Literal[2] = 2

UserRegistrationRequest = Union[Estudiante, Maestro]
