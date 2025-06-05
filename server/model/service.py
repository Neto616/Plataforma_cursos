from jinja2.utils import consume

from model.bd import MYSQL_CONNECTOR
from model.usuarios import Usuario
import os
from dotenv import load_dotenv
load_dotenv()
secret = str(os.getenv("SECRET"))

class Services():
    def __init__(self):
        pass

    @staticmethod
    def login(data_base: MYSQL_CONNECTOR, usuario: Usuario):
        user_exist = usuario.has_existence(data_base)

        if not user_exist: return "El usuario no existe"

        consulta = """ SELECT 
            CAST(AES_DECRYPT(contrasena, %s) AS CHAR) AS decrypted_contrasena 
            FROM usuario where correo = %s and estatus = 1"""
        data = data_base.select_queries(consulta, secret, usuario.correo)
        info_user = usuario.get_info_by_mail(data_base)

        if data[0]["decrypted_contrasena"] != usuario._contrasena: 
            return {"estatus": 0, "result": {
            "message": f"Error en las credenciales",
            "user_id": 0,
            "tipo_usuario": 0
        }}
            
        return {"estatus": 1, "result": {
            "message": f"Bienvenido {info_user['result']['data'][0]["nombre_completo"]}",
            "user_id": info_user['result']['data'][0]['id'],
            "tipo_usuario": info_user['result']['data'][0]['tipo_usuario']
        }}

if __name__ == "__main__":
    user = os.getenv("USER")
    password = os.getenv("PASS")
    host = os.getenv("HOST")
    db = os.getenv("DB")

    dataBase = MYSQL_CONNECTOR(user, password, host, db)
    usuario1: Usuario = Usuario("basn160603@gmail.com", "Cpapu")
    print(Services.login(dataBase, usuario1))