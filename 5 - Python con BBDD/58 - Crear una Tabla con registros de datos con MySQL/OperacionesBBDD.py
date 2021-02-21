# Importamos el módulo "conexion_bbdd" creado anteriormente en el archivo "conexion.py" donde se realiza la conexión a
# la BBDD.
from Conexion import conexion_bbdd

# Se realiza la conexión entre nuestro archivo y la BBDD MySQL creada.
w_conexion_bbdd = conexion_bbdd()

# Se utiliza el método "cursor" del objeto de conexión "w_conexion" para así poder realizar sentencias en la BBDD.
# Este método devuelve un objeto por lo que se guarda en el objeto "w_cursor".
w_cursor = w_conexion_bbdd.cursor()

# Se realiza la sentencia de crea la tabla de usuarios en MySQL y se guarda en una variable.
w_sentencia_sql = "CREATE TABLE usuarios (id        INTEGER(10) PRIMARY KEY, " \
                                         "email     VARCHAR(250) NOT NULL, " \
                                         "password  VARCHAR(250) NOT NULL)"

# El método "execute" del objeto cursor, prepara la BBDD y ejecuta la sentencia SQL que se indice como parámetro.
# En este caso, va a ejecutar la creación de la tabla de usuarios.
w_cursor.execute(w_sentencia_sql)

# Se inserta 2 registros en la tabla Usuarios y se comita la inserción.
w_sql1 = "INSERT INTO usuarios VALUES (1, 'juan@gmail.com', 'ju@N')"
w_cursor.execute(w_sql1)
w_sql2 = "INSERT INTO usuarios VALUES (2, 'alfonso@gmail.com', 'al@g')"
w_cursor.execute(w_sql2)
w_conexion_bbdd.commit()

# Se consulta todos los registros de la tabla usuario y se muestra por consola.
w_sql = "SELECT * FROM usuarios"
w_cursor.execute(w_sql)
w_datos_usuarios = w_cursor.fetchall()

for r_datos_usuarios in w_datos_usuarios:
    print(r_datos_usuarios)

# Se cierra el cursor.
w_cursor.close()

# Se cierra la conexión a la BBDD.
w_conexion_bbdd.close()