# Se importa la libreria necesaria llamada "pymysql".
import pymysql


# Se crea un metodo que que llame "obtenerConexion" que realice la función de conectarse a la BBDD que se indique por
# parámetro en la llamada.
def conexion_bbdd(w_nombre_bbdd):

    # Se crea un objeto constructor de conexión de BBDD utilizando la libreria "pymysql" para crear la conexión a la
    # base de datos y se utiliza el módulo "connect" y va a retornar un objeto de conexión por lo que asignamos el
    # constructor al objeto "w_conexion". Se pasa a este método los siguientes parámetros:

    # host: Nombre del dominio de la BBDD.
    # user: Usuario de la BBDD.
    # password: Password del usuario de BBDD.
    # database: Nombre de la BBDD.

    # Se declara el Objeto de conexión a la BBDD con los parámetros necesarios para conectarse a nuestra BBDD MySQL.

    w_conexion = pymysql.connect(host="localhost",
                                 user="root",
                                 password="",
                                 database=w_nombre_bbdd
                                 )

    # Se devuelve el objeto de conexión.

    return w_conexion
