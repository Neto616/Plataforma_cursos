from model.bd import MYSQL_CONNECTOR

class Curso: 
    def __init__(self, maestro, titulo, portada, id, capitulos = None):
        self.maestro = maestro
        self.titulo = titulo
        self.portada = portada
        self.id = id

    def __str__(self):
        return f"Maestro: {self.maestro}\nTitulo: {self.maestro}\nCapitulos: {"\n".join(self.capitulos)}"
    
    def to_dict(self):
        return {
            "maestro": self.maestro,
            "titulo": self.titulo,
            "portada": self.portada,
            "id": self.id
        }

class Capitulos: 
    def __init__(self, capitulo, url, duracion, descripcion):
        self.capitulo = capitulo
        self.url = url
        self.duracion = duracion
        self.descripcion = descripcion
        
    def to_dict(self):
        return {
            "capitulo": self.capitulo,
            "url": self.url,
            "duracion": self.duracion,
            "descripcion": self.descripcion
        }
        
class CursoService(MYSQL_CONNECTOR):
    def __init__(self, user, password, host, db):
        super().__init__(user, password, host, db)
        
    def obtain_chapter(self, course_id):
        consulta = f"select * from capitulo where estatus = 1 and curso = %s"
        capitulos = super().select_queries(consulta, course_id)
        list_capitulos = [Capitulos(x["capitulo"], x["url_video"], x["duracion"], x["descripcion"]).to_dict() for x in capitulos]
        
        return list_capitulos
        
    def obtain_courses(self):
        consulta = f"select * from curso where estatus = 1"
        cursos = super().select_queries(consulta)
        list_cursos = [Curso(x["maestro"], x["titulo"], x["portada"], x["id"]).to_dict() for x in cursos]
        
        for i in list_cursos:
            i.__str__()
                
        return { "estatus": 1, "result": {
            "message": "Se han traido los cursos que se tienen en base de datos",
            "cursos": list_cursos
        }}
        
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