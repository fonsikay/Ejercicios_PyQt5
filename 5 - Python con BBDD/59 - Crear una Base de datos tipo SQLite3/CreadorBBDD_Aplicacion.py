# Se importan las librerias necesarias.
import sys
import sqlite3
from sqlite3 import Error
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from CreadorBBDD import frmCrearBBDD


# Se crea la clase Aplicación.
class CreadorBBDD_Aplicacion(QDialog):

    # Se crea el método del constructor inicializador.
    def __init__(self):

        # Se invoca el constructor padre.
        super().__init__()
        # Se crea una instancia de nuestra ventana diseñada.
        self.uiVentana = frmCrearBBDD()
        # Se llama al método "setupUi" que esta en la clase "frmCrearBBDD" del archivo "CreadorBBDD.py".
        self.uiVentana.setupUi(self)
        # Se muestra la pantalla.
        self.show()

        # Declaración de los controladores de eventos (Event Handler).
        self.uiVentana.btnCrearBBDD.clicked.connect(self.crear_bbdd)

    # Se crea el método que se lanza cuando se pulsa el botón "Crear Base de Datos".
    def crear_bbdd(self):

        # Se comprueba si se ha rellenado el texto del nombre de la BBDD y sino, pues se informa con un mensaje.
        if len(self.uiVentana.txtNombreBBDD.text()) > 0:

            # Se guarda el nombre introducido en una variable.
            w_nombre_bbdd = self.uiVentana.txtNombreBBDD.text()

            # Se crea un bloque de excepciones por si se produce algún error en el momento de crear la BBDD.
            try:
                w_conexion = sqlite3.connect('{}.db'.format(w_nombre_bbdd))
                self.uiVentana.txtInformacion.setText('La Base de datos {} se ha creado de forma correcta.'
                                                      .format(w_nombre_bbdd))

            # Si se ha producido algún error de tipo "Error" de la libreria "sqlite3" en el momento de la creación de
            # la BBDD, pues se indica dicho error producido en el campo de texto de "Información".
            except Error as w_error:
                self.uiVentana.txtInformacion.setText('Error: {}'.format(w_error))

            # Haya error o no, se realiza el cierre de la conexión con la BBDD.
            finally:
                w_conexion.close()

        # Si no se ha rellenado el campo de texto.
        else:
            # Se crea un mensaje de texto indicando que sea de tipo Información.
            w_mensaje = QMessageBox()
            w_mensaje.setIcon(QMessageBox.Information)
            w_mensaje.setText('Debe escribir el nombre de la Base de datos.')
            w_mensaje.setWindowTitle('Mensaje de Información')
            w_mensaje.exec_()


# Hacemos referencia al módulo principal de la aplicación.
if __name__ == '__main__':

    # Creamos una aplicación de nuestra ventana.
    app = QApplication(sys.argv)
    # Creamos una instancia de la clase "CreadorBBDD_Aplicacion()".
    ventana = CreadorBBDD_Aplicacion()
    # Se muestra la pantalla.
    ventana.show()
    # Se indica el método para que cierre la aplicación al pulsar el botón de cerrar.
    sys.exit(app.exec_())
