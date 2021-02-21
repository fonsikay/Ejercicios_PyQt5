# Se importan las librerias necesarias.
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QFontDialog
from SeleccionFuentes import frmSeleccionFuentes


# Se crea la clase Aplicación.
class SeleccionFuentes_Aplicacion(QDialog):

    # Se crea el método del constructor inicializador.
    def __init__(self):

        # Se invoca el constructor padre.
        super().__init__()
        # Se crea una instancia de nuestra ventana diseñada.
        self.uiVentana = frmSeleccionFuentes()
        # Se llama al método "setupUi" que esta en la clase "frmSeleccionFuentes" del archivo "SeleccionFuentes.py".
        self.uiVentana.setupUi(self)
        # Se muestra la pantalla.
        self.show()

        # Declaración de los controladores de eventos (Event Handler).
        self.uiVentana.btnSeleccionFuente.clicked.connect(self.seleccionar_fuente)

        # Se indica un texto por defecto en el campo de texto.
        self.uiVentana.txteTexto.setText('Ese Cadi Oe!')


    def seleccionar_fuente(self):
        # Se crea la ventana de Fuentes que devuelve la fuente seleccionada y si la seleccion ha sido correcta o no.
        w_fuente_seleccionada, w_boton_seleccionado = QFontDialog.getFont()

        # Si ha pulsado el botón de "Aceptar".
        if w_boton_seleccionado:

            # Se asigna la fuente a la caja de texto.
            self.uiVentana.txteTexto.setFont(w_fuente_seleccionada)


# Hacemos referencia al módulo principal de la aplicación.
if __name__ == '__main__':

    # Creamos una aplicación de nuestra ventana.
    app = QApplication(sys.argv)
    # Creamos una instancia de la clase "Diagnosticos_Aplicacion()".
    ventana = SeleccionFuentes_Aplicacion()
    # Se muestra la pantalla.
    ventana.show()
    # Se indica el método para que cierre la aplicación al pulsar el botón de cerrar.
    sys.exit(app.exec_())
