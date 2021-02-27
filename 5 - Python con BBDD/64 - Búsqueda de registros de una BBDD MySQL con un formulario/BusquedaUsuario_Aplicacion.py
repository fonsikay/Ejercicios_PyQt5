# Se importan las librerias necesarias.
import sys
import re

from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5.QtGui import QIcon
from Conexion_PHPMyAdmin import conexion_bbdd
from pymysql import Error
from BusquedaUsuario import frmBusquedaUsuario


# Se crea la clase Aplicación.
class BusquedaUsuario_Aplicacion(QDialog):

    # Se crea el método del constructor inicializador.
    def __init__(self):

        # Se invoca el constructor padre.
        super().__init__()
        # Se crea una instancia de nuestra ventana diseñada.
        self.uiVentana = frmBusquedaUsuario()
        # Se llama al método "setupUi" que esta en la clase "frmBusquedaUsuario" del archivo "BusquedaUsuario.py".
        self.uiVentana.setupUi(self)
        # Se indica un icono para la ventana principal.
        self.setWindowIcon(QIcon('icono_ventana.ico'))
        # Se indica el tamaño de la ventana para que no se pueda modificar su tamaño.
        self.setFixedSize(412, 401)
        # Se muestra la pantalla.
        self.show()

        # Declaración de los controladores de eventos (Event Handler).
        self.uiVentana.btnBuscar.clicked.connect(self.pro_buscar_registro)

        # Se indica el foco en el campo de búsqueda.
        self.uiVentana.txtBusCodigo.setFocus()
        # Se crea un objeto de tipo ventana de mensaje.
        self.ventana_mensaje = QMessageBox(self)

        # Se crea la variable de conexión y de cursor para que se pueda utilizar en el programa.
        self.w_conexion = None
        self.w_cursor = None

        # Se realiza la conexion a la BBDD.
        self.pro_conexion_bbdd()

    # Se crea el método para conectar a la BBDD.
    def pro_conexion_bbdd(self):

        # Se crea un bloque de excepciones para controlar los fallos.
        try:

            # Se realiza la conexión a la BBDD del curso.
            self.w_conexion = conexion_bbdd('curso_pyqt')

        # Si se ha producido un error en la conexión a la BBDD, se muestra un mensaje de error.
        except Error as w_error:

            self.pro_mensaje_error('Error Conexión: {}'.format(w_error), 'Error de conexión')

    # Se crea el método que se lanza al pulsar el botón "Buscar".
    def pro_buscar_registro(self):

        # Se guarda en una variable el código del usuario a buscar.
        w_txtbuscodigo = self.uiVentana.txtBusCodigo.text()

        # Se comprueba si el usuario ha introducido algún texto en el campo de búsqueda.
        if w_txtbuscodigo != '':

            # Si lo que ha introducido el usuario son caracteres numéricos.
            if w_txtbuscodigo.isdigit():

                # Se consulta en la tabla usuarios los datos del usuario a buscar.
                w_cursor = self.w_conexion.cursor()
                w_sentencia_sql = '''SELECT * FROM curso_pyqt.usuarios WHERE codigo = {}'''.format(w_txtbuscodigo)
                w_cursor.execute(w_sentencia_sql)
                w_registros = w_cursor.fetchone()

                # Si la consulta ha recuperado datos y no está vacía.
                if w_registros is not None:

                    # Se asigna al campo de texto "Código" el primer elemento de la tupla de registros.
                    self.uiVentana.txtCodigo.setText(str(w_registros[0]))
                    self.uiVentana.txtNombre.setText(w_registros[1])
                    self.uiVentana.txtApellido1.setText(w_registros[2])
                    self.uiVentana.txtApellido2.setText(w_registros[3])
                    self.uiVentana.txtContrasena.setText(w_registros[4])
                    self.uiVentana.txtEmail.setText(w_registros[5])
                    self.uiVentana.txtFecCreacion.setText(str(w_registros[6]))
                    self.uiVentana.txtUsuCreador.setText(w_registros[7])

                # Si no se recupera registros, se muestra un mensaje al usuario.
                else:

                    # Se limpia los campos del formulario.
                    self.pro_limpiar_formulario()

                    self.pro_mensaje_informacion('No se ha encontrado el usuario con código {}.'.format(w_txtbuscodigo),
                                                 'Usuario no encontrado')

            # Si el código del usuario no es númerico, pues se muestra un mensaje de error al usuario.
            else:

                # Se limpia los campos del formulario.
                self.pro_limpiar_formulario()

                self.pro_mensaje_error('El código del usuario introducido es erróneo ya que tiene que ser númérico.',
                                       'Código de usuario erróneo')

        # Si no ha introducido el código a buscar, se informa al usuario por mensaje.
        else:

            # Se limpia los campos del formulario.
            self.pro_limpiar_formulario()

            self.pro_mensaje_informacion('No se ha indicado el código del usuario a buscar.', 'Código vacío')

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

    # Se crea un método para limpiar los campos del formulario.
    def pro_limpiar_formulario(self):

        self.uiVentana.txtCodigo.setText('')
        self.uiVentana.txtNombre.setText('')
        self.uiVentana.txtApellido1.setText('')
        self.uiVentana.txtApellido2.setText('')
        self.uiVentana.txtContrasena.setText('')
        self.uiVentana.txtEmail.setText('')
        self.uiVentana.txtFecCreacion.setText('')
        self.uiVentana.txtUsuCreador.setText('')
        self.uiVentana.txtBusCodigo.setFocus()
        self.uiVentana.txtBusCodigo.setText('')


# Hacemos referencia al módulo principal de la aplicación.
if __name__ == '__main__':

    # Creamos una aplicación de nuestra ventana.
    app = QApplication(sys.argv)
    # Creamos una instancia de la clase "BusquedaUsuario_Aplicacion()".
    ventana = BusquedaUsuario_Aplicacion()
    # Se muestra la pantalla.
    ventana.show()
    # Se indica el método para que cierre la aplicación al pulsar el botón de cerrar.
    sys.exit(app.exec_())
