# Se importan las librerias necesarias.
import sys
import re
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5.QtGui import QIcon
from InsertarRegistros import frmInsertarRegistros
from Conexion_MySQL import conexion_bbdd
from pymysql import Error


# Se crea la clase Aplicación.
class InsertarRegistrosMySQL_Aplicacion(QDialog):

    # Se crea el método del constructor inicializador.
    def __init__(self):

        # Se invoca el constructor padre.
        super().__init__()
        # Se crea una instancia de nuestra ventana diseñada.
        self.uiVentana = frmInsertarRegistros()
        # Se llama al método "setupUi" que esta en la clase "frmInsertarRegistros" del archivo "InsertarRegistros.py".
        self.uiVentana.setupUi(self)
        # Se indica un icono para la ventana principal.
        self.setWindowIcon(QIcon('icono.ico'))
        # Se indica el tamaño de la ventana para que no se pueda modificar su tamaño.
        self.setFixedSize(342, 232)
        # Se muestra la pantalla.
        self.show()

        # Declaración de los controladores de eventos (Event Handler).
        self.uiVentana.btnConectar.clicked.connect(self.conectar_bbdd)
        self.uiVentana.btnInsertar.clicked.connect(self.insertar_registro)

        # Se desactivan los campos donde se indica la tabla, sus campos y el boton de "Insertar" de forma inicial.
        self.uiVentana.txtTabla.setEnabled(False)
        self.uiVentana.txtCodigo.setEnabled(False)
        self.uiVentana.txtNombre.setEnabled(False)
        self.uiVentana.btnInsertar.setEnabled(False)

        # Se crea un objeto de tipo ventana de mensaje.
        self.ventana_mensaje = QMessageBox(self)

        # Se crea el patrón que permite validar texto.
        # Se indica que se puede escribir desde la "a" hasta la "z" y desde la "A" hasta la "Z" mas de una vez.
        w_patron_texto = '[a-zA-Z]+'
        self.w_regex_texto = re.compile(w_patron_texto)

        # Se crea la variable de conexión y de cursor para que se pueda utilizar en el programa.
        self.w_conexion = None
        self.w_cursor = None

    # Se crea el método que se lanza cuando se pulsa en el botón "Conectar".
    def conectar_bbdd(self):

        # Se crea un bloque de excepciones donde se obtiene el nombre de la BBDD indicada en la caja de texto.
        try:

            # Se obtiene el nombre de la BBDD a utilizar.
            w_nombre_bbdd = self.uiVentana.txtBBDD.text().strip()

            # Se comprueba si el nombre de la BBDD es válido con respecto al patrón que solo permite texto al inicio y
            # luego ya si puede introducir números.
            if self.w_regex_texto.match(w_nombre_bbdd) is not None:

                # Se comprueba si existe la BBDD indicada con el método "existe_bbdd()".
                # Si la consulta ha recuperado un registro.
                if self.fun_existe_bbdd(w_nombre_bbdd) == 1:

                    # Se realiza la conexión a la BBDD que se ha indicado.
                    self.w_conexion = conexion_bbdd(w_nombre_bbdd)

                    self.pro_mensaje_informacion('Se ha conectado de forma correcta a la BBDD llamada {}'.
                                                 format(w_nombre_bbdd), 'Conexión establecida')

                    # Se activan los campos donde se indica la tabla y sus campos.
                    self.uiVentana.txtTabla.setEnabled(True)
                    self.uiVentana.txtCodigo.setEnabled(True)
                    self.uiVentana.txtNombre.setEnabled(True)
                    self.uiVentana.btnInsertar.setEnabled(True)

                    # Se desactivan los campos de BBDD y el botón de conectar.
                    self.uiVentana.txtBBDD.setEnabled(False)
                    self.uiVentana.btnConectar.setEnabled(False)

                # Si la consulta no ha recuperado datos, es que no existe la BBDD indicada y se informa por pantalla.
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

    # Se crea el método que se lanza cuando se pulsa en el botón "Insertar Registro".
    def insertar_registro(self):

        # Se crea un bloque de excepciones donde se realiza la inserción del registro indicado.
        try:

            # Se guarda en variables los datos introducidos en las cajas de texto.
            w_nombre_bbdd = self.uiVentana.txtBBDD.text().strip()
            w_nombre_tabla = self.uiVentana.txtTabla.text().strip()
            w_id = self.uiVentana.txtCodigo.text().strip()
            w_nombre = self.uiVentana.txtNombre.text().strip()

            # Se comprueba si el nombre de la tabla cumple el patrón de la expresión regular que comprueba que el nombre
            # sólo comience por letra.
            if self.w_regex_texto.match(w_nombre_tabla) is not None:

                # Se comprueba si la tabla indicada existe en la BBDD indicada utilizando el método "existe_tabla()".
                # Si ha recuperado registro, existe la tabla en la BBDD.
                if self.fun_existe_tabla(w_nombre_bbdd, w_nombre_tabla) == 1:

                    # Se comprueba que el campo código no esté vacío.
                    if w_id != '':

                        # Se comprueba que el campo nombre no esté vacío.
                        if w_nombre != '':
            
                            # Se llama al método "existe_registro()" que comprueba si ese registro está ya en la tabla.
                            # Si no existe el registro en la tabla, se inserta.
                            if self.fun_existe_registro(w_nombre_bbdd, w_nombre_tabla, w_id) == 0:

                                # Se crea el registro nuevo llamando al método "pd_insertar_registro()".
                                self.pd_insertar_registro(w_nombre_bbdd, w_nombre_tabla, w_id, w_nombre)

                                # Se indica un mensaje al usuario de que se ha insertado correctamente el nuevo
                                # registro mediante el método "pro_mensaje_informacion()".

                                self.pro_mensaje_informacion('Se ha insertado el registro {} de forma correcta en '
                                                             'la tabla {}'.format(w_nombre, w_nombre_tabla),
                                                             'Registro creado')

                                # Se limpian las cajas de texto del código y del nombre.
                                self.uiVentana.txtCodigo.setText('')
                                self.uiVentana.txtNombre.setText('')
                                self.uiVentana.txtCodigo.setFocus()

                            # Si ya existe, se informa al usuario por mensaje.
                            else:

                                self.pro_mensaje_error('El registro {} ya existe en la tabla {}.'
                                                       .format(w_nombre,  w_nombre_tabla), 'Registro ya insertado')

                                # Se limpian los registros para indicar uno nuevo.
                                self.uiVentana.txtCodigo.setText('')
                                self.uiVentana.txtNombre.setText('')
                                self.uiVentana.txtCodigo.setFocus()

                        # Si el campo "Nombre" esta vacío, se muestra un mensaje de error al usuario.
                        else:

                            self.pro_mensaje_error('El campo Nombre no esta relleno.', 'Nombre vacío')

                            # Se limpian los registros para indicar uno nuevo.
                            self.uiVentana.txtNombre.setFocus()

                    # Si el campo "Código" esta vacío, se muestra un mensaje de error al usuario.
                    else:

                        self.pro_mensaje_error('El campo Código no esta relleno.', 'Código vacío')

                        # Se limpian los registros para indicar uno nuevo.
                        self.uiVentana.txtCodigo.setFocus()

                # Si la tabla no existe en la BBDD indicada, pues se muestra un mensaje de error al usuario.
                else:

                    self.pro_mensaje_error('La tabla {} no existe en la BBDD.'.format(w_nombre_tabla),
                                           'Tabla inexistente')

                    # Se limpian los registros para indicar uno nuevo.
                    self.uiVentana.txtTabla.setText('')
                    self.uiVentana.txtCodigo.setText('')
                    self.uiVentana.txtNombre.setText('')
                    self.uiVentana.txtTabla.setFocus()

            # Si la tabla indicada es errónea o esta en campo vacío, se muestra un mensaje de error al usuario.
            else:

                self.pro_mensaje_error('El nombre de la tabla no es válida: {}'.format(w_nombre_tabla),
                                       'Error de inserción')

                # Se limpian los registros para indicar uno nuevo.
                self.uiVentana.txtTabla.setText('')
                self.uiVentana.txtCodigo.setText('')
                self.uiVentana.txtNombre.setText('')
                self.uiVentana.txtTabla.setFocus()

        # Si se ha producido un error en la conexión a la BBDD o en la inserción, se muestra un mensaje de error.
        except Error as w_error:

            self.pro_mensaje_error('Error Inserción: {}'.format(w_error), 'Error de inserción')

            # Se limpian los registros para indicar uno nuevo.
            self.uiVentana.txtCodigo.setText('')
            self.uiVentana.txtNombre.setText('')
            self.uiVentana.txtCodigo.setFocus()

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

    # Se crea el método para comprobar si ya existe en la tabla el registro a insertar.
    def fun_existe_registro(self, w_nombre_bbdd, w_nombre_tabla, w_id):

        # Se comprueba si ya existe el registro insertado en la tabla.
        w_cursor = self.w_conexion.cursor()
        w_sentencia = '''SELECT * FROM {}.{} WHERE codigo = {}'''.format(w_nombre_bbdd, w_nombre_tabla, w_id)
        w_cursor.execute(w_sentencia)
        w_resultado_sql = w_cursor.fetchall()

        # Si la consulta ha recuperado un registro.
        if w_resultado_sql:

            # Se retorna un 1 para indicar que existe un registro ya dado de alta.
            w_cursor.close()
            return 1
        # Si la consulta no ha recuperado registros.
        else:

            # Se retorna un 0 para indicar que no existe el registro dado de alta.
            w_cursor.close()
            return 0

    # Se crea un método para crear el registro nuevo en la BBDD.
    def pd_insertar_registro(self, w_nombre_bbdd, w_nombre_tabla, w_id, w_nombre):

        # Se crea el objeto cursor para luego lanzar la inserción.
        w_cursor = self.w_conexion.cursor()
        # Se crea la sentencia de la inserción del registro.
        w_sentencia = '''INSERT INTO {}.{} (codigo, nombre) VALUES ({}, '{}')'''. \
            format(w_nombre_bbdd, w_nombre_tabla, w_id, w_nombre)
        # Se ejecuta la sentencia de inserción.
        w_cursor.execute(w_sentencia)
        # Se comita el insert realizado.
        self.w_conexion.commit()

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
    # Creamos una instancia de la clase "InsertarRegistrosMySQL_Aplicacion()".
    ventana = InsertarRegistrosMySQL_Aplicacion()
    # Se muestra la pantalla.
    ventana.show()
    # Se indica el método para que cierre la aplicación al pulsar el botón de cerrar.
    sys.exit(app.exec_())
