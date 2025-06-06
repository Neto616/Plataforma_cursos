# Pydantic nos permite crear modelos bases que son para esperar ciertos datos y ciertos tipos de datos para
# asi poder solicitarlos en los endpoints
from pydantic import BaseModel
# CRreamos una clase con los datos que esperamos de parte del login en este caso unicamente correo y contraseña donde ambos son strings
class LoginInfo(BaseModel):
    correo: str
    contrasena: str