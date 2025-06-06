# Importamos nuestra clase MYSQL_CONNECTOR ya que nos conectaremos a base de datos
from model.bd import MYSQL_CONNECTOR
# Importamos nuestra clase Usuario ya que Services Utiliza del objeto Usuario
from model.usuarios import Usuario
#Librerias para leer archivos internos
import os
from dotenv import load_dotenv
# Leemos las variables de entorno que hemos creadp
load_dotenv()
# Obtenemos el secreto con el cual encriptamos la contraseña del usuario en sql
secret = str(os.getenv("SECRET"))

class Services():
    # Inicializamos nuestra clase y para service no requiere parametros de entrada
    def __init__(self):
        pass
    # Creamos una clase estatica por si en un futuro la clase Service requiere de parametros de inicialización
    @staticmethod
    # Esta función se encarga de realizar el login del usuario
    # Recibe como parametro la clase de base de datos que hemos creado y la clase usuario ya que requiere de metodos que este tiene
    def login(data_base: MYSQL_CONNECTOR, usuario: Usuario):
        # Utilizamos el metodo has_existence para verificar que el usuario exista dentro de nuestra base de datos
        user_exist = usuario.has_existence(data_base) # Retorna un booleano True o False dependiendo si existe o no
        # En caso de que no exista retorna un string advirtiendo que el usuario no existe
        if not user_exist: return "El usuario no existe"
        # En caso de si existir realizaremos una consulta a base de datos trayendo la contraseña que tenemos pero ya desencriptada
        consulta = """ SELECT 
            CAST(AES_DECRYPT(contrasena, %s) AS CHAR) AS decrypted_contrasena 
            FROM usuario where correo = %s and estatus = 1"""
        # Utilizamos el metodo para realizar la consulta select y le pasamos los parametros requeridos
        data = data_base.select_queries(consulta, secret, usuario.correo)
        # Obtenemos la información del usuario
        info_user = usuario.get_info_by_mail(data_base)
        # En caso de que las contraseñas no se parezcan retornamos un estatuso 0 dando a entender que no estan correctas las credenciales
        if data[0]["decrypted_contrasena"] != usuario._contrasena: 
            return {"estatus": 0, "result": {
            "message": f"Error en las credenciales",
            "user_id": 0,
            "tipo_usuario": 0
        }}
        # En cao contrario retornamos uno y los datos necesarios para la ceración de la sesión para el usuarip
        return {"estatus": 1, "result": {
            "message": f"Bienvenido {info_user['result']['data'][0]["nombre_completo"]}",
            "user_id": info_user['result']['data'][0]['id'],
            "tipo_usuario": info_user['result']['data'][0]['tipo_usuario']
        }}
# Pruebas realizadas para verificar el funcionamiento de la clase creada
if __name__ == "__main__":
    user = os.getenv("USER")
    password = os.getenv("PASS")
    host = os.getenv("HOST")
    db = os.getenv("DB")

    dataBase = MYSQL_CONNECTOR(user, password, host, db)
    usuario1: Usuario = Usuario("basn160603@gmail.com", "Cpapu")
    print(Services.login(dataBase, usuario1))