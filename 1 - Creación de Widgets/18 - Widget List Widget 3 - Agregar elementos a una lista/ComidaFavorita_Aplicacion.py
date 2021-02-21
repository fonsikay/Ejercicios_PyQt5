# Se importan las librerias necesarias.
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from ComidaFavorita import frmComidaFavorita


# Se crea la clase Aplicación.
class ComidaFavorita_Aplicacion(QDialog):

    # Se crea el método del constructor inicializador.
    def __init__(self):

        # Se invoca el constructor padre.
        super().__init__()
        # Se crea una instancia de nuestra ventana diseñada.
        self.uiVentana = frmComidaFavorita()
        # Se llama al método "setupUi" que esta en la clase "frmComidaFavorita" del archivo "ComidaFavorita.py".
        self.uiVentana.setupUi(self)
        # Se muestra la pantalla.
        self.show()

        # Se indica el método "anadir_comida" que se va a lanzar cuando se pulse el botón "Añadir".
        self.uiVentana.btnAnadir.clicked.connect(self.anadir_comida)

    # Se define el método "anadir_comida" para añadir el texto de la caja de texto en la lista como nuevo elemento.
    def anadir_comida(self):

        # Se almacena el texto de la caja de texto.
        w_comida = self.uiVentana.txtComida.text()
        # Se añade el texto como un nuevo elemento de la lista.
        self.uiVentana.listComida.addItem(w_comida)
        # Se limpia el texto de la caja de texto.
        self.uiVentana.txtComida.setText('')
        # Se pone el foco de nuevo en la caja de texto.
        self.uiVentana.txtComida.setFocus()


# Hacemos referencia al módulo principal de la aplicación.
if __name__ == '__main__':

    # Creamos una aplicación de nuestra ventana.
    aplicacion = QApplication(sys.argv)
    # Creamos una instancia de la clase "Diagnosticos_Aplicacion()" para que se genere nuestra ventana.
    ventana = ComidaFavorita_Aplicacion()
    # Se muestra la ventana creada.
    ventana.show()
    # Se indica el método "exec" de nuestra aplicación para que se cierre al pulsar el botón de cerrar.
    sys.exit(aplicacion.exec_())
