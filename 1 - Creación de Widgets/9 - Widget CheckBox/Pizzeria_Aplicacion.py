# Se importan las librerias necesarias.
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QPushButton

# Se importa todas las clases del archivo creado con el PyQT5 Designer, por lo que se indica el nombre del archivo sin 
# la extensión.
from Pizzeria import Ui_frmPrincipal


# Se crea la clase principal del programa.
class PizzeriaAplicacion(QDialog):

    # Se define el método del constructor de la clase.
    def __init__(self):
        super().__init__()

        # Se crea un objeto del tipo de la clase que se encuentra en el archivo "DialogoSaludo.py" creado por el
        # compilador.
        self.uiVentana = Ui_frmPrincipal()
        # Se llama al método "setupUi" de la clase "nombreClaseArchivoCompilado()".
        self.uiVentana.setupUi(self)
        
        self.uiVentana.chkQueso.stateChanged.connect(self.calcularprecio)
        self.uiVentana.chkJamon.stateChanged.connect(self.calcularprecio)
        self.uiVentana.chkChampinon.stateChanged.connect(self.calcularprecio)

        self.uiVentana.lblResultado.setText('El precio total de la pizza es de: 15 €.')
                                            
        # Se muestra la clase actual.
        self.show()

    def calcularprecio(self):
        w_preciobase = 15
        w_precioextras = 0
        
        if self.uiVentana.chkQueso.isChecked():
            w_precioextras = w_precioextras + 3
        if self.uiVentana.chkJamon.isChecked():
            w_precioextras = w_precioextras + 5
        if self.uiVentana.chkChampinon.isChecked():
            w_precioextras = w_precioextras + 2
        
        w_preciototal = w_preciobase + w_precioextras
        self.uiVentana.lblResultado.setText('El precio total de la pizza es de: {} €.'.format(w_preciototal))


# Se crea el iniciador para que se ejecute la ventana.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventanaDialogo = PizzeriaAplicacion()
    ventanaDialogo.show()
    sys.exit(app.exec_())
