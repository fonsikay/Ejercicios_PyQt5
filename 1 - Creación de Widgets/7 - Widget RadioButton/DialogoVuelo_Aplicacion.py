import sys
from PyQt5.QtWidgets import QDialog, QApplication
from DialogoVuelo import Ui_ventanaVuelo


class DialogoVueloAplicacion(QDialog):
    def __init__(self):
        super().__init__()

        self.vuelo = Ui_ventanaVuelo()
        self.vuelo.setupUi(self)

        self.vuelo.rbnPrimera.toggled.connect(self.mostrarinformacion)
        self.vuelo.rbnNegocios.toggled.connect(self.mostrarinformacion)
        self.vuelo.rbnEconomica.toggled.connect(self.mostrarinformacion)

        self.show()

    def mostrarinformacion(self):
        w_preciovuelo = 0

        if self.vuelo.rbnPrimera.isChecked():
            w_preciovuelo = 190

        elif self.vuelo.rbnNegocios.isChecked():
            w_preciovuelo = 130

        elif self.vuelo.rbnEconomica.isChecked():
            w_preciovuelo = 99

        self.vuelo.lblResultado.setText('El precio del vuelo es de {precioVuelo} €.'.format(precioVuelo = w_preciovuelo))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventanaDialogo = DialogoVueloAplicacion()
    ventanaDialogo.show()
    sys.exit(app.exec_())