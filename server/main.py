# Importamos las funciones necesarias de nuestraas librerias que hemos descargado
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import os
# Importamos a los archivos de controllers y views de nuestra carpeta de routes
from routes import controllers, views

frontend_path = os.path.join(os.path.dirname(__file__), "../app/build")

# Inicializamos nuestra aplicación y pasaremos a configurarlo
app = FastAPI()
# Añadimos el middleware cors para realizar la conexión entre el front y el backend en este caso estamos dando acceso a cualquier sitio que se quiere coenctar
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # o ["*"] para permitir todos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Añadimos a las rutas del sitio los archivos sobre todo en sus configuraciones de app de view y controllers
app.include_router(views.app)
app.include_router(controllers.app)

app.mount("/static", StaticFiles(directory="../app/build/static"), name="static")
@app.get("/{full_path:path}")
async def serve_react_app():
    file_path = os.path.join(frontend_path, "index.html")
    return FileResponse(file_path)