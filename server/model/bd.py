# Importamos de la libreria mysql el connector para poder conectarnos a la base de datos
import mysql.connector

# Creamos nuestra clase encargada de manejar la solcitud de base de datos
class MYSQL_CONNECTOR:
    # Creamos nuestra función para inicializar nuestra clase con los datos que necesitamos
    # Requerimos los datos necesarios para la conexión a base de datos
    def __init__(self, user, password, host, db):
        self._user = user
        self._password = password
        self._host = host
        self._db = db
    # metodo para visualizar los atributos de nuestro objeto
    def __str__(self):
        return f"USUARIO: {self._user}\nPASSWORD: {self._password}\nHOST: {self._host}\nDB: {self._db}"
    # Metodo "privado" para realizar la conexión a base de datos
    def _connection(self):
        return mysql.connector.connect(
            user=self._user,
            password=self._password,
            host=self._host,
            database=self._db
        )
    # Metodo que nos permite realizar INSERTS, UPDATES O DELETES
    # recibe de parametros la consulta a realizar y N parametros que llegaran en formato de tupla
    def other_queries(self, query, *params):
        # Realizamos la conexion a base de datos
        connection = self._connection()
        # Encapsulamos todo en un try except para controlar los errores
        try:
            # Inicializamos nuestro cursor para la base de datos y decimos que la respuesta nos la de en formato de diccionario
            cursor = connection.cursor(dictionary=True)
            # Ejecutamos la consulta con los parametros que requiera
            cursor.execute(query, params)
            # Aceptamos los cambios a realizar
            connection.commit()
            # Retornamos las columnas afectadas y las id que fueron afectadas
            return {"rows_affected": cursor.rowcount, "last_insert_id": cursor.lastrowid}
        # En caso de error de mysql tira un error especifico
        except mysql.connector.Error as err:
            print(f"Error al conectar a la base de datos: {err}")
        # En caso de un error general imprimimos en consola dicho error
        except Exception as err:
            print(f"Ha ocurrido un error ❌-❌ {err}")
        # Al final sea todo correcto o un error cerramos la conexión a base de datos
        finally:
            connection.close()
    # Metodo para realizar las peticiones SELECT a base de datos
    # Al igual que el anterior recibe la consulta y N parametros que los recibira en formato de tupla
    def select_queries(self, query, *params):
        # realizamos la conexión a la base de datos
        connection = self._connection()
        # Encapsulamos todo en un try except para controlar los errores
        try:
            # Inicializamos nuestro cursor para la base de datos y decimos que la respuesta nos la de en formato de diccionario
            cursor = connection.cursor(dictionary= True)
            # Ejecutamos nuestra peticion ycon los parametros que requiera
            cursor.execute(query, params)
            # Retornamos todos los resultados que encontro en la consulta
            return cursor.fetchall()
        # En caso de error de mysql tira un error especifico
        except mysql.connector.Error as err:
            print(f"Error al conectar a la base de datos: {err}")
         # En caso de un error general imprimimos en consola dicho error
        except Exception as err:
            print(f"Ha ocurrido un error ❌-❌ {err}")
         # Al final sea todo correcto o un error cerramos la conexión a base de datos
        finally:
            connection.close()

# Pruebas realizadas para verificar el funcionamiento de la clase creda
if __name__ == "__main__":
    import os
    from dotenv import load_dotenv
    load_dotenv()
    user = os.getenv("USER")
    password = os.getenv("PASS")
    host = os.getenv("HOST")
    db = os.getenv("DB")
    dataBase = MYSQL_CONNECTOR(user, password, host, db)
    print(dataBase.__str__())
    try:
        pruebaDb = dataBase.select_queries("SELECT * from usuario")
        for e in pruebaDb:
            print(e)
    except Exception as e:
        print(e)




