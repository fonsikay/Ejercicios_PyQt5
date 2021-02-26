# Se importan las librerias necesarias.
import sys
import re

from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QTableWidgetItem
from PyQt5.QtGui import QIcon
from ConsultaDatosProductos import frmConsultaDatos
from Conexion_PHPMyAdmin import conexion_bbdd
from pymysql import Error
from PyQt5 import QtCore


# Se crea la clase Aplicación.
class ConsultaDatosProductos_Aplicacion(QDialog):

    # Se crea el método del constructor inicializador.
    def __init__(self):

        # Se invoca el constructor padre.
        super().__init__()
        # Se crea una instancia de nuestra ventana diseñada.
        self.uiVentana = frmConsultaDatos()
        # Se llama al método "setupUi" que esta en la clase "frmConsultaDatos" del archivo "ConsultaDatosProductos.py".
        self.uiVentana.setupUi(self)
        # Se indica un icono para la ventana principal.
        self.setWindowIcon(QIcon('icono.ico'))
        # Se indica el tamaño de la ventana para que no se pueda modificar su tamaño.
        self.setFixedSize(441, 380)
        # Se muestra la pantalla.
        self.show()

        # Declaración de los controladores de eventos (Event Handler).
        self.uiVentana.btnConsultar.clicked.connect(self.pro_consultar_registros)
        self.uiVentana.btnConectar.clicked.connect(self.pro_conectar_bbdd)

        # Se crea el patrón que permite validar texto.
        # Se indica que se puede escribir desde la "a" hasta la "z" y desde la "A" hasta la "Z" mas de una vez.
        w_patron_texto = '[a-zA-Z]+'
        self.w_validador = re.compile(w_patron_texto)

        # Se crea un objeto de tipo ventana de mensaje.
        self.ventana_mensaje = QMessageBox(self)

        # Se crea la variable de conexión y de cursor para que se pueda utilizar en el programa.
        self.w_conexion = None
        self.w_cursor = None

        # Se desactivan de inicio el campo de texto del nombre de la tabla, el botón de consultar y la tabla.
        self.uiVentana.txtTabla.setEnabled(False)
        self.uiVentana.btnConsultar.setEnabled(False)
        self.uiVentana.tabDatosProductos.setEnabled(False)

    def pro_conectar_bbdd(self):

        # Se crea un bloque de excepciones para controlar los fallos.
        try:

            # Se obtiene el valor del nombre de la BBDD y de la tabla ingresada por pantalla.
            w_nombre_bbdd = self.uiVentana.txtBBDD.text().strip()

            # Si el texto introducido en el campo "Nombre de BBDD" es válido.
            if self.w_validador.match(w_nombre_bbdd) is not None:

                # Si existe la BBDD.
                if self.fun_existe_bbdd(w_nombre_bbdd) == 1:

                    # Se realiza la conexión a la BBDD que se ha indicado.
                    self.w_conexion = conexion_bbdd(w_nombre_bbdd)

                    # Se muestra un mensaje de información al usuario.
                    self.pro_mensaje_informacion('Se ha conectado a la BBDD {} de forma correcta.'.format(w_nombre_bbdd)
                                                 , 'BBDD conectada')

                    # Se desactiva el campo de texto de la BBDD y el botón Conectar.
                    self.uiVentana.txtBBDD.setEnabled(False)
                    self.uiVentana.btnConectar.setEnabled(False)

                    # Se activan el campo de texto de la tabla y el botón Consultar.
                    self.uiVentana.txtTabla.setEnabled(True)
                    self.uiVentana.btnConsultar.setEnabled(True)
                    self.uiVentana.tabDatosProductos.setEnabled(True)
                    self.uiVentana.txtTabla.setFocus()

                # Si la consulta no ha recuperado datos, es que no existe la BBDD indicada y se informa por
                # pantalla.
                else:

                    self.pro_mensaje_error('La Base de datos {} no existe.'.format(w_nombre_bbdd), 'No existe la BBDD')

                    self.uiVentana.txtBBDD.setText('')
                    self.uiVentana.txtBBDD.setFocus()

            # Si se inicia el nombre de la BBDD con números, se muestra un mensaje de error al usuario.
            else:

                self.pro_mensaje_error('El nombre de la BBDD introducida no es válido: {}'.format(w_nombre_bbdd),
                                       'Nombre de BBDD erróneo')

                self.uiVentana.txtBBDD.setText('')
                self.uiVentana.txtBBDD.setFocus()

        # Si se ha producido un error en la conexión a la BBDD, se muestra un mensaje de error.
        except Error as w_error:

            self.pro_mensaje_error('Error Conexión: {}'.format(w_error), 'Error de conexión')

            self.uiVentana.txtBBDD.setText('')
            self.uiVentana.txtBBDD.setFocus()

    # Se crea el método que se lanza cuando se pulsa el botón "Consultar".
    def pro_consultar_registros(self):

        # Se obtiene el valor del nombre de la BBDD y de la tabla ingresada por pantalla.
        w_nombre_bbdd = self.uiVentana.txtBBDD.text().strip()
        # Se obtiene el valor del nombre de la tabla ingresada por pantalla.
        w_nombre_tabla = self.uiVentana.txtTabla.text().strip()

        # Se comprueba si el nombre de la tabla cumple el patrón de la expresión regular que comprueba
        # que el nombre sólo comience por letra.
        if self.w_validador.match(w_nombre_tabla) is not None:

            # Se comprueba si la tabla indicada existe en la BBDD indicada utilizando el método "existe_
            # tabla()".
            # Si ha recuperado registro, existe la tabla en la BBDD.
            if self.fun_existe_tabla(w_nombre_bbdd, w_nombre_tabla) == 1:

                # Se lanza el método "pro_obtener_datos()" para obtener los datos y cargarlos en la tabla.
                self.pro_obtener_datos(w_nombre_bbdd, w_nombre_tabla)

            # Si la tabla no existe en la BBDD indicada, pues se muestra un mensaje de error al usuario.
            else:

                self.pro_mensaje_error('La tabla {} no existe en la BBDD.'.format(w_nombre_tabla),
                                       'Tabla inexistente')

                # Se limpian los registros para indicar uno nuevo.
                self.uiVentana.txtTabla.setText('')
                self.uiVentana.txtTabla.setFocus()
                # Se indica los nº de columnas y filas iniciales y se limpia de registros la tabla.
                self.uiVentana.tabDatosProductos.setRowCount(6)
                self.uiVentana.tabDatosProductos.setColumnCount(2)
                self.uiVentana.tabDatosProductos.clear()

        # Si la tabla indicada es errónea o esta en campo vacío, se muestra un mensaje de error al usuario.
        else:

            self.pro_mensaje_error('El nombre de la tabla no es válida: {}'.format(w_nombre_tabla),
                                   'Tabla no válida')

            # Se limpian los registros para indicar uno nuevo.
            self.uiVentana.txtTabla.setText('')
            self.uiVentana.txtTabla.setFocus()

            # Se indica los nº de columnas y filas iniciales y se limpia de registros la tabla.
            self.uiVentana.tabDatosProductos.setRowCount(6)
            self.uiVentana.tabDatosProductos.setColumnCount(2)
            self.uiVentana.tabDatosProductos.clear()

    # Se crea el método para comprobar si existe la BBDD en MySQL.
    def fun_existe_bbdd(self, w_nombre_bbdd):

        # Como no tenemos forma de acceder a una BBDD de administrador, pues nos conectamos primero a nuestra
        # BBDD y comprobamos si esa base de datos existe con la consulta indicada filtrando por la BBDD que
        # se ha indicado en el formulario.
        w_conexion_bbdd = conexion_bbdd('phpmyadmin')
        w_cursor_bbdd = w_conexion_bbdd.cursor()
        w_sentencia = '''(SELECT * FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '{}')'''.format(w_nombre_bbdd)
        w_cursor_bbdd.execute(w_sentencia)
        w_resultado_sql = w_cursor_bbdd.fetchall()

        # Si la consulta ha recuperado un registro.
        if w_resultado_sql:

            # Se retorna un 1 para indicar que existe un registro ya dado de alta.
            w_cursor_bbdd.close()
            return 1
        # Si la consulta no ha recuperado registros.
        else:

            # Se retorna un 0 para indicar que no existe el registro dado de alta.
            w_cursor_bbdd.close()
            return 0

    # Se crea el método para comprobar si ya existe la tabla en la BBDD.
    def fun_existe_tabla(self, w_nombre_bbdd, w_nombre_tabla):

        # Se comprueba si la tabla indicada existe en la BBDD indicada.
        w_cursor_tabla = self.w_conexion.cursor()
        w_sentencia = '''(SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = '{}' AND TABLE_NAME = 
                                        '{}')'''.format(w_nombre_bbdd, w_nombre_tabla)
        w_cursor_tabla.execute(w_sentencia)
        w_resultado_sql = w_cursor_tabla.fetchall()

        # Si la consulta ha recuperado un registro.
        if w_resultado_sql:

            # Se retorna un 1 para indicar que existe un registro ya dado de alta.
            w_cursor_tabla.close()
            return 1
        # Si la consulta no ha recuperado registros.
        else:

            # Se retorna un 0 para indicar que no existe el registro dado de alta.
            w_cursor_tabla.close()
            return 0

    # Se crea el método "pro_obtener_datos()" para cargar en la tabla los datos de la tabla indicada.
    def pro_obtener_datos(self, w_nombre_bbdd, w_nombre_tabla):

        # Se obtiene todos los registros de la tabla indicada.
        w_cursor_reg = self.w_conexion.cursor()
        w_sentencia = '''SELECT * FROM {}.{}'''.format(w_nombre_bbdd, w_nombre_tabla)
        w_cursor_reg.execute(w_sentencia)
        w_registros_tabla = w_cursor_reg.fetchall()

        # Se indica que se creen tantos registros como haya recuperado la consulta.
        self.uiVentana.tabDatosProductos.setRowCount(len(w_registros_tabla))

        # Se llama al método que crea la tabla configurada.
        self.pro_creacion_tabla(w_nombre_bbdd, w_nombre_tabla)

        # Si se ha recuperado datos.
        if len(w_registros_tabla) > 0:

            # Se crea una variable para almacenar la fila de la tabla.
            w_fila = 0

            # Se recorre las filas recuperadas.
            for r_fila_registros in w_registros_tabla:

                # Se crea una variable para almacenar la columna de la tabla.
                w_columna = 0

                # Se recorren las columnas de cada una de las filas.
                for r_columna_registro in r_fila_registros:

                    # Se crea una variable para almacenar cada uno de los valores de la tabla.
                    # Importante, se debe de añadir el método "str()" a la variable para que recupere los datos.
                    w_registro = QTableWidgetItem(str(r_columna_registro))
                    # Se añade cada uno de los datos a la tabla indicando la fila, columna y el dato.
                    self.uiVentana.tabDatosProductos.setItem(w_fila, w_columna, w_registro)
                    # Se aumenta el contador de columnas.
                    w_columna = w_columna + 1

                # Se aumenta el contador de filas.
                w_fila = w_fila + 1

        # Si no se ha recuperado registros de la tabla, pues se muestra un mensaje de información al usuario.
        else:

            self.pro_mensaje_informacion('La tabla {} no tiene registros.'.format(w_nombre_tabla),
                                         'Tabla sin registros')

            # Se indica los nº de columnas y filas iniciales y se limpia de registros la tabla.
            self.uiVentana.tabDatosProductos.setRowCount(6)
            self.uiVentana.tabDatosProductos.setColumnCount(2)
            self.uiVentana.tabDatosProductos.clear()

    # Se crea el método para cargar la estructura de la tabla de datos a mostrar.
    def pro_creacion_tabla(self, w_nombre_bbdd, w_nombre_tabla):

        # Se obtiene el nº de columnas que tiene la tabla.
        w_cursor_col = self.w_conexion.cursor()
        w_sentencia2 = '''(SELECT COUNT(*) FROM Information_Schema.Columns WHERE Table_Schema = '{}' AND Table_Name = 
                       '{}')'''.format(w_nombre_bbdd, w_nombre_tabla)
        w_cursor_col.execute(w_sentencia2)
        w_num_column = w_cursor_col.fetchall()

        # Se obtiene el nombre de cada una de columnas que tiene la tabla.
        w_cursor_nom_col = self.w_conexion.cursor()
        w_sentencia3 = '''(SELECT UPPER(column_name) FROM Information_Schema.Columns WHERE Table_Schema = '{}' 
                        AND Table_Name = '{}')'''.format(w_nombre_bbdd, w_nombre_tabla)
        w_cursor_nom_col.execute(w_sentencia3)
        w_nombre_columnas = w_cursor_nom_col.fetchall()

        # Se crea una variable para almacenar las filas de la tabla.
        w_contador_fila = 0
        # Se crea una lista porque el método "setHorizontalHeaderLabels()" necesita una lista con todos los nombres de
        # los campos para mostrarlos como titulo de cada campo.
        w_lista_nombre_columnas = []

        # Se recorre las filas recuperadas.
        for r_nombre_columnas in w_nombre_columnas:

            # Se crea una variable para almacenar la columna de la tabla.
            w_contador_columna = 0

            # Se recorren las columnas de cada una de las filas.
            for r_nombre_columnas_datos in r_nombre_columnas:

                # Se crea una variable para almacenar cada uno de los valores de la tabla.
                # Importante, se debe de añadir el método "str()" a la variable para que recupere los datos.
                w_nombre_columnas_registro = QTableWidgetItem(str(r_nombre_columnas_datos))

                # Se obtiene el texto de cada uno de los elementos para añadirlos a la lista.
                w_lista_nombre_columnas.append(w_nombre_columnas_registro.text())

                # Se aumenta el contador de columnas.
                w_contador_columna = w_contador_columna + 1

                # Se aumenta el contador de filas.
            w_contador_fila = w_contador_fila + 1

        # Se indica que se creen tantas columnas como tenga la tabla. Para ello se debe de obtener el valor [0][0] de
        # una matriz
        self.uiVentana.tabDatosProductos.setColumnCount(w_num_column[0][0])

        # Indicamos los titulos de cada uno de las columnas de la tabla consultada que estan almacenadas en la lista.
        self.uiVentana.tabDatosProductos.setHorizontalHeaderLabels(w_lista_nombre_columnas)
        # Indicamos que se muestre los titulos de los campos.
        self.uiVentana.tabDatosProductos.horizontalHeader().setVisible(True)
        # Indicamos que se muestre los titulos de los campos de forma centrada.
        self.uiVentana.tabDatosProductos.verticalHeader().setDefaultAlignment(QtCore.Qt.AlignHCenter)
        # Indicamos que se pueda ordenar por la columna seleccionada.
        self.uiVentana.tabDatosProductos.setSortingEnabled(True)

    # Se crea un método para mostrar por pantalla un mensaje personalizado de tipo información.
    def pro_mensaje_informacion(self, w_mensaje, w_titulo):

        self.ventana_mensaje.setText(w_mensaje)
        self.ventana_mensaje.setIcon(QMessageBox.Information)
        self.ventana_mensaje.setWindowTitle(w_titulo)
        self.ventana_mensaje.exec_()

    # Se crea un método para mostrar por pantalla un mensaje personalizado de tipo error.
    def pro_mensaje_error(self, w_mensaje, w_titulo):

        self.ventana_mensaje.setText(w_mensaje)
        self.ventana_mensaje.setIcon(QMessageBox.Critical)
        self.ventana_mensaje.setWindowTitle(w_titulo)
        self.ventana_mensaje.exec_()


# Hacemos referencia al módulo principal de la aplicación.
if __name__ == '__main__':

    # Creamos una aplicación de nuestra ventana.
    app = QApplication(sys.argv)
    # Creamos una instancia de la clase "ConsultaDatosProductos_Aplicacion()".
    ventana = ConsultaDatosProductos_Aplicacion()
    # Se muestra la pantalla.
    ventana.show()
    # Se indica el método para que cierre la aplicación al pulsar el botón de cerrar.
    sys.exit(app.exec_())
