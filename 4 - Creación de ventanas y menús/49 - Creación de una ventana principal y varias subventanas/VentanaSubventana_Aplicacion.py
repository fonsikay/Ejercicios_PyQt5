# Se importan las librerias necesarias.
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from VentanaSubventana import frmContenedorVentanas


# Se crea la clase Aplicación.
class VentanaSubventana_Aplicacion(QMainWindow):

    # Se crea el método del constructor inicializador.
    def __init__(self):

        # Se invoca el constructor padre.
        super().__init__()
        # Se crea una instancia de nuestra ventana diseñada.
        self.uiVentana = frmContenedorVentanas()
        # Se llama al método "setupUi" que esta en la clase "frmContenedorVentanas" del archivo "VentanaSubventanas.py".
        self.uiVentana.setupUi(self)

        # Declaración de los controladores de eventos (Event Handler) del menú.
        self.uiVentana.mniPestana.triggered.connect(self.vista_tab)
        self.uiVentana.mniCascada.triggered.connect(self.vista_cascada)
        self.uiVentana.mniCuadricula.triggered.connect(self.vista_cuadricula)
        self.uiVentana.mniSubVentanas.triggered.connect(self.vista_subventana)

        self.uiVentana.mdiArea.addSubWindow(self.uiVentana.winPrimeraVent)
        self.uiVentana.mdiArea.addSubWindow(self.uiVentana.winSegundaVent)

        # Se muestra la pantalla.
        self.show()

    # Se crea el método que se lanza cuando se pulsa la opción del menú "Vista Pestañas".
    def vista_tab(self):

        # Se indica el módo de visión de pestañas.
        self.uiVentana.mdiArea.setViewMode(1)

    # Se crea el método que se lanza cuando se pulsa la opción del menú "Vista Cascada".
    def vista_cascada(self):

        # Se indica el módo de visión de Cascada.
        self.uiVentana.mdiArea.cascadeSubWindows()

    # Se crea el método que se lanza cuando se pulsa la opción del menú "Vista Cuadrícula".
    def vista_cuadricula(self):

        # Se indica el módo de visión de Cuadrícula.
        self.uiVentana.mdiArea.tileSubWindows()

    # Se crea el método que se lanza cuando se pulsa la opción del menú "Vista Subventanas".
    def vista_subventana(self):

        # Se indica el módo de visión de Subventanas.
        self.uiVentana.mdiArea.setViewMode(0)


# Hacemos referencia al módulo principal de la aplicación.
if __name__ == '__main__':

    # Creamos una aplicación de nuestra ventana.
    app = QApplication(sys.argv)
    # Creamos una instancia de la clase "VentanaSubventana_Aplicacion()".
    ventana = VentanaSubventana_Aplicacion()
    # Se muestra la pantalla.
    ventana.show()
    # Se indica el método para que cierre la aplicación al pulsar el botón de cerrar.
    sys.exit(app.exec_())
