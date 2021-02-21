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

        # Se crea un objeto del tipo de la clase que se encuentra en el archivo "DialogoSaludo.py" creado por el
        # compilador.
        self.uiVentana = Ui_VentaCamisas()
        # Se llama al método "setupUi" de la clase "nombreClaseArchivoCompilado()".
        self.uiVentana.setupUi(self)

        self.uiVentana.rbtTallaM.toggled.connect(self.mostrarinformacion)
        self.uiVentana.rbtTallaL.toggled.connect(self.mostrarinformacion)
        self.uiVentana.rbtTallaXL.toggled.connect(self.mostrarinformacion)
        self.uiVentana.rbtTallaXXL.toggled.connect(self.mostrarinformacion)
        
        self.uiVentana.rbtPagoTarjeta.toggled.connect(self.mostrarinformacion)
        self.uiVentana.rbtPagoContra.toggled.connect(self.mostrarinformacion)
        self.uiVentana.rbtPagoTransferencia.toggled.connect(self.mostrarinformacion)
        
        # Se muestra la clase actual.
        self.show()

    def mostrarinformacion(self):
        
        w_talla = ''
        w_metodopago = ''
        
        if self.uiVentana.rbtTallaM.isChecked():
            w_talla = 'M'
        elif self.uiVentana.rbtTallaL.isChecked():
            w_talla = 'L'
        elif self.uiVentana.rbtTallaXL.isChecked():
            w_talla = 'XL'
        elif self.uiVentana.rbtTallaXXL.isChecked():
            w_talla = 'XXL'    
        
        if self.uiVentana.rbtPagoTarjeta.isChecked():
            w_metodopago = 'Tarjeta de Débito/Crédito'
        elif self.uiVentana.rbtPagoContra.isChecked():
            w_metodopago = 'Pago Contrareembolso'
        elif self.uiVentana.rbtPagoTransferencia.isChecked():
            w_metodopago = 'Transferencia Bancaria'
        
        self.uiVentana.lblResultado.setText('La talla es {} y el método es {}.'.format(w_talla, w_metodopago))


# Se crea el iniciador para que se ejecute la ventana.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventanaDialogo = VentaCamisas_Aplicacion()
    ventanaDialogo.show()
    sys.exit(app.exec_())
