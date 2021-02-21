# Se importan las librerias necesarias.
import sys
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QApplication, QWidget
from EventosSlot import frmEventos


# Se crea la clase Aplicación.
class EventosSlot_Aplicacion(QDialog):

    # Se crea el constructor inicializador.
    def __init__(self):
        # Se invoca el constructor padre.
        super().__init__()

        # Se crea una instancia de nuestra ventana diseñada.
        self.uiVentana = frmEventos()
        self.uiVentana.setupUi(self)
        self.show()


# Hacemos referencia al módulo principal de la aplicación.
if __name__ == '__main__':

    # Creamos una aplicación de nuestra ventana.
    app = QApplication(sys.argv)

    # Creamos una instancia de la clase "EventosSlot_Aplicacion()".
    ventana = EventosSlot_Aplicacion()
    ventana.show()
    sys.exit(ventana.exec_())
