# Se importan las librerias necesarias.
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from label import frmLabel


# Se crea la clase Aplicación.
class label_aplicacion(QMainWindow):

    # Se crea el método del constructor inicializador.
    def __init__(self):

        # Se invoca el constructor padre.
        super().__init__()
        # Se crea una instancia de nuestra ventana diseñada.
        self.uiVentana = frmLabel()
        # Se llama al método "setupUi" que esta en la clase "frmComidaFavorita" del archivo "Diagnosticos.py".
        self.uiVentana.setupUi(self)

        pix = QPixmap('fondo.jpg')

        self.uiVentana.label.setPixmap(pix)
        self.uiVentana.label.setScaledContents(True)
        w_sizepolicity = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.uiVentana.label.setSizePolicy(w_sizepolicity)
        # Se muestra la pantalla.
        self.show()


# Hacemos referencia al módulo principal de la aplicación.
if __name__ == '__main__':

    # Creamos una aplicación de nuestra ventana.
    app = QApplication(sys.argv)
    # Creamos una instancia de la clase "Diagnosticos_Aplicacion()".
    ventana = label_aplicacion()
    # Se muestra la pantalla.
    ventana.show()
    # Se indica el método para que cierre la aplicación al pulsar el botón de cerrar.
    sys.exit(app.exec_())
