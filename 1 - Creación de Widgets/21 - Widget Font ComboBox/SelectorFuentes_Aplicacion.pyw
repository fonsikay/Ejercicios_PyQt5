# Se importan las librerias necesarias.
import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QDialog, QApplication
from SelectorFuentes import frmFuentes


# Se crea la clase Aplicación.
class SelectorFuentes_Aplicacion(QDialog):

    # Se crea el método del constructor inicializador.
    def __init__(self):

        # Se invoca el constructor padre.
        super().__init__()
        # Se crea una instancia de nuestra ventana diseñada.
        self.uiVentana = frmFuentes()
        # Se llama al método "setupUi" que esta en la clase "frmFuentes" del archivo "SelectorFuentes.py".
        self.uiVentana.setupUi(self)
        # Se muestra la pantalla.
        self.show()

        # Se indica el método que se lanza cuando se produce un cambio en la fuente elegida del Font ComboBox.
        self.uiVentana.fcmbFuentes.currentFontChanged.connect(self.modificar_fuente)

        # Precargamos la fuente predeterminada del ComboBox como la inicial que se va a utilizar en la caja de texto.

        # Se calcula la posicion del elemento inicial predeterminado en el Font ComboBox.
        w_posicion_inicial = self.uiVentana.fcmbFuentes.currentIndex()
        # Se indica el tamaño que va a tener por defecto la fuente.
        w_tamano_fuente = 15
        # Se guarda la fuente actual predeterminada que tiene asignada el Font ComboBox.
        w_fuente_actual = QtGui.QFont(self.uiVentana.fcmbFuentes.itemText(w_posicion_inicial), w_tamano_fuente)
        # Se indica que la fuente utilizada en la caja de texto es la que se ha calculado anteriormente.
        self.uiVentana.txteFuentes.setFont(w_fuente_actual)
        # Se indica un texto predefinido para que aparezca con la fuente inicial aplicada.
        self.uiVentana.txteFuentes.setText('Texto de prueba')

    # Se crea el método para que se lance cuando se modifique el valor de la fuente de la ComboBox.
    def modificar_fuente(self):
        # Se calcula la posicion de la fuente elegida en el Font ComboBox.
        w_posicion_inicial = self.uiVentana.fcmbFuentes.currentIndex()
        # Se indica el tamaño que va a tener la fuente por defecto.
        w_tamano_fuente = 15
        # Se guarda la fuente que se ha elegido en el Font ComboBox.
        w_fuente_seleccionada = QtGui.QFont(self.uiVentana.fcmbFuentes.itemText(w_posicion_inicial), w_tamano_fuente)
        # Se indica que la fuente utilizada en la caja de texto es la elegida anteriormente.
        self.uiVentana.txteFuentes.setFont(w_fuente_seleccionada)


# Hacemos referencia al módulo principal de la aplicación.
if __name__ == '__main__':

    # Creamos una aplicación de nuestra ventana.
    app = QApplication(sys.argv)
    # Creamos una instancia de la clase "SelectorFuentes_Aplicacion()".
    ventana = SelectorFuentes_Aplicacion()
    # Se muestra la pantalla.
    ventana.show()
    # Se indica el método para que cierre la aplicación al pulsar el botón de cerrar.
    sys.exit(app.exec_())
