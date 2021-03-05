# Se importan las librerias necesarias.
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QGraphicsPixmapItem, QGraphicsScene
from PyQt5.QtGui import QIcon, QPixmap
from VisualizadorImagen import frmVisualizaImagen


# Se crea la clase Aplicación.
class VisualizadorImagen_Aplicacion(QDialog):

    # Se crea el método del constructor inicializador.
    def __init__(self):

        # Se invoca el constructor padre.
        super().__init__()
        # Se crea una instancia de nuestra ventana diseñada.
        self.uiVentana = frmVisualizaImagen()
        # Se llama al método "setupUi" que esta en la clase "frmVisualizaImagen" del archivo "VisualizadorImagen.py".
        self.uiVentana.setupUi(self)
        # Se indica un icono para la ventana principal.
        self.setWindowIcon(QIcon('icono.ico'))
        # Se indica el tamaño de la ventana para que no se pueda modificar su tamaño.
        self.setFixedSize(640, 480)
        # Se muestra la pantalla.
        self.show()

        # Se crea un objeto de tipo escena.
        w_imagen = QGraphicsScene(self)
        # Se crea un objeto de tipo Pixmap
        w_pixmap = QPixmap()
        # Se indica la ruta y el nombre de la imagen a mostrar con el método "load()".
        w_pixmap.load('fondo.png')
        # Se crea un objeto item de imagen indicándole la imagen a mostrar.
        w_item = QGraphicsPixmapItem(w_pixmap)
        # Se añade el objeto item al objeto de tipo escena.
        w_imagen.addItem(w_item)
        # Se indica en el widget Graphics View el objeto escena.
        self.uiVentana.gpcImagen.setScene(w_imagen)


# Hacemos referencia al módulo principal de la aplicación.
if __name__ == '__main__':

    # Creamos una aplicación de nuestra ventana.
    app = QApplication(sys.argv)
    # Creamos una instancia de la clase "Diagnosticos_Aplicacion()".
    ventana = VisualizadorImagen_Aplicacion()
    # Se muestra la pantalla.
    ventana.show()
    # Se indica el método para que cierre la aplicación al pulsar el botón de cerrar.
    sys.exit(app.exec_())
