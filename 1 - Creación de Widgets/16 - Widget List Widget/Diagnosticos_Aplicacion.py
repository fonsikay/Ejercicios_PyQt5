# Se importan las librerias necesarias.
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from Diagnósticos import frmDiagnostico


# Se crea la clase Aplicación.
class Diagnosticos_Aplicacion(QDialog):

    # Se crea el método del constructor inicializador.
    def __init__(self):

        # Se invoca el constructor padre.
        super().__init__()
        # Se crea una instancia de nuestra ventana diseñada.
        self.uiVentana = frmDiagnostico()
        # Se llama al método "setupUi" que esta en la clase "frmDiagnostico" del archivo "Diagnósticos.py".
        self.uiVentana.setupUi(self)
        # Se muestra la pantalla.
        self.show()

        # Se indica el método que lanza al seleccionar un valor de la lista.
        self.uiVentana.listDiagnosticos.itemClicked.connect(self.seleccion)

    # Se crea el método que indica el elemento seleccionado de la lista en una label.
    def seleccion(self):

        # Se obtiene el texto del elemento seleccionado de la lista.
        w_elemento_seleccionado = self.uiVentana.listDiagnosticos.currentItem().text()
        # Se asigna el texto de la lista a la etiqueta.
        self.uiVentana.lblResultado2.setText(w_elemento_seleccionado)


# Hacemos referencia al módulo principal de la aplicación.
if __name__ == '__main__':

    # Creamos una aplicación de nuestra ventana.
    app = QApplication(sys.argv)
    # Creamos una instancia de la clase "Diagnósticos_Aplicacion()".
    ventana = Diagnosticos_Aplicacion()
    # Se muestra la pantalla.
    ventana.show()
    # Se indica el método para que cierre la aplicación al pulsar el botón de cerrar.
    sys.exit(app.exec_())