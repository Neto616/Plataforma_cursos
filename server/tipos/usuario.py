# Igualmente generamos itpo de datos aqui que nos ayudará en la creación de los usuarios
# Importamos pydantinc para crear nuestros tipos de datos de entrada
from pydantic import BaseModel
# Nos permite crear tipos de datos en este caso literal y union
from typing import Literal, Union


# Cuando el usuario es de tipo = 1 indica que es un estudiante
# Cuando el usuario es de tipo = 2 indica que es un maestro
# El tipo de usuario en formato numerico nos permite la compatibilidad con el id que este tenga en base de datos

# Clase usuario donde recibimos su nombre apellidos, correo y contraseña
class Usuario(BaseModel):
    nombre: str
    apellidos: str
    correo: str
    contrasena: str
    
# Tipo estudiante que hereda de usuario sus atributos pero se les agrega el curp y el tipo de dato 1 o 2 donde 1 es estudiante
class Estudiante(Usuario):
    curp: str
    tipo: Literal["1"] = 1
    
# Tipo de Maestro que hereda los atributos de usuario donde su tipo esperado es 2
class Maestro(Usuario):
    tipo: Literal["2"] = 2
# Aqui unimos los dos tipos de usuarios para dar a entender que esperamos cualquiera de esos dos tipos
UserRegistrationRequest = Union[Estudiante, Maestro]
