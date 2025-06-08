# Archivo con las rutas POST, PUT o DELETE que vaya a tener nuestra API

#Utilizar fastApi que es nuestra libreria
from fastapi import APIRouter, HTTPException, Response, Request
from fastapi.responses import RedirectResponse
#Utilizamos las clases que creamos 
from model.bd import MYSQL_CONNECTOR #Clase realizar peticiones y conectarse a base de datos
from model.usuarios import Usuario as User_obj #Clase para cada movimiento del usuario
from model.estudiante import Estudiante as Studen_obj #Clase para cada movimiento del estudiante
from model.service import Services as Service_obj #Clase para cada movimiento de "servicio" como iniciar sesion
from model.cursos import CursoService #Clase que nos permite acceder a la base de datos con movimientos para los cursos
#Tipos para las rutas
from tipos.usuario import *
from tipos.login_info import *
from tipos.cursos import *
import json
#Librerias para leer archivos internos
import os
from dotenv import load_dotenv

#Inicializamos el objeto APIRouter para crear nuestras rutas
app = APIRouter()
# Leemos nuestra variable de entorno y obtenemos los datos necesarios para la conexión a nuestra bd
# usuario, contraseña, host y base de datos
load_dotenv()
user = os.getenv("USER")
password = os.getenv("PASS")
host = os.getenv("HOST")
db = os.getenv("DB")
# Nombramos el endpoint y debajo pasamos la funcion que hara
@app.post("/crear_usuario")
async def crear_usuario(user_data: UserRegistrationRequest):
     # Encapsulamos nuestra función en un try except para tener control sobre los errores que puedan surgir
    try:
        # Inicializamos nuestra clase MYSQL_CONNECTOR que nos conecta a base de datos y nos permite realizar peticiones a la bd
        dataBase = MYSQL_CONNECTOR(user, password, host, db)
        # En caso de que el tipo del usuario que recibimos sea 1 haremos lo siguiente
        if user_data.tipo == 1:
            # Inicializamos nuestro objeto Estudiante y le pasamos sus parametros de inico 
            student: Studen_obj = Studen_obj(user_data.correo, user_data.contrasena)
            # Guardamos el resultado en una variable
            result = student.create(data_base=dataBase, name=user_data.nombre, lastname=user_data.apellidos,
                                    user_type=user_data.tipo, curp=user_data.curp)
        # En caso de que el tipo no sea 1 haremos lo siguiente
        else:
            # Inicializamos nuestor objeto usuario 
            usuario: User_obj = User_obj(user_data.correo, user_data.contrasena)
            # Y creamos al usuario profesor
            result = usuario.create(data_base=dataBase, name=user_data.nombre, lastname=user_data.apellidos,
                                    user_type=user_data.tipo)
        # retornamos el resultado que obtengamos de dichos metodos
        return result
    # Captura el error que sea por HTTP y nos tira el error
    except HTTPException as e:
        raise e
    # Ante cualquier error imprimimos el error en consola y tiramos una excepcion HTTP y retornamos un estatus 500 
    except Exception as e:
        print("Ha ocurrido un error: ", e)
        raise HTTPException(status_code=500, detail="Ha ocurrido un error")
# Nombramos el endpoint y debajo pasamos la funcion que hara    
@app.post("/iniciar-sesion")
async def login(data: LoginInfo, response: Response):
     # Encapsulamos nuestra función en un try except para tener control sobre los errores que puedan surgir
    try:
        # Inicializamos nuestra clase MYSQL_CONNECTOR que nos conecta a base de datos y nos permite realizar peticiones a la bd
        dataBase = MYSQL_CONNECTOR(user, password, host, db)
        # Si contraseña o nuestro correo estan vacios retornara un 0 dando a entender que ocurrio algo mal o no llegaron los datos esperados
        if not (len(data.contrasena) or len(data.correo)): return {"estatus": 0, "result": {
            "message": "No se admiten vacios en los campos",
        }}
        # Iniciamos nuestro objeto User aqui nombrado con el alias User_obj y le pasamos sus datos necesarios
        usuario: User_obj = User_obj(data.correo, data.contrasena)
        # Iniciamos sesión gracias al objeto Service_obj
        login_response = Service_obj.login(dataBase, usuario)
        # Si el estatus que retorna es 1 indica que todo bien entonces pasamos a lo siguiente
        if login_response["estatus"] == 1:
            # Inicializamos los datos que esperamos que tenga nuestra sesión
            session_token = {"userId": login_response["result"]["user_id"], "tipo": login_response["result"]["tipo_usuario"]}
            # Creamos y configuramos la sesión del usuario con los datos que recibimos
            response.set_cookie(key="session", value= json.dumps(session_token), httponly=True, secure= False, domain="localhost", path="/")
            print("Se creo la cookie")
        # Retornamos la respuesta del servidor
        return login_response
    # Captura el error que sea por HTTP y nos tira el error
    except HTTPException as e:
        raise e
    # Ante cualquier error imprimimos el error en consola y tiramos una excepcion HTTP y retornamos un estatus 500 
    except Exception as e:
        print("Ha ocurrido un error: ", e)
        raise HTTPException(status_code=500, detail="Ha ocurrido un error")
@app.post("/comprar-certificado")
async def buyCertificate(data: ComprarCurso, request:Request):
    try:
        session = request.cookies.get("session")
        print("La session es : ", session)
        if not session: return { "estatus": -1, "result": { "message": "Debes iniciar sesión"}}
        userId = json.loads(session)["userId"]
        service: CursoService = CursoService(user, password, host, db)
        result = service.buy_course(userId, data.curso_id)
        print(result)
        return result
    # Captura el error que sea por HTTP y nos tira el error
    except HTTPException as e:
        raise e
    # Ante cualquier error imprimimos el error en consola y tiramos una excepcion HTTP y retornamos un estatus 500 
    except Exception as e:
        print("Ha ocurrido un error: ", e)
        raise HTTPException(status_code=500, detail="Ha ocurrido un error")
# Nombramos el endpoint y debajo pasamos la funcion que hara
@app.get("/cerrar-sesion")
def logout():
     # Encapsulamos nuestra función en un try except para tener control sobre los errores que puedan surgir
    try:
        # Redirigimos al usuario al home de nuestro sitio 
        response = RedirectResponse(url="/", status_code=302)
        # Eliminamos la sesión que tenga activa
        response.delete_cookie("session")
        # Retornamos la acción realizada
        return response
    # Captura el error que sea por HTTP y nos tira el error
    except HTTPException as e:
        raise e
    # Ante cualquier error imprimimos el error en consola y tiramos una excepcion HTTP y retornamos un estatus 500 
    except Exception as e:
        print("Ha ocurrido un error: ", e)
        raise HTTPException(status_code=500, detail="Ha ocurrido un error")