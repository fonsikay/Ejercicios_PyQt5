# Se importan las librerias necesarias.
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QColorDialog
from PyQt5.QtGui import QColor
from SeleccionColores import frmSeleccionColor


# Se crea la clase Aplicación.
class SeleccionColores_Aplicacion(QDialog):

    # Se crea el método del constructor inicializador.
    def __init__(self):

        # Se invoca el constructor padre.
        super().__init__()
        # Se crea una instancia de nuestra ventana diseñada.
        self.uiVentana = frmSeleccionColor()
        # Se llama al método "setupUi" que esta en la clase "frmSeleccionColor" del archivo "SeleccionColores.py".
        self.uiVentana.setupUi(self)
        # Se muestra la pantalla.
        self.show()

        # Declaración de los controladores de eventos (Event Handler).
        self.uiVentana.btnSeleccionColor.clicked.connect(self.seleccionar_color)

        # Se guarda en una variable el color negro de fondo que va a tener el Frame de inicio indicando los valores
        # RGB del color negro (0,0,0).
        w_color_inicial = QColor(0, 0, 0)
        # Se indica al Frame que el color de fondo que va a tener va a ser el negro.
        self.uiVentana.frameColor.setStyleSheet('QWidget {background-color: %s}' % w_color_inicial.name())

    # Se crea el método que va a lanzar la ventana de diálogo para que se pueda elegir el color.
    def seleccionar_color(self):

        # Se crea la ventana de diálogo de selección de color para que se pueda elegir el color deseado.
        w_color_seleccionado = QColorDialog.getColor()

        # Si el color que se ha elegido es válido.
        if w_color_seleccionado.isValid():

            # Se asigna el nuevo color como color de fondo del Frame.
            self.uiVentana.frameColor.setStyleSheet('QWidget {background-color: %s}' % w_color_seleccionado.name())
            # Se indica en la caja de texto el valor del color selecionado en Hexadecimal.
            self.uiVentana.txtColor.setText(str(w_color_seleccionado.name()))


# Hacemos referencia al módulo principal de la aplicación.
if __name__ == '__main__':

    # Creamos una aplicación de nuestra ventana.
    app = QApplication(sys.argv)
    # Creamos una instancia de la clase "SeleccionColores_Aplicacion()".
    ventana = SeleccionColores_Aplicacion()
    # Se muestra la pantalla.
    ventana.show()
    # Se indica el método para que cierre la aplicación al pulsar el botón de cerrar.
    sys.exit(app.exec_())
