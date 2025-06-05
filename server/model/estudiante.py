from model.bd import MYSQL_CONNECTOR
from model.usuarios import Usuario
import os
from dotenv import load_dotenv
load_dotenv()
secret = str(os.getenv("SECRET"))

class Estudiante(Usuario):
    def __init__(self, correo, contrasena):
        super().__init__(correo, contrasena)

    def create(self, data_base: MYSQL_CONNECTOR, name: str, lastname: str, user_type:int, curp: str) -> dict:
        is_user_exist = self.has_existence(data_base)

        if is_user_exist:
            return {"estatus": 0, "message": "El correo se utiliza para otra cuenta"}

        usuario_insert = super().create(data_base, name, lastname, user_type)

        if usuario_insert["estatus"] == 0:
            return usuario_insert

        estudiante_insert = f"""
                        INSERT INTO estudiante (id_usuario, curp)
                        values
                        (%s, %s);
                        """

        data_base.other_queries(estudiante_insert, usuario_insert["last_insert_id"], curp)

        return {"estatus": 1, "message": "Se ha creado el usuario de manera exitosa"}

    @staticmethod
    def get_info(data_base: MYSQL_CONNECTOR, user_id: int) -> dict:
        user_info = Usuario.get_info(data_base, user_id)
        if user_info["estatus"] == 0:
            return user_info

        consulta = f"select * from estudiante where id_usuario = %s"
        student_info = data_base.select_queries(consulta, user_id)
        #print( user_info["result"]["data"][0] |  student_info[0])
        return { "estatus": 1, "result": {
            "message": "Información de estudiante",
                "data": user_info["result"]["data"] | student_info[0]
        }}

if __name__ == "__main__":
    user = os.getenv("USER")
    password = os.getenv("PASS")
    host = os.getenv("HOST")
    db = os.getenv("DB")

    dataBase = MYSQL_CONNECTOR(user, password, host, db)
    estudiante: Estudiante = Estudiante("basn160603@gmail.com", "C_papu")
    #print(estudiante.create(dataBase, "Iván", "Soto", 1, "BASN030616HTSLTSA2"))
    print(Estudiante.get_info(dataBase, 1))