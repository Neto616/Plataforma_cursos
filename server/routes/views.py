#Utilizar fastApi que es nuestra libreria
from fastapi import APIRouter, HTTPException, Response, Request
from fastapi.responses import RedirectResponse
#Llamamos a las clases creadas para obtener la información necesaria
from model.cursos import CursoService
#Librerias apra leer archivos del sistema
import os
from dotenv import load_dotenv

load_dotenv()
user = os.getenv("USER")
password = os.getenv("PASS")
host = os.getenv("HOST")
db = os.getenv("DB")

app = APIRouter()

@app.get("/")
async def inicio():
    try:
        response = RedirectResponse(url="/estudiantes/", status_code=302)
        response.delete_cookie("session")
        return response
    
    except HTTPException as e:
        raise e
    except Exception as e:
        print("Ha ocurrido un error: ", e)
        raise HTTPException(status_code=500, detail="Ha ocurrido un error")
    
@app.get("/{tipo}/")
async def inicio():
    print("Prueba de impresion")
    return { "estatus": 1, "info": { "message": "Hola mi gente" }}

@app.get("/capitulos/{curso}")
async def obtener_capitulos(curso: int):
    try:
        cursos_service: CursoService = CursoService(user, password, host, db)
        list_course = cursos_service.obtain_chapter(curso)
        
        return list_course
    except HTTPException as e:
        raise e
    except Exception as e:
        print("Ha ocurrido un error: ", e)
        raise HTTPException(status_code=500, detail="Ha ocurrido un error")

@app.get("/obtener_cursos")
async def obtener_cursos():
    try:
        cursos_service: CursoService = CursoService(user, password, host, db)
        list_course = cursos_service.obtain_courses()
        
        return list_course
    except HTTPException as e:
        raise e
    except Exception as e:
        print("Ha ocurrido un error: ", e)
        raise HTTPException(status_code=500, detail="Ha ocurrido un error")