# Importamos la clase encargada para conectarnos a base de datos
from model.bd import MYSQL_CONNECTOR
# Creamos una clase Curso encargada de almacenar los datos de los cursos y convertirlos 
# a un formato legible para los sitios web
class Curso: 
    # Funcion para inicializar nuestro objeto
    def __init__(self, maestro, titulo, portada, id, capitulos = None):
        self.maestro = maestro
        self.titulo = titulo
        self.portada = portada
        self.id = id
    # Este metodo nos sirve para poder visualizar los atributos que tenga la clase
    def __str__(self):
        return f"Maestro: {self.maestro}\nTitulo: {self.maestro}\nCapitulos: {"\n".join(self.capitulos)}"
    # Metodo que retorna un diccionario con los atributos de nuestra clase
    def to_dict(self):
        return {
            "maestro": self.maestro,
            "titulo": self.titulo,
            "portada": self.portada,
            "id": self.id
        }
# Clase Capitulos encargada de almacenar los datos de los capitulos de un curso
# y de transformarlos a nu formato legible para el sitio web
class Capitulos: 
    # Metodo constructor de la clase
    def __init__(self, capitulo, url, duracion, descripcion):
        self.capitulo = capitulo
        self.url = url
        self.duracion = duracion
        self.descripcion = descripcion
    # Generamos el metodo que retorne un JSON con los atributos de la clase
    def to_dict(self):
        return {
            "capitulo": self.capitulo,
            "url": self.url,
            "duracion": self.duracion,
            "descripcion": self.descripcion
        }
        
# Clase encargada de conectarse a base de datos para realizar las acciones necesarios
# esta clase hereda de MYSQ_CONNECTOR
class CursoService(MYSQL_CONNECTOR):
    # Constructor de nuestra clase que adquiere los atributos de la clase padre
    def __init__(self, user, password, host, db):
        super().__init__(user, password, host, db)
    # Metodo encargado de obtener los capitulos de un curso recibe el id del curso como parametro
    def obtain_chapter(self, course_id):
        # Tenemos la consulta que realiza a base de datos
        consulta = f"select * from capitulo where estatus = 1 and curso = %s"
        # Obtenemos los capitulos llamando al metodo necesario
        capitulos = super().select_queries(consulta, course_id)
        # Enlistamos los capitulos guardandolos en un arreglo 
        list_capitulos = [Capitulos(x["capitulo"], x["url_video"], x["duracion"], x["descripcion"]).to_dict() for x in capitulos]
        # retornamos dicho arreglo
        return list_capitulos
    # Metodo para obtener los cursos que esten en base de datos
    def obtain_courses(self):
        # Creamos nuestra consulta donde queremos traer los cursos con estatus de 1
        consulta = f"select * from curso where estatus = 1"
        # Llamamos al metodo de la clase padre para obtener las consultas
        cursos = super().select_queries(consulta)
        # Creamoss un arreglo con la respuesta de la llamada anterior y lo convertimos n un diccionario
        list_cursos = [Curso(x["maestro"], x["titulo"], x["portada"], x["id"]).to_dict() for x in cursos]
        #  Retornamos una repsuesta legible para el usuario
        return { "estatus": 1, "result": {
            "message": "Se han traido los cursos que se tienen en base de datos",
            "cursos": list_cursos
        }}
    # Metodo para saber si el usuario tiene o no el curso comprado
    def has_course(self, user_id, course_id) -> bool:
        # Creamos nuestra consulta para verificar si el usuario ya tiene o no comprado dicho curso
        consulta = f"select * from curso_estudiante where estudiante = %s and curso = %s;"
        # Llamamos la metodo para realizar la consulta
        cursos = super().select_queries(consulta, user_id, course_id)
        # Retornamos True o False dependiendo
        return len(cursos) > 0
    
    # Metodo para comprar la certificación de un curso
    def buy_course(self, user_id, course_id):
        # En caso de que el metodo anterior de True indica que ese curso ya lo tenemos
        if self.has_course(user_id, course_id): return {"estatus": 0, "result": {
            "message": "El curso ya lo has comprado"
                }
            }
        # Realizamos la consulta que insertara los datos a la bd
        consulta = "insert into curso_estudiante (estudiante, curso, certificado, estatus) values (%s, %s, %s, %s)"
        # Llamamos al metodo correspondiente y le pasamos los datos necesarios
        super().other_queries(consulta, user_id, course_id, 1, 1)
        # Retornamos un estatus de 1 dando a entender que todo estabien 
        return {"estatus": 1, "result": {
            "message": "El certificado se ha comprado"
        }}
        
# Pruebas realizadas para verificar el funcionamiento correcto de la clase recien creada
if __name__ == "__main__":
    import os
    from dotenv import load_dotenv
    load_dotenv()
    
    user = os.getenv("USER")
    password = os.getenv("PASS")
    host = os.getenv("HOST")
    db = os.getenv("DB")
    
    cursos: CursoService = CursoService(user, password, host, db)
    # print(cursos.obtain_courses())
    print(cursos.obtain_chapter(1))