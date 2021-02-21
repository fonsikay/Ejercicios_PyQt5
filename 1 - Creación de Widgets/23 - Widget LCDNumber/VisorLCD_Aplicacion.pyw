# Se importan las librerias necesarias.
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QLCDNumber
from VisorLCD import frmVisorLCD


# Se crea la clase Aplicación.
class VisorLCD_Aplicacion(QDialog):

    # Se crea el método del constructor inicializador.
    def __init__(self):

        # Se invoca el constructor padre.
        super().__init__()
        # Se crea una instancia de nuestra ventana diseñada.
        self.uiVentana = frmVisorLCD()
        # Se llama al método "setupUi" que esta en la clase "frmVisorLCD" del archivo "VisorLCD.py".
        self.uiVentana.setupUi(self)
        # Se muestra la pantalla.
        self.show()

        # Se indica el método que se lanza cuando se pulsa los botones para realizar la conversión del número.
        self.uiVentana.btnDecimal.clicked.connect(self.conversion_decimal)
        self.uiVentana.btnBinario.clicked.connect(self.conversion_binario)
        self.uiVentana.btnOctal.clicked.connect(self.conversion_octal)
        self.uiVentana.btnHexadecimal.clicked.connect(self.conversion_hexadecimal)

        # Se indica un valor por defecto para el display LCD.
        self.uiVentana.lcdNumero.display(42)
        # Se indica que el numero de digitos a mostrar sea de 8 para que aparezca de forma correcta el binario.
        self.uiVentana.lcdNumero.setDigitCount(8)

    # Se crea el método para convertir el número a Decimal.
    def conversion_decimal(self):
        # Se indica que el modo va a ser Decimal.
        self.uiVentana.lcdNumero.setMode(QLCDNumber.Dec)

    # Se crea el método para convertir el número a Binario.
    def conversion_binario(self):
        # Se indica que el modo va a ser Binario.
        self.uiVentana.lcdNumero.setMode(QLCDNumber.Bin)

    # Se crea el método para convertir el número a Octal.
    def conversion_octal(self):
        # Se indica que el modo va a ser Octal.
        self.uiVentana.lcdNumero.setMode(QLCDNumber.Oct)

    # Se crea el método para convertir el número a Hexadecimal.
    def conversion_hexadecimal(self):
        # Se indica que el modo va a ser Hexadecimal.
        self.uiVentana.lcdNumero.setMode(QLCDNumber.Hex)


# Hacemos referencia al módulo principal de la aplicación.
if __name__ == '__main__':

    # Creamos una aplicación de nuestra ventana.
    app = QApplication(sys.argv)
    # Creamos una instancia de la clase "VisorLCD_Aplicacion()".
    ventana = VisorLCD_Aplicacion()
    # Se muestra la pantalla.
    ventana.show()
    # Se indica el método para que cierre la aplicación al pulsar el botón de cerrar.
    sys.exit(app.exec_())
