# Se importan las librerias necesarias.
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton
# Libreria para poder indicar un icono a la ventana.
from PyQt5.QtGui import QIcon


# Creamos la clase "Aplicación" que va a heredar los métodos de la clase "QMainWindow".
class Aplicacion (QMainWindow):

    # Se define el método inicializador de la clase.
    def __init__(self):

        # Se indica el constructor de la clase padre "QMainWindow".
        super(Aplicacion, self).__init__()

        # Se indica la posicion que se va a mostrar la ventana y su tamaño.
        # Los dos primeros es la posición (x, y) y los dos ultimos es el tamaño (x, y).
        self.setGeometry(400, 400, 500, 300)

        # Se indica un titulo a la ventana.
        self.setWindowTitle('Jerarquía de Herencia')

        # Se indica un icono para la ventana.
        self.setWindowIcon(QIcon('icono.ico'))

        # Se crea un boton llamado "saludar" indicando que su texto sea "Saludar" y que pertenece a esta ventana con
        # el valor "self".
        btnSaludar = QPushButton('Saludar', self)

        # Se coloca el botón en la ventana indicando su posición (x, y).
        btnSaludar.move(200, 100)

        # Se indica el método que se lanza cuando pulse el botón "Saludar".
        btnSaludar.clicked.connect(self.mostrar_mensaje)

        # Se muestra la ventana.
        self.show()

    # Se crea el método "mostrar_mensaje" para mostrar por pantalla en una ventana emergente un mensaje indicado.
    def mostrar_mensaje(self):

        # Se crea un objeto de ventana emergente.
        objVentana = QMessageBox()
        # Se indica el texto a mostrar en la ventana emergente.
        objVentana.setText('Bienvenido a PyQt5 Alfonso.')
        # Se muestra la ventana emergente.
        objVentana.exec_()


# Hacemos referencia al módulo principal de la aplicación.
if __name__ == '__main__':
    # Creamos una aplicación de nuestra ventana.
    app = QApplication(sys.argv)
    # Creamos una instancia de la clase "Aplicacion()".
    ventana = Aplicacion()
    # Se muestra la pantalla.
    ventana.show()
    # Se indica el método para que cierre la aplicación al pulsar el botón de cerrar.
    sys.exit(app.exec_())
