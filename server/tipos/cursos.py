# Pydantic nos permite crear modelos bases que son para esperar ciertos datos y ciertos tipos de datos para
# asi poder solicitarlos en los endpoints
from pydantic import BaseModel

#Creamos uan clase para definir los datos
#que esperamos del body

class ComprarCurso(BaseModel):
    curso_id: int