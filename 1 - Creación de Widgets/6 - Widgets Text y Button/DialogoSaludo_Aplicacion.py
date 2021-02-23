# Se importan las librerias necesarias para crear la aplicación.
import sys
from PyQt5.QtWidgets import QDialog, QApplication

# Se importa todas las clases del archivo creado con el PyQT5 Designer, por lo que se indica el nombre del archivo sin 
# la extensión.
from DialogoSaludo import *


# Se crea la clase principal del programa.
class DialogoSaludoAplicacion(QDialog):

    # Se define el método del constructor de la clase.
    def __init__(self):
        super().__init__()

        # Se crea un objeto del tipo de la clase que se encuentra en el archivo "DialogoSaludo.py" creado por el
        # compilador.
        self.ventanaDialogo = Ui_DialogoSaludar()
        # Se llama al método "setupUi" de la clase "Ui_DialogoSaludar".
        self.ventanaDialogo.setupUi(self)

        # Se indica el método que va a realizar una acción cuando se realice el evento "click" del botón.
        self.ventanaDialogo.btnSaludar.clicked.connect(self.mostrarsaludo)
        # Se muestra la clase actual.
        self.show()

    # Se define el método que realiza la acción de copiar el texto introducido en el "txtNombre" y pegarlo en la label
    # 'lblMensajeSaludo'.

    def mostrarsaludo(self):
        w_mensaje = self.ventanaDialogo.txtNombre.text()
        self.ventanaDialogo.lblMensajeSaludo.setText(w_mensaje)


# Se crea el iniciador para que se ejecute la ventana.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventanaDialogo = DialogoSaludoAplicacion()
    ventanaDialogo.show()
    sys.exit(app.exec_())
