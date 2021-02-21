# Se importan las librerias necesarias.
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from VentanaFlotante import venPrincipal


# Se crea la clase Aplicación.
class VentanaFlotante_Aplicacion(QMainWindow):

    # Se crea el método del constructor inicializador.
    def __init__(self):

        # Se invoca el constructor padre.
        super().__init__()
        # Se crea una instancia de nuestra ventana diseñada.
        self.uiVentana = venPrincipal()
        # Se llama al método "setupUi" que esta en la clase "venPrincipal" del archivo "VentanaFlotante.py".
        self.uiVentana.setupUi(self)
        # Se muestra la pantalla.
        self.show()

        # Declaración de los controladores de eventos (Event Handler).
        self.uiVentana.btnIniciarSesion.clicked.connect(self.iniciar_sesion)

    # Se crea el módulo que se lanza cuando se pulsa el botón de "Iniciar Sesion".
    def iniciar_sesion(self):
        pass


# Hacemos referencia al módulo principal de la aplicación.
if __name__ == '__main__':

    # Creamos una aplicación de nuestra ventana.
    app = QApplication(sys.argv)
    # Creamos una instancia de la clase "VentanaFlotante_Aplicacion()".
    ventana = VentanaFlotante_Aplicacion()
    # Se muestra la pantalla.
    ventana.show()
    # Se indica el método para que cierre la aplicación al pulsar el botón de cerrar.
    sys.exit(app.exec_())
