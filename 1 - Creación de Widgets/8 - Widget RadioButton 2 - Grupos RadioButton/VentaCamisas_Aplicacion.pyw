# Se importan las librerias necesarias.
import sys
from PyQt5.QtWidgets import QDialog, QApplication

# Se importa todas las clases del archivo creado con el PyQT5 Designer, por lo que se indica el nombre del archivo sin 
# la extensión.
from VentaCamisas import *

# Se crea la clase principal del programa.
class VentaCamisas_Aplicacion(QDialog):

    # Se define el método del constructor de la clase.
    def __init__(self):
        super().__init__()

        # Se crea un objeto del tipo de la clase que se encuentra en el archivo "DialogoSaludo.py" creado por el compilador.
        self.uiVentana = Ui_VentaCamisas()
        # Se llama al método "setupUi" de la clase "nombreClaseArchivoCompilado()".
        self.uiVentana.setupUi(self)

        self.uiVentana.rbtTallaM.toggled.connect(self.mostrarInformacion)
        self.uiVentana.rbtTallaL.toggled.connect(self.mostrarInformacion)
        self.uiVentana.rbtTallaXL.toggled.connect(self.mostrarInformacion)
        self.uiVentana.rbtTallaXXL.toggled.connect(self.mostrarInformacion)
        
        self.uiVentana.rbtPagoTarjeta.toggled.connect(self.mostrarInformacion)
        self.uiVentana.rbtPagoContra.toggled.connect(self.mostrarInformacion)
        self.uiVentana.rbtPagoTransferencia.toggled.connect(self.mostrarInformacion)
        
        # Se muestra la clase actual.
        self.show()

    def mostrarInformacion(self):
        
        w_talla = ''
        w_metodoPago = ''
        
        if self.uiVentana.rbtTallaM.isChecked() == True:
            w_talla = 'M'
        elif self.uiVentana.rbtTallaL.isChecked() == True:
            w_talla = 'L'
        elif self.uiVentana.rbtTallaXL.isChecked() == True:
            w_talla = 'XL'
        elif self.uiVentana.rbtTallaXXL.isChecked() == True:
            w_talla = 'XXL'    
        
        if self.uiVentana.rbtPagoTarjeta.isChecked() == True:
            w_metodoPago = 'Tarjeta de Débito/Crédito'
        elif self.uiVentana.rbtPagoContra.isChecked() == True:
            w_metodoPago = 'Pago Contrareembolso'
        elif self.uiVentana.rbtPagoTransferencia.isChecked() == True:
            w_metodoPago = 'Transferencia Bancaria'
        
        self.uiVentana.lblResultado.setText('La talla es {} y el método es {}.'.format(w_talla, w_metodoPago))
        
# Se crea el iniciador para que se ejecute la ventana.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventanaDialogo = VentaCamisas_Aplicacion()
    ventanaDialogo.show()
    sys.exit(app.exec_())
