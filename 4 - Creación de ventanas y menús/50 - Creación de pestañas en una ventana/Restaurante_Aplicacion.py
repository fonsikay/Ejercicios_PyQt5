# Se importan las librerias necesarias.
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from Restaurante import frmRestaurante


# Se crea la clase Aplicación.
class Restaurante_Aplicacion(QDialog):

    # Se crea el método del constructor inicializador.
    def __init__(self):

        # Se invoca el constructor padre.
        super().__init__()
        # Se crea una instancia de nuestra ventana diseñada.
        self.uiVentana = frmRestaurante()
        # Se llama al método "setupUi" que esta en la clase "frmRestaurante" del archivo "Restaurante.py".
        self.uiVentana.setupUi(self)
        # Se muestra la pantalla.
        self.show()


# Hacemos referencia al módulo principal de la aplicación.
if __name__ == '__main__':

    # Creamos una aplicación de nuestra ventana.
    app = QApplication(sys.argv)
    # Creamos una instancia de la clase "Restaurante_Aplicacion()".
    ventana = Restaurante_Aplicacion()
    # Se muestra la pantalla.
    ventana.show()
    # Se indica el método para que cierre la aplicación al pulsar el botón de cerrar.
    sys.exit(app.exec_())
