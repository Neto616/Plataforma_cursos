#Utilizar fastApi que es nuestra libreria
from fastapi import APIRouter, HTTPException, Response, Request
from fastapi.responses import RedirectResponse
#Utilizamos las clases que creamos 
from model.bd import MYSQL_CONNECTOR #Clase realizar peticiones y conectarse a base de datos
from model.usuarios import Usuario as User_obj #Clase para cada movimiento del usuario
from model.estudiante import Estudiante as Studen_obj #Clase para cada movimiento del estudiante
from model.service import Services as Service_obj #Clase para cada movimiento de "servicio" como iniciar sesion
#Tipos para las rutas
from tipos.usuario import *
from tipos.login_info import *
#Librerias para leer archivos internos
import os
from dotenv import load_dotenv

#Inicializamos el objeto APIRouter para crear nuestras rutas
app = APIRouter()

load_dotenv()
user = os.getenv("USER")
password = os.getenv("PASS")
host = os.getenv("HOST")
db = os.getenv("DB")

@app.post("/crear_usuario")
async def crear_usuario(user_data: UserRegistrationRequest):
    try:
        dataBase = MYSQL_CONNECTOR(user, password, host, db)
        if user_data.tipo == 1:
            print("Se creara un estudiante")
            student: Studen_obj = Studen_obj(user_data.correo, user_data.contrasena)
            result = student.create(data_base=dataBase, name=user_data.nombre, lastname=user_data.apellidos,
                                    user_type=user_data.tipo, curp=user_data.curp)
            print("Estudiante creado: ", result)
        else:
            print("Se creara un maestro")
            usuario: User_obj = User_obj(user_data.correo, user_data.contrasena)
            result = usuario.create(data_base=dataBase, name=user_data.nombre, lastname=user_data.apellidos,
                                    user_type=user_data.tipo)
        print("El result que se obtiene es: ", result)
        return result
    except HTTPException as e:
        raise e
    except Exception as e:
        print("Ha ocurrido un error: ", e)
        raise HTTPException(status_code=500, detail="Ha ocurrido un error")
    
@app.post("/iniciar-sesion")
async def login(data: LoginInfo, response: Response):
    try:
        print(data)
        dataBase = MYSQL_CONNECTOR(user, password, host, db)
        if not (len(data.contrasena) or len(data.correo)): return {"estatus": 0, "result": {
            "message": "No se admiten vacios en los campos",
        }}
        
        usuario: User_obj = User_obj(data.correo, data.contrasena)
        print(usuario.__str__())
        login_response = Service_obj.login(dataBase, usuario)
        
        if login_response["estatus"] == 1:
            session_token = {"userId": login_response["result"]["user_id"], "tipo": login_response["result"]["tipo_usuario"]}
            response.set_cookie(key="session", value= session_token, httponly=True)
            print("Se creo la cookie")

        print(login_response)
        return login_response
    except HTTPException as e:
        raise e
    except Exception as e:
        print("Ha ocurrido un error: ", e)
        raise HTTPException(status_code=500, detail="Ha ocurrido un error")
    
@app.get("/cerrar-sesion")
def logout():
    try:
        response = RedirectResponse(url="/", status_code=302)
        response.delete_cookie("session")
        return response
    
    except HTTPException as e:
        raise e
    except Exception as e:
        print("Ha ocurrido un error: ", e)
        raise HTTPException(status_code=500, detail="Ha ocurrido un error")