# Se importan las librerias necesarias.
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from Calendario import frmCalendario


# Se crea la clase Aplicación.
class Calendario_Aplicacion(QDialog):

    # Se crea el método del constructor inicializador.
    def __init__(self):

        # Se invoca el constructor padre.
        super().__init__()
        # Se crea una instancia de nuestra ventana diseñada.
        self.uiVentana = frmCalendario()
        # Se llama al método "setupUi" que esta en la clase "frmCalendario" del archivo "Calendario.py".
        self.uiVentana.setupUi(self)
        # Se muestra la pantalla.
        self.show()

        # Se indica el método que se lanza cuando se elige una fecha en el Calendar Widget.
        self.uiVentana.calCalendario.selectionChanged.connect(self.actualizar_fecha)

    def actualizar_fecha(self):

        # Se guarda la fecha que se ha seleccionado en el Calendar Widget.
        w_fecha = self.uiVentana.calCalendario.selectedDate()
        # Se indica la fecha elegida en el Calendar Widget en el Date Edit.
        self.uiVentana.dateFecha.setDate(w_fecha)


# Hacemos referencia al módulo principal de la aplicación.
if __name__ == '__main__':

    # Creamos una aplicación de nuestra ventana.
    app = QApplication(sys.argv)
    # Creamos una instancia de la clase "Calendario_Aplicacion()".
    ventana = Calendario_Aplicacion()
    # Se muestra la pantalla.
    ventana.show()
    # Se indica el método para que cierre la aplicación al pulsar el botón de cerrar.
    sys.exit(app.exec_())
