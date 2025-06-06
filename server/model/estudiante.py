# Mandamos a llamar a nuestras clases que necesitaremos
from model.bd import MYSQL_CONNECTOR
from model.usuarios import Usuario
# Librerias para leer nuestras varaibles de entorno
import os
from dotenv import load_dotenv
# Cargamos las variables de entorno
load_dotenv()
# Obtenemos el secreto con el cual encriptamos la contraseña
secret = str(os.getenv("SECRET"))
# Creamos nuestra clase estudiante que hereda los datos de usuarios
class Estudiante(Usuario):
    # Inicializamos nuestro objeto y le pasamos los atributos que necesita de su clase padre
    def __init__(self, correo, contrasena):
        # Inicializamos la clase padre
        super().__init__(correo, contrasena)
    # Metodo para crear al usuario de tipo estudiante
    def create(self, data_base: MYSQL_CONNECTOR, name: str, lastname: str, user_type:int, curp: str) -> dict:
        # Verificamos que el usuario exista
        is_user_exist = self.has_existence(data_base)
        # En caos de que exista retornaremos la respuesta de que ya existe un usuario con el correo
        if is_user_exist:
            return {"estatus": 0, "message": "El correo se utiliza para otra cuenta"}
        # Llamamos al metodo de la clase padre para crear al usuario
        usuario_insert = super().create(data_base, name, lastname, user_type)
    # En caso de que de cero retornamos la respuesta del metodo anterior
        if usuario_insert["estatus"] == 0:
            return usuario_insert
        # En caos contrario realizaremos otra consulta en este caso otro insert pero a la tabla correspondiente
        # de los estudiantes
        estudiante_insert = f"""
                        INSERT INTO estudiante (id_usuario, curp)
                        values
                        (%s, %s);
                        """
        # llamamos al metodo de la clase base de datos
        data_base.other_queries(estudiante_insert, usuario_insert["last_insert_id"], curp)
        # Retornamos la repsuesta del objeto estatus 1 y el mensaje que el estudiante se ha creado
        return {"estatus": 1, "message": "Se ha creado el usuario de manera exitosa"}
    # Metodo estatico encargado de brindarnos la información del usuario
    @staticmethod
    def get_info(data_base: MYSQL_CONNECTOR, user_id: int) -> dict:
        # Del objeto usuario obtenemos sus datos
        user_info = Usuario.get_info(data_base, user_id)
        if user_info["estatus"] == 0:
            return user_info
        # Obteneomos el curp desde la tabla estudiante con el id del usuario
        consulta = f"select * from estudiante where id_usuario = %s"
        # Utilizamos el metodo de la clase base de datos para los select
        student_info = data_base.select_queries(consulta, user_id)
        # Retornamos un diccionario con el estatus 1 dando a entender que todo esta bien
        return { "estatus": 1, "result": {
            "message": "Información de estudiante",
                "data": user_info["result"]["data"] | student_info[0]
        }}

# Pruebas realizadas para verificar el correcto funcionamiento de nuestra clase
if __name__ == "__main__":
    user = os.getenv("USER")
    password = os.getenv("PASS")
    host = os.getenv("HOST")
    db = os.getenv("DB")

    dataBase = MYSQL_CONNECTOR(user, password, host, db)
    estudiante: Estudiante = Estudiante("basn160603@gmail.com", "C_papu")
    #print(estudiante.create(dataBase, "Iván", "Soto", 1, "BASN030616HTSLTSA2"))
    print(Estudiante.get_info(dataBase, 1))