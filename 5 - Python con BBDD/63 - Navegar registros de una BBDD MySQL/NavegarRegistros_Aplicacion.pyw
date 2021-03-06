# Se importan las librerias necesarias.
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5.QtGui import QIcon
from Conexion_PHPMyAdmin import conexion_bbdd
from pymysql import Error
from NavegarRegistros import frmNavegacionRegistros


# Se crea la clase Aplicación.
class NavegarRegistros_Aplicacion(QDialog):

    # Se crea el método del constructor inicializador.
    def __init__(self):

        # Se invoca el constructor padre.
        super().__init__()
        # Se crea una instancia de nuestra ventana diseñada.
        self.uiVentana = frmNavegacionRegistros()
        # Se llama al método "setupUi" que esta en la clase "frmNavegacionRegistros" del archivo "NavegarRegistros.py".
        self.uiVentana.setupUi(self)
        # Se indica un icono para la ventana principal.
        self.setWindowIcon(QIcon('icono.ico'))
        # Se indica el tamaño de la ventana para que no se pueda modificar su tamaño.
        self.setFixedSize(474, 361)
        # Se muestra la pantalla.
        self.show()

        # Se crea un objeto de tipo ventana de mensaje.
        self.ventana_mensaje = QMessageBox(self)

        # Se crea la variable de conexión y de cursor para que se pueda utilizar en el programa.
        self.w_conexion = None
        self.w_cursor = None

        # Se crea una variable para contar que registro es el que se está mostrando por el formulario actualmente.
        self.w_num_registro = 1

        # Se crea dos variables para guardar el nº total de registros.
        self.w_num_total_registros = 0
        self.w_num_total = 0

        # Declaración de los controladores de eventos (Event Handler).
        self.uiVentana.btnInicio.clicked.connect(self.pro_registro_inicial)
        self.uiVentana.btnAnterior.clicked.connect(self.pro_registro_anterior)
        self.uiVentana.btnSiguiente.clicked.connect(self.pro_registro_siguiente)
        self.uiVentana.btnFinal.clicked.connect(self.pro_registro_final)

        # Se deshabilitan los botones de forma inicial por si no se conecta a la BBDD.
        self.uiVentana.btnInicio.setEnabled(False)
        self.uiVentana.btnAnterior.setEnabled(False)
        self.uiVentana.btnSiguiente.setEnabled(False)
        self.uiVentana.btnFinal.setEnabled(False)

        # Se realiza la conexion a la BBDD.
        self.pro_conexion_bbdd()

    # Se crea el método para conectar a la BBDD.
    def pro_conexion_bbdd(self):

        # Se crea un bloque de excepciones para controlar los fallos.
        try:

            # Se realiza la conexión a la BBDD del curso.
            self.w_conexion = conexion_bbdd('curso_pyqt')

            # Se obtiene el número de registros totales que tiene la tabla.
            w_cursor = self.w_conexion.cursor()
            w_sql = '''SELECT COUNT(*) FROM curso_pyqt.usuarios'''
            w_cursor.execute(w_sql)
            self.w_num_total_registros = w_cursor.fetchall()

            # Debido a que lo que devuelve "w_cursor.fetchall()" es una tupla, tengo que obtener el valor [0, 0] para
            # sacar el nº de registros actuales, por ello lo guardo en una segunda variable.
            self.w_num_total = self.w_num_total_registros[0][0]

            # Se lanza el método para realizar la consulta del primer registro.
            self.pro_registro_inicial()

        # Si se ha producido un error en la conexión a la BBDD, se muestra un mensaje de error.
        except Error as w_error:

            self.pro_mensaje_error('Error Conexión: {}'.format(w_error), 'Error de conexión')

    # Se crea el método que se lanza al pulsar en el botón "registro inicial".
    def pro_registro_inicial(self):

        # Se obtiene el primer registro de la tabla usuarios.
        w_cursor_reg = self.w_conexion.cursor()
        w_sentencia = '''SELECT * FROM curso_pyqt.usuarios LIMIT 1'''
        w_cursor_reg.execute(w_sentencia)
        w_registros_tabla = w_cursor_reg.fetchone()

        # Se indica que estamos posicionados en el primer registro.
        self.w_num_registro = 1

        # Si la consulta ha recuperado datos y está vacía.
        if w_registros_tabla is not None:

            # Se asigna al campo de texto "Código" el primer elemento de la tupla de registros.
            self.uiVentana.txtCodigo.setText(str(w_registros_tabla[0]))
            self.uiVentana.txtNombre.setText(w_registros_tabla[1])
            self.uiVentana.txtApellido1.setText(w_registros_tabla[2])
            self.uiVentana.txtApellido2.setText(w_registros_tabla[3])
            self.uiVentana.txtPass.setText(w_registros_tabla[4])
            self.uiVentana.txtEmail.setText(w_registros_tabla[5])
            self.uiVentana.txtFecCreacion.setText(str(w_registros_tabla[6]))
            self.uiVentana.txtUsuCreador.setText(w_registros_tabla[7])

            # Se habilitan los botones de forma inicial al recuperar datos.
            self.uiVentana.btnInicio.setEnabled(True)
            self.uiVentana.btnAnterior.setEnabled(True)
            self.uiVentana.btnSiguiente.setEnabled(True)
            self.uiVentana.btnFinal.setEnabled(True)

        # Si no se recupera registros, se muestra un mensaje al usuario.
        else:
            self.pro_mensaje_error('La tabla de usuarios no tiene registros.', 'Tabla sin registros')

    # Se crea el método que se lanza al pulsar en el botón "registro anterior".
    def pro_registro_anterior(self):

        # Si el nº del registro actual no ha llegado al primer registro.
        if self.w_num_registro > 1:

            # Se resta en uno el contador de registros.
            self.w_num_registro = self.w_num_registro - 1
            # Se obtiene el anterior registro al que estamos mostrando por el formulario.
            w_sentencia = '''SELECT * FROM curso_pyqt.usuarios ORDER BY codigo DESC LIMIT 1 OFFSET {}'''.\
                          format(self.w_num_total - self.w_num_registro)
            w_cursor_reg = self.w_conexion.cursor()
            w_cursor_reg.execute(w_sentencia)
            w_registros_tabla = w_cursor_reg.fetchone()

            # Si la consulta ha recuperado datos.
            if len(w_registros_tabla) > 1:

                # Se asigna al campo de texto "Código" el primer elemento de la tupla de registros.
                self.uiVentana.txtCodigo.setText(str(w_registros_tabla[0]))
                self.uiVentana.txtNombre.setText(w_registros_tabla[1])
                self.uiVentana.txtApellido1.setText(w_registros_tabla[2])
                self.uiVentana.txtApellido2.setText(w_registros_tabla[3])
                self.uiVentana.txtPass.setText(w_registros_tabla[4])
                self.uiVentana.txtEmail.setText(w_registros_tabla[5])
                self.uiVentana.txtFecCreacion.setText(str(w_registros_tabla[6]))
                self.uiVentana.txtUsuCreador.setText(w_registros_tabla[7])

        # Si se ha llegado al primer registro, se muestra un mensaje de información al usuario.
        else:

            self.pro_mensaje_informacion('Se ha llegado al primer registro de la tabla.', 'Primer registro')

    # Se crea el método que se lanza al pulsar en el botón "registro siguiente".
    def pro_registro_siguiente(self):

        # Si el nº del registro actual no ha llegado al último registro.
        if self.w_num_registro < self.w_num_total:

            # Se obtiene el siguiente registro al que estamos mostrando por el formulario.
            w_sentencia = '''SELECT * FROM curso_pyqt.usuarios LIMIT 1 OFFSET {}'''.format(self.w_num_registro)
            w_cursor_reg = self.w_conexion.cursor()
            w_cursor_reg.execute(w_sentencia)
            w_registros_tabla = w_cursor_reg.fetchone()
            # Se aumenta el contador de registros.
            self.w_num_registro = self.w_num_registro + 1

            # Si la consulta ha recuperado datos.
            if len(w_registros_tabla) > 0:

                # Se asigna al campo de texto "Código" el primer elemento de la tupla de registros.
                self.uiVentana.txtCodigo.setText(str(w_registros_tabla[0]))
                self.uiVentana.txtNombre.setText(w_registros_tabla[1])
                self.uiVentana.txtApellido1.setText(w_registros_tabla[2])
                self.uiVentana.txtApellido2.setText(w_registros_tabla[3])
                self.uiVentana.txtPass.setText(w_registros_tabla[4])
                self.uiVentana.txtEmail.setText(w_registros_tabla[5])
                self.uiVentana.txtFecCreacion.setText(str(w_registros_tabla[6]))
                self.uiVentana.txtUsuCreador.setText(w_registros_tabla[7])

        # Si se ha llegado al último registro, se muestra un mensaje de información al usuario.
        else:

            self.pro_mensaje_informacion('Se ha llegado al último registro de la tabla.', 'Último registro')

    # Se crea el método que se lanza al pulsar en el botón "registro final".
    def pro_registro_final(self):

        # Se indica que estamos posicionados en el último registro.
        self.w_num_registro = self.w_num_total

        # Se obtiene el primer registro de la tabla usuarios.
        w_cursor_reg = self.w_conexion.cursor()
        w_sentencia = '''SELECT * FROM curso_pyqt.usuarios ORDER BY codigo DESC LIMIT 1'''
        w_cursor_reg.execute(w_sentencia)
        w_registros_tabla = w_cursor_reg.fetchone()

        # Si la consulta ha recuperado datos.
        if len(w_registros_tabla) > 0:

            # Se asigna al campo de texto "Código" el primer elemento de la tupla de registros.
            self.uiVentana.txtCodigo.setText(str(w_registros_tabla[0]))
            self.uiVentana.txtNombre.setText(w_registros_tabla[1])
            self.uiVentana.txtApellido1.setText(w_registros_tabla[2])
            self.uiVentana.txtApellido2.setText(w_registros_tabla[3])
            self.uiVentana.txtPass.setText(w_registros_tabla[4])
            self.uiVentana.txtEmail.setText(w_registros_tabla[5])
            self.uiVentana.txtFecCreacion.setText(str(w_registros_tabla[6]))
            self.uiVentana.txtUsuCreador.setText(w_registros_tabla[7])

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
    # Creamos una instancia de la clase "NavegarRegistros_Aplicacion()".
    ventana = NavegarRegistros_Aplicacion()
    # Se muestra la pantalla.
    ventana.show()
    # Se indica el método para que cierre la aplicación al pulsar el botón de cerrar.
    sys.exit(app.exec_())
