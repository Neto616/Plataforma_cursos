# Archivo con las rutas de de tipo get que tenga el sitio

#Utilizar fastApi que es nuestra libreria
from fastapi import APIRouter, HTTPException, Response, Request
from fastapi.responses import RedirectResponse
#Llamamos a las clases creadas para obtener la información necesaria
from model.cursos import CursoService
#Librerias apra leer archivos del sistema
import os
from dotenv import load_dotenv
# Leemos nuestra variable de entorno y obtenemos los datos necesarios para la conexión a nuestra bd
# usuario, contraseña, host y base de datos
load_dotenv()
user = os.getenv("USER")
password = os.getenv("PASS")
host = os.getenv("HOST")
db = os.getenv("DB")
# Inicializamos nuestras rutas de la api
app = APIRouter()

# Definimos el endpoint y llamamos a su respectiva función
# @app.get("/")
# async def inicio():
    # # Encapsulamos nuestra función en un try except para tener control sobre los errores que puedan surgir
    # try:
    #     response = RedirectResponse(url="/estudiantes/", status_code=302)
    #     response.delete_cookie("session")
    #     return response
    # # Captura el error que sea por HTTP y nos tira el error
    # except HTTPException as e:
    #     raise e
    # # Ante cualquier error imprimimos el error en consola y tiramos una excepcion HTTP y retornamos un estatus 500 
    # except Exception as e:
    #     print("Ha ocurrido un error: ", e)
    #     raise HTTPException(status_code=500, detail="Ha ocurrido un error")

@app.get("/capitulos/{curso}")
async def obtener_capitulos(curso: int):
     # Encapsulamos nuestra función en un try except para tener control sobre los errores que puedan surgir
    try:
        # Inicializamos nuestra clase Curso Service que se encarga de obtener los datos de los cursos 
        cursos_service: CursoService = CursoService(user, password, host, db)
        # Obtenemos los capitulos del curso que tenemos
        list_course = cursos_service.obtain_chapter(curso)
        # Retornamos el arreglo con los capitulos q tenga el curso
        return list_course
    # Captura el error que sea por HTTP y nos tira el error
    except HTTPException as e:
        raise e
    # Ante cualquier error imprimimos el error en consola y tiramos una excepcion HTTP y retornamos un estatus 500 
    except Exception as e:
        print("Ha ocurrido un error: ", e)
        raise HTTPException(status_code=500, detail="Ha ocurrido un error")

@app.get("/obtener_cursos")
async def obtener_cursos():
     # Encapsulamos nuestra función en un try except para tener control sobre los errores que puedan surgir
    try:
        # Inicializamos nuestra clase Curso Service que se encarga de obtener los datos de los cursos 
        cursos_service: CursoService = CursoService(user, password, host, db)
        # Obtenemos todos los cursos que estan dados de alta
        list_course = cursos_service.obtain_courses()
        # Retornamos el arreglo de los cursos que tenemos dados de alta
        return list_course
    # Captura el error que sea por HTTP y nos tira el error
    except HTTPException as e:
        raise e
    # Ante cualquier error imprimimos el error en consola y tiramos una excepcion HTTP y retornamos un estatus 500 
    except Exception as e:
        print("Ha ocurrido un error: ", e)
        raise HTTPException(status_code=500, detail="Ha ocurrido un error")