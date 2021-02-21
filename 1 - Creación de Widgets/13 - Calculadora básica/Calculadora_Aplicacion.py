import sys
from PyQt5.QtWidgets import QDialog, QWidget, QApplication
from Calculadora import frmCalculadora


# Se crea la clase Aplicación.
class calculadora_Aplicacion(QDialog):

    # Se crea el constructor inicializador.
    def __init__(self):
        # Se invoca el constructor padre.
        super().__init__()

        # Se crea una instancia de nuestra ventana diseñada.
        self.uiVentana = frmCalculadora()
        # Se llama al método "setupUi" que esta en la clase "frmCalculadora" del archivo "Calculadora.py".
        self.uiVentana.setupUi(self)
        # Se muestra la pantalla.
        self.show()

        # Se indica el método que se activa cuando se hace "click" en cada uno de los botones.
        self.uiVentana.btnSumar.clicked.connect(self.sumar)
        self.uiVentana.btnRestar.clicked.connect(self.restar)
        self.uiVentana.btnMultiplicar.clicked.connect(self.multiplicar)
        self.uiVentana.btnDividir.clicked.connect(self.dividir)

        # Se indica que cuando se entre en la pantalla los 3 valores tengan el valor 0 predefinido.
        self.uiVentana.txtNum1.setText('0')
        self.uiVentana.txtNum2.setText('0')
        self.uiVentana.txtResultado.setText('0')

    # Se define la función de sumar los dos valores.
    def sumar(self):

        # Se declaran las variables a utilizar.
        w_num1 = 0
        w_num2 = 0

        # Se comprueba si el campo de texto del nº 1 esta vacío o lo han rellenado.
        if len(self.uiVentana.txtNum1.text()) > 0:

            # Se almacena el valor introducido en la caja de texto del nº 1.
            w_num1 = int(self.uiVentana.txtNum1.text())

        # Se comprueba si el campo de texto del nº 2 esta vacío o lo han rellenado.
        if len(self.uiVentana.txtNum2.text()) > 0:

            # Se almacena el valor introducido en la caja de texto del nº 2.
            w_num2 = int(self.uiVentana.txtNum2.text())

        # Se asigna el valor de la suma como texto de la caja de texto (Hay que indicar que sea cadena con str()).
        self.uiVentana.txtResultado.setText(str(w_num1 + w_num2))

    # Se define la función de restar los dos valores.
    def restar(self):

        # Se declaran las variables a utilizar.
        w_num1 = 0
        w_num2 = 0

        # Se comprueba si el campo de texto del nº 1 esta vacío o lo han rellenado.
        if len(self.uiVentana.txtNum1.text()) > 0:

            # Se almacena el valor introducido en la caja de texto del nº 1.
            w_num1 = int(self.uiVentana.txtNum1.text())

        # Se comprueba si el campo de texto del nº 2 esta vacío o lo han rellenado.
        if len(self.uiVentana.txtNum2.text()) > 0:

            # Se almacena el valor introducido en la caja de texto del nº 2.
            w_num2 = int(self.uiVentana.txtNum2.text())

        # Se asigna el valor de la resta como texto de la caja de texto (Hay que indicar que sea cadena con str()).
        self.uiVentana.txtResultado.setText(str(w_num1 - w_num2))

    # Se define la función de multiplicar los dos valores.
    def multiplicar(self):

        # Se declaran las variables a utilizar.
        w_num1 = 0
        w_num2 = 0

        # Se comprueba si el campo de texto del nº 1 esta vacío o lo han rellenado.
        if len(self.uiVentana.txtNum1.text()) > 0:

            # Se almacena el valor introducido en la caja de texto del nº 1.
            w_num1 = int(self.uiVentana.txtNum1.text())

        # Se comprueba si el campo de texto del nº 2 esta vacío o lo han rellenado.
        if len(self.uiVentana.txtNum2.text()) > 0:

            # Se almacena el valor introducido en la caja de texto del nº 2.
            w_num2 = int(self.uiVentana.txtNum2.text())

        # Se asigna el valor de la multiplicación como texto de la caja de texto (Hay que indicar que sea cadena con
        # str()).
        self.uiVentana.txtResultado.setText(str(w_num1 * w_num2))

    # Se define la función de dividir los dos valores.
    def dividir(self):

        # Se declaran las variables a utilizar.
        w_num1 = 0
        w_num2 = 0

        # Se comprueba si el campo de texto del nº 1 esta vacío o lo han rellenado.
        if len(self.uiVentana.txtNum1.text()) > 0:

            # Se almacena el valor introducido en la caja de texto del nº 1.
            w_num1 = int(self.uiVentana.txtNum1.text())

        # Se comprueba si el campo de texto del nº 2 esta vacío o lo han rellenado.
        if len(self.uiVentana.txtNum2.text()) > 0:

            # Se almacena el valor introducido en la caja de texto del nº 2.
            w_num2 = int(self.uiVentana.txtNum2.text())

        # Se asigna el valor de la división como texto de la caja de texto (Hay que indicar que sea cadena con str()).
        self.uiVentana.txtResultado.setText(str(w_num1 / w_num2))


# Hacemos referencia al módulo principal de la aplicación.
if __name__ == '__main__':

    # Creamos una aplicación de nuestra ventana.
    app = QApplication(sys.argv)

    # Creamos una instancia de la clase "calculadora_Aplicacion()".
    ventana = calculadora_Aplicacion()

    # Se muestra la pantalla.
    ventana.show()
    sys.exit(app.exec_())
