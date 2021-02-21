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

        # Se crea un objeto del tipo de la clase que se encuentra en el archivo "DialogoSaludo.py" creado por el compilador.
        self.uiVentana = Ui_frmPrincipal()
        # Se llama al método "setupUi" de la clase "nombreClaseArchivoCompilado()".
        self.uiVentana.setupUi(self)
        
        self.uiVentana.chkQueso.stateChanged.connect(self.calcularPrecio)
        self.uiVentana.chkJamon.stateChanged.connect(self.calcularPrecio)
        self.uiVentana.chkChampinon.stateChanged.connect(self.calcularPrecio)

        # Se muestra la clase actual.
        self.show()

    def calcularPrecio(self):
        w_precioBase = 15
        w_precioExtras = 0
        
        if self.uiVentana.chkQueso.isChecked() == True:
            w_precioExtras = w_precioExtras + 3
        if self.uiVentana.chkJamon.isChecked() == True:
            w_precioExtras = w_precioExtras + 5
        if self.uiVentana.chkChampinon.isChecked() == True:
            w_precioExtras = w_precioExtras + 2
        
        w_precioTotal = w_precioBase + w_precioExtras
        self.uiVentana.lblResultado.setText('El precio total de la pizza es de: {} €.'.format(w_precioTotal))    
        
# Se crea el iniciador para que se ejecute la ventana.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventanaDialogo = PizzeriaAplicacion()
    ventanaDialogo.show()
    sys.exit(app.exec_())
