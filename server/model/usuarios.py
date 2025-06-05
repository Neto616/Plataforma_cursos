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

    def has_existence(self, data_base: MYSQL_CONNECTOR) -> bool:
        consulta = f"""SELECT 1 FROM usuario where correo = %s and estatus = 1"""
        db_response = data_base.select_queries(consulta, self.correo)
        return len(db_response) > 0

    def get_info_by_mail(self, data_base: MYSQL_CONNECTOR) -> dict:
        if not self.has_existence(data_base): return {"estatus": 0, "result": {
            "message": "El usuario no existe",
            "data": []
        }}

        consulta = """
        select 
            u.id,
    	    u.nombre,
    	    u.apellido,
            concat(u.nombre, " ", u.apellido) as nombre_completo,
	        u.correo,
    	    tu.nombre as tipo_usuario
        from usuario u
        inner join tipo_usuario tu on u.tipo_usuario = tu.id
        where u.correo = %s and u.estatus = 1; 
        """
        data = data_base.select_queries(consulta, self.correo)
        #print(f"Datos obtenidos de la base de datos: {data}")
        return {"estatus": 1, "result": {
            "message": "Información del usuario",
            "data": data
        }}

    def create(self, data_base: MYSQL_CONNECTOR, name: str, lastname: str, user_type:int) -> dict:
        is_user_exist = self.has_existence(data_base)

        if is_user_exist: return {"estatus": 0, "message": "El correo se utiliza para otra cuenta"}

        consulta = f"""
        INSERT INTO usuario (correo, contrasena, nombre, apellido, tipo_usuario, estatus)
        values
        (%s, AES_ENCRYPT(%s, '{secret}'), %s, %s, %s, 1);
        """

        insertion = data_base.other_queries(consulta, self.correo, self._contrasena, name, lastname, user_type)
        return {"estatus": 1, "message": "Se ha creado el usuario de manera exitosa", "last_insert_id": insertion["last_insert_id"]}

    def update_data(self, data_base: MYSQL_CONNECTOR, user_id: int, new_name: str, new_lastname: str):
        if not Usuario.has_existence_by_id(data_base, user_id): return {"estatus": 0, "message": "El usuario no existe"}

        consulta = """update usuario
            set nombre = %s,
            apellido = %s
            where id = %s
        """

        data_base.other_queries(consulta, new_name, new_lastname, user_id)
        return {"estatus": 1, "message": "Se ha actualizado la información del usuario"}

    @staticmethod
    def has_existence_by_id(data_base: MYSQL_CONNECTOR, user_id: int):
        consulta = f"""SELECT 1 FROM usuario where id = %s and estatus = 1"""
        db_response = data_base.select_queries(consulta, user_id)
        return len(db_response) > 0

    @staticmethod
    def get_info(data_base: MYSQL_CONNECTOR, user_id: int) -> dict:
        if not Usuario.has_existence_by_id(data_base, user_id): return {"estatus": 0, "result": {
            "message": "El usuario no existe",
            "data": []
        }}

        consulta = """
        select 
            u.id,
	        u.nombre,
	        u.apellido,
	        concat(u.nombre, " ", u.apellido) as nombre_completo,
	        u.correo,
	        tu.nombre as tipo_usuario
        from usuario u
        inner join tipo_usuario tu on u.tipo_usuario = tu.id
        where u.id = %s; 
        """
        data = data_base.select_queries(consulta, user_id)

        return { "estatus": 1, "result": {
            "message": "Información del usuario",
            "data": data[0]
        }}

    @staticmethod
    def delete(data_base: MYSQL_CONNECTOR, user_id: int):
        if not Usuario.has_existence_by_id(data_base, user_id): return {"estatus": 0, "message": "El usuario no existe"}

        consulta = f"""update usuario set estatus = 0 where id = %s"""
        data_base.other_queries(consulta, user_id)
        return {"estatus": 1, "message": "Se ha eliminado el usuario de manera correcta"}


if __name__ == "__main__":
    user = os.getenv("USER")
    password = os.getenv("PASS")
    host = os.getenv("HOST")
    db = os.getenv("DB")

    dataBase = MYSQL_CONNECTOR(user, password, host, db)
    usuario1: Usuario = Usuario("basn160603@gmail.com", "Cpapu")
    # print(usuario1.has_existence(dataBase))
    # print(usuario1.create(dataBase, "Néstor", "Balderas", 1))
    # print(usuario1.delete(dataBase,  3))
    print(usuario1.get_info_by_mail(dataBase))