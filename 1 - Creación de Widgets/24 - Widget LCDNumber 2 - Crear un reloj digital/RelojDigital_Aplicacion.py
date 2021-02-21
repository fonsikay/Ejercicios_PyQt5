# Se importan las librerias necesarias.
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import QTimer, QTime
from RelojDigital import frmRelojDigital


# Se crea la clase Aplicación.
class RelojDigital_Aplicacion(QDialog):

    # Se crea el método del constructor inicializador.
    def __init__(self):

        # Se invoca el constructor padre.
        super().__init__()
        # Se crea una instancia de nuestra ventana diseñada.
        self.uiVentana = frmRelojDigital()
        # Se llama al método "setupUi" que esta en la clase "frmRelojDigital" del archivo "RelojDigital.py".
        self.uiVentana.setupUi(self)
        # Se muestra la pantalla.
        self.show()

        # Se crea un objeto del tipo QTimer.
        w_timer = QTimer(self)
        # Se crea el método para que se lance cuando varia un minuto de la hora actual.
        w_timer.timeout.connect(self.cambiar_cada_minuto)
        w_timer.start(1000)

        # Se lanza de nuevo el método "cambiar_cada_minuto()".
        self.cambiar_cada_minuto()

    # Se crea el método que obtiene la hora del sistema y lo muestra en el display LCD.
    def cambiar_cada_minuto(self):
        # Se crea un objeto de tipo reloj que contiene la hora del sistema.
        w_hora = QTime.currentTime()
        # Se indica el formato de la hora.
        w_hora_texto = w_hora.toString('hh:mm')
        # Se indica que el valor del display sea la hora actual.
        self.uiVentana.lcdReloj.display(w_hora_texto)


# Hacemos referencia al módulo principal de la aplicación.
if __name__ == '__main__':

    # Creamos una aplicación de nuestra ventana.
    app = QApplication(sys.argv)
    # Creamos una instancia de la clase "RelojDigital_Aplicacion()".
    ventana = RelojDigital_Aplicacion()
    # Se muestra la pantalla.
    ventana.show()
    # Se indica el método para que cierre la aplicación al pulsar el botón de cerrar.
    sys.exit(app.exec_())
