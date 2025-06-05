import mysql.connector

class MYSQL_CONNECTOR:
    def __init__(self, user, password, host, db):
        self._user = user
        self._password = password
        self._host = host
        self._db = db

    def __str__(self):
        return f"USUARIO: {self._user}\nPASSWORD: {self._password}\nHOST: {self._host}\nDB: {self._db}"

    def _connection(self):
        return mysql.connector.connect(
            user=self._user,
            password=self._password,
            host=self._host,
            database=self._db
        )

    def other_queries(self, query, *params):
        connection = self._connection()
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute(query, params)
            connection.commit()

            return {"rows_affected": cursor.rowcount, "last_insert_id": cursor.lastrowid}
        except mysql.connector.Error as err:
            print(f"Error al conectar a la base de datos: {err}")
        except Exception as err:
            print(f"Ha ocurrido un error ❌-❌ {err}")
        finally:
            connection.close()

    def select_queries(self, query, *params):
        connection = self._connection()
        try:
            cursor = connection.cursor(dictionary= True)
            cursor.execute(query, params)

            return cursor.fetchall()
        except mysql.connector.Error as err:
            print(f"Error al conectar a la base de datos: {err}")
        except Exception as err:
            print(f"Ha ocurrido un error ❌-❌ {err}")
        finally:
            connection.close()


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




