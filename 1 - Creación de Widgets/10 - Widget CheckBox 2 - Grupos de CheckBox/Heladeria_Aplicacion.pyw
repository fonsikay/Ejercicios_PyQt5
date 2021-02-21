# Se importan las librerias necesarias.
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QPushButton

# Se importa todas las clases del archivo creado con el PyQT5 Designer, por lo que se indica el nombre del archivo sin 
# la extensión.
from Heladeria import frmHeladeria


# Se crea la clase principal del programa.
class Heladeria_Aplicacion(QDialog):

    # Se define el método del constructor de la clase.
    def __init__(self):
        super().__init__()

        # Se crea un objeto del tipo de la clase que se encuentra en el archivo "DialogoSaludo.py" creado por el
        # compilador.
        self.uiVentana = frmHeladeria()
        # Se llama al método "setupUi" de la clase "nombreClaseArchivoCompilado()".
        self.uiVentana.setupUi(self)

        # Se asocia en el evento del cambio del checkbox el método "calcularprecio".
        self.uiVentana.chkChocolate.stateChanged.connect(self.calcularprecio)
        self.uiVentana.chkVainilla.stateChanged.connect(self.calcularprecio)
        self.uiVentana.chkFresa.stateChanged.connect(self.calcularprecio)
        self.uiVentana.chkRon.stateChanged.connect(self.calcularprecio)
        self.uiVentana.chkCafe.stateChanged.connect(self.calcularprecio)
        self.uiVentana.chkAgua.stateChanged.connect(self.calcularprecio)
        self.uiVentana.chkRefresco.stateChanged.connect(self.calcularprecio)

        # Se muestra la clase actual.
        self.show()

    # Se define el método asociado al evento del checkbox llamado "calcularprecio".
    def calcularprecio(self):

        w_preciohelado = 0
        w_preciobebida = 0

        # Se observa si los checks estan marcados y cuando estén marcados, pues se suma el precio que ya tiene con el
        # precio del producto marcado.
        if self.uiVentana.chkChocolate.isChecked():
            w_preciohelado = w_preciohelado + 3
        if self.uiVentana.chkVainilla.isChecked():
            w_preciohelado = w_preciohelado + 2
        if self.uiVentana.chkFresa.isChecked():
            w_preciohelado = w_preciohelado + 3
        if self.uiVentana.chkRon.isChecked():
            w_preciohelado = w_preciohelado + 5
        if self.uiVentana.chkCafe.isChecked():
            w_preciobebida = w_preciobebida + 2
        if self.uiVentana.chkAgua.isChecked():
            w_preciobebida = w_preciobebida + 1
        if self.uiVentana.chkRefresco.isChecked():
            w_preciobebida = w_preciobebida + 3

        # Se suman los precios de los helados y bebidas marcadas y se muestra el total en la label.
        w_preciototal = w_preciohelado + w_preciobebida
        self.uiVentana.lblPrecioTotal.setText('El precio total es de: {} €.'.format(w_preciototal))


# Se crea el iniciador para que se ejecute la ventana.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventanaDialogo = Heladeria_Aplicacion()
    ventanaDialogo.show()
    sys.exit(app.exec_())
