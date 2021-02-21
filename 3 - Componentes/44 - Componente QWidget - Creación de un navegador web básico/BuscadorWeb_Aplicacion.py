# Se importan las librerias necesarias.
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5.QtCore import QUrl
from BuscadorWeb import frmBuscadorWeb


# Se crea la clase Aplicación.
class BuscadorWeb_Aplicacion(QDialog):

    # Se crea el método del constructor inicializador.
    def __init__(self):

        # Se invoca el constructor padre.
        super().__init__()
        # Se crea una instancia de nuestra ventana diseñada.
        self.uiVentana = frmBuscadorWeb()
        # Se llama al método "setupUi" que esta en la clase "frmBuscadorWeb" del archivo "BuscadorWeb.py".
        self.uiVentana.setupUi(self)
        # Se muestra la pantalla.
        self.show()

        # Declaración de los controladores de eventos (Event Handler).
        self.uiVentana.btnIr.clicked.connect(self.buscador)

    # Se define el método que se lanza cuando se pulsa el botón "Ir".
    def buscador(self):

        # Se comprueba si el usuario ha introducido algo en el cuadro de texto de la URL.
        if len(self.uiVentana.txtDireccion.text()) > 0:

            # Se carga la web introducida por el usuario.
            self.uiVentana.webContenido.load(QUrl(self.uiVentana.txtDireccion.text()))

        # Si no se ha rellenado nada, se muestra un mensaje de aviso al usuario.
        else:
            ventana_aviso = QMessageBox()
            ventana_aviso.setText("Debe de introducir una dirección web para mostrar la información.")
            # Se ejecuta la pantalla de Mensaje.
            ventana_aviso.exec_()


# Hacemos referencia al módulo principal de la aplicación.
if __name__ == '__main__':

    # Creamos una aplicación de nuestra ventana.
    app = QApplication(sys.argv)
    # Creamos una instancia de la clase "BuscadorWeb_Aplicacion()".
    ventana = BuscadorWeb_Aplicacion()
    # Se muestra la pantalla.
    ventana.show()
    # Se indica el método para que cierre la aplicación al pulsar el botón de cerrar.
    sys.exit(app.exec_())
