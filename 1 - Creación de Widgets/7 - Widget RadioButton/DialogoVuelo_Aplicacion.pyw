import sys
from PyQt5.QtWidgets import QDialog, QApplication
from DialogoVuelo import Ui_ventanaVuelo


class DialogoVueloAplicacion(QDialog):
    def __init__(self):
        super().__init__()
        
        self.vuelo = Ui_ventanaVuelo()
        self.vuelo.setupUi(self)
        
        self.vuelo.rbnPrimera.toggled.connect(self.mostrarInformacion)
        self.vuelo.rbnNegocios.toggled.connect(self.mostrarInformacion)
        self.vuelo.rbnEconomica.toggled.connect(self.mostrarInformacion)
        
        self.show()
    
    def mostrarInformacion(self):
        w_precioVuelo = 0
        
        if self.vuelo.rbnPrimera.isChecked() == True:
            w_precioVuelo = 190
        
        elif self.vuelo.rbnNegocios.isChecked() == True:
            w_precioVuelo = 130
            
        elif self.vuelo.rbnEconomica.isChecked() == True:
            w_precioVuelo = 99
        
        self.vuelo.lblResultado.setText('El precio del vuelo es de {precioVuelo} €.'.format(precioVuelo = w_precioVuelo))
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventanaDialogo = DialogoVueloAplicacion()
    ventanaDialogo.show()
    sys.exit(app.exec_())