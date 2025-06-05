from pydantic import BaseModel

class LoginInfo(BaseModel):
    correo: str
    contrasena: str