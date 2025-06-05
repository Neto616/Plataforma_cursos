from dns.e164 import query

from model.bd import MYSQL_CONNECTOR

import os
from dotenv import load_dotenv
load_dotenv()
secret = str(os.getenv("SECRET"))

class Usuario:
    def __init__(self, correo, contrasena):
        self.correo = correo
        self._contrasena = contrasena

    def __str__(self):
        return f"Los datos del usuario son: \nCorreo: {self.correo}\nContraseña: {self._contrasena}"

    def _has_existence(self, data_base: MYSQL_CONNECTOR) -> bool:
        consulta = f"""SELECT 1 FROM usuario where correo = %s and estatus = 1"""
        db_response = data_base.select_queries(consulta, self.correo)
        return len(db_response) > 0

    def create(self, data_base: MYSQL_CONNECTOR, name: str, lastname: str, user_type:int) -> str:
        is_user_exist = self._has_existence(data_base)

        if is_user_exist: return "El usuario existe"

        consulta = f"""
        INSERT INTO usuario (correo, contrasena, nombre, apellido, tipo_usuario, estatus)
        values
        (%s, AES_ENCRYPT(%s, '{secret}'), %s, %s, %s, 1);
        """

        data_base.other_queries(consulta, self.correo, self._contrasena, name, lastname, user_type)
        return "El usuario se ha creado de manera exitosa"

    def update_data(self, data_base: MYSQL_CONNECTOR, user_id: int, new_name: str, new_lastname: str):
        if not Usuario._has_existence_by_id(data_base, user_id): return "El usuario no existe"

        consulta = """update usuario
            set nombre = %s,
            apellido = %s
            where id = %s
        """

        data_base.other_queries(consulta, new_name, new_lastname, user_id)
        return "Se ha actualizado la información del usuario"

    @staticmethod
    def _has_existence_by_id(data_base: MYSQL_CONNECTOR, user_id: int):
        consulta = f"""SELECT 1 FROM usuario where id = %s and estatus = 1"""
        db_response = data_base.select_queries(consulta, user_id)
        return len(db_response) > 0

    @staticmethod
    def delete(data_base: MYSQL_CONNECTOR, user_id: int):
        if not Usuario._has_existence_by_id(data_base, user_id): return "El usuario no existe"

        consulta = f"""update usuario set estatus = 0 where id = %s"""
        data_base.other_queries(consulta, user_id)
        return "Se ha eliminado el usuario de manera correcta"


if __name__ == "__main__":
    load_dotenv()
    user = os.getenv("USER")
    password = os.getenv("PASS")
    host = os.getenv("HOST")
    db = os.getenv("DB")

    dataBase = MYSQL_CONNECTOR(user, password, host, db)
    usuario1: Usuario = Usuario("basn160603@gmail.com", "Cpapu")
    print(usuario1._has_existence(dataBase))
    print(usuario1.create(dataBase, "Néstor", "Balderas", 1))
    print(usuario1.delete(dataBase,  3))
