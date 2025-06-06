# Importamos nuestra clase encargada de conectarse a base de datos
from model.bd import MYSQL_CONNECTOR
# Importamos las librerias necesarias para leer archivos del sistema
import os
# Leemos nuestras variables de entorno
from dotenv import load_dotenv
load_dotenv()
# Obtenemos el secreto coon el que encriptamos las contraseñas de nuestros usuarios
secret = str(os.getenv("SECRET"))
# Creamos nuestra clase usuario
class Usuario:
    # Metodo constructor de la clase
    def __init__(self, correo, contrasena):
        self.correo = correo
        self._contrasena = contrasena
    # Metodo que nos sirve para imprimir los datos del objeto
    def __str__(self):
        return f"Los datos del usuario son: \nCorreo: {self.correo}\nContraseña: {self._contrasena}"
    # Metodo para verificar la existencia de un usuario retorna un valor booleano
    def has_existence(self, data_base: MYSQL_CONNECTOR) -> bool:
        # Escibimos nuestra consulta
        consulta = f"""SELECT 1 FROM usuario where correo = %s and estatus = 1"""
        # Realizamos la peticion a la base de datos
        db_response = data_base.select_queries(consulta, self.correo)
        # retornamos un valor booleano dependiendo la longitud del arreglo de la respuesta
        return len(db_response) > 0
    # Metodo que nos regresa la inforamción del usuairo en base a su correo
    # retorna un diccionario
    def get_info_by_mail(self, data_base: MYSQL_CONNECTOR) -> dict:
        # Usamos el metodo para verificar que el usuario si existe en el sistema y en caso de existir
        # retornamos un cero 
        if not self.has_existence(data_base): return {"estatus": 0, "result": {
            "message": "El usuario no existe",
            "data": []
        }}
        # caso contrario escribimos nuestra consulta
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
        # Realizamos la peticion a la base de datos
        data = data_base.select_queries(consulta, self.correo)
        # retornamos un 1 y la inforamción que obtuvimos de base de datos
        return {"estatus": 1, "result": {
            "message": "Información del usuario",
            "data": data
        }}
    # Metodo para crear al usuario
    # Recibe como parametros el objeto de base de datos, nombre, apellido y demas datos necesarios
    def create(self, data_base: MYSQL_CONNECTOR, name: str, lastname: str, user_type:int) -> dict:
        # Verificamos si el usuario existe o no
        is_user_exist = self.has_existence(data_base)
        # En caos de existir se notifica que ya existe un usuario con las credenciales
        if is_user_exist: return {"estatus": 0, "message": "El correo se utiliza para otra cuenta"}
        # Escribimos la consulta
        consulta = f"""
        INSERT INTO usuario (correo, contrasena, nombre, apellido, tipo_usuario, estatus)
        values
        (%s, AES_ENCRYPT(%s, '{secret}'), %s, %s, %s, 1);
        """
        # Realizamos la consulta
        insertion = data_base.other_queries(consulta, self.correo, self._contrasena, name, lastname, user_type)
        # Retornamos nuestro estatus 1 y el mensaje de que se ha creado con exito nuestro usuario
        return {"estatus": 1, "message": "Se ha creado el usuario de manera exitosa", "last_insert_id": insertion["last_insert_id"]}
    # Metodo para actualizar la información del usuario
    def update_data(self, data_base: MYSQL_CONNECTOR, user_id: int, new_name: str, new_lastname: str):
        # Verificamos primero que el usuario exista por medio de su ID
        if not Usuario.has_existence_by_id(data_base, user_id): return {"estatus": 0, "message": "El usuario no existe"}
        # Escribimos nuestra consulta
        consulta = """update usuario
            set nombre = %s,
            apellido = %s
            where id = %s
        """
        # Realizamos la peticion
        data_base.other_queries(consulta, new_name, new_lastname, user_id)
        # Retornamos un estatus 1 y el mensaje de que se ha actualizado el usario
        return {"estatus": 1, "message": "Se ha actualizado la información del usuario"}
    # Metodo estatico para saber si el usuario existe por medio de su ID
    @staticmethod
    def has_existence_by_id(data_base: MYSQL_CONNECTOR, user_id: int):
        # Escribimos la consulta
        consulta = f"""SELECT 1 FROM usuario where id = %s and estatus = 1"""
        # Realizamos nuestra consulta a base de datos
        db_response = data_base.select_queries(consulta, user_id)
        # Dependiendo del tamaño del arreglo devolveremos el valor booleano
        return len(db_response) > 0
    # Metodo estatico para obtener la información del usuario
    @staticmethod
    def get_info(data_base: MYSQL_CONNECTOR, user_id: int) -> dict:
        # Si el usuario no existe retornamo un estado de cero
        if not Usuario.has_existence_by_id(data_base, user_id): return {"estatus": 0, "result": {
            "message": "El usuario no existe",
            "data": []
        }}
        # Escribimos nuestra consulta
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
        # Realizamos la peticion a base de datos
        data = data_base.select_queries(consulta, user_id)
        # Retornamos un estatus de 1 y los datos obtenidos
        return { "estatus": 1, "result": {
            "message": "Información del usuario",
            "data": data[0]
        }}
    # Metodo estatico para "eliminar" a un usuario
    @staticmethod
    def delete(data_base: MYSQL_CONNECTOR, user_id: int):
        # En caos de que no exista el usuario retornamo un 0
        if not Usuario.has_existence_by_id(data_base, user_id): return {"estatus": 0, "message": "El usuario no existe"}
        # Escribimos la consulta el borrado del usuario sera un borrado logico
        consulta = f"""update usuario set estatus = 0 where id = %s"""
        # Realizamos nuestra consulta
        data_base.other_queries(consulta, user_id)
        # Retornamos un estatus de 1 y el mensaje de que se elimino de manera correcta el usuario
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