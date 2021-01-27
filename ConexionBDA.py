import sqlite3
DATABASE_NAME = "BDD.db"

def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

conexion=sqlite3.connect("BDD.db")
try: 
    conexion.execute("""
                        create table imc (
                            id integer primary key autoincrement,
                            nombre text,
                            edad numeric,
                            estatura real,
                            resultado integer
                        )
                     """)
    print("Se creo la tabla de imc")
except sqlite3.OperationalError:
    print("La tabla imc ya existe")
conexion.close()
