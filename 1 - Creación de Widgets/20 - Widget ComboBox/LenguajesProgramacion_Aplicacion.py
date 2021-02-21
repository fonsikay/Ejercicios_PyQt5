# Se importan las librerias necesarias.
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from LenguajesProgramacion import frmLenguajes


# Se crea la clase Aplicación.
class LenguajesProgramacion_Aplicacion(QDialog):

    # Se crea el método del constructor inicializador.
    def __init__(self):

        # Se invoca el constructor padre.
        super().__init__()
        # Se crea una instancia de nuestra ventana diseñada.
        self.uiVentana = frmLenguajes()
        # Se llama al método "setupUi" que esta en la clase "frmLenguajes" del archivo "Lenguajes_programacion.py".
        self.uiVentana.setupUi(self)
        # Se muestra la pantalla.
        self.show()

        # Se indica el método que se lanza cuando el usuario seleccione un elemento del comboBox.
        self.uiVentana.cmbLenguaje.currentIndexChanged.connect(self.mostrar_lenguaje)

    # Se crea el método que mostrará en la caja de texto el lenguaje de programacion seleccionado en el comboBox.
    def mostrar_lenguaje(self):

        # Se obtiene la posición del elemento seleccionado dentro del comboBox.
        w_posicion_elemento_sel = self.uiVentana.cmbLenguaje.currentIndex()
        # Se obtiene el texto del elemento seleccionado en el comboBox indicando su posición.
        w_texto_elemento_sel = self.uiVentana.cmbLenguaje.itemText(w_posicion_elemento_sel)
        # Se asigna el texto obtenido del elemento del comboBox seleccionado en la caja de texto.
        self.uiVentana.txtLenguajeSel.setText(w_texto_elemento_sel)


# Hacemos referencia al módulo principal de la aplicación.
if __name__ == '__main__':

    # Creamos una aplicación de nuestra ventana.
    app = QApplication(sys.argv)
    # Creamos una instancia de la clase "LenguajesProgramacion_Aplicacion()".
    ventana = LenguajesProgramacion_Aplicacion()
    # Se muestra la pantalla.
    ventana.show()
    # Se indica el método para que cierre la aplicación al pulsar el botón de cerrar.
    sys.exit(app.exec_())