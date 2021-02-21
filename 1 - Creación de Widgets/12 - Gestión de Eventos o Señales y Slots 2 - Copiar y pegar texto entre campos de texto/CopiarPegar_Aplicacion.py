import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog
from CopiarPegar import frmCopiarPegar


class copiarpegar_Aplicacion(QDialog):

    def __init__(self):
        super().__init__()

        self.uiVentana = frmCopiarPegar()
        self.uiVentana.setupUi(self)

        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)

    ventana = copiarpegar_Aplicacion()
    ventana.show()
    sys.exit(ventana.exec_())