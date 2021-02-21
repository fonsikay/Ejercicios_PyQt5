# Se importan las librerias necesarias.
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PuntoVenta import frmPuntoVenta


# Se crea la clase Aplicación.
class PuntoVenta_Aplicacion(QDialog):

    # Se crea el método del constructor inicializador.
    def __init__(self):
        # Se invoca el constructor padre.
        super().__init__()
        # Se crea una instancia de nuestra ventana diseñada.
        self.uiVentana = frmPuntoVenta()
        # Se llama al método "setupUi" que esta en la clase "frmPuntoVenta" del archivo "PuntoVenta.py".
        self.uiVentana.setupUi(self)
        # Se muestra la pantalla.
        self.show()

        # Se indica el método que se lanza cuando el usuario ha elegido el valor correcto en el SpinBox.
        self.uiVentana.spbCantTeclado.editingFinished.connect(self.calcular_total)
        self.uiVentana.sbpCantRaton.editingFinished.connect(self.calcular_total)

    # Se crea el método "calcular_total" que calcula según el precio y la cantidad, los precios de los subtotales y del
    # total de la compra.
    def calcular_total(self):

        # Se activan las cajas de texto de los campos de subtotales y totales para que puedan ser modificados.
        self.uiVentana.txtSubtotalTeclado.setReadOnly(False)
        self.uiVentana.txtSubTotalRaton.setReadOnly(False)
        self.uiVentana.txtTotal.setReadOnly(False)

        # Se obtiene el precio indicado del teclado y del ratón.
        w_precio_teclado = int(self.uiVentana.txtPrecioTeclado.text())
        w_precio_raton = int(self.uiVentana.txtPrecioRaton.text())

        # Se obtiene la cantidad indicada de teclados y ratones.
        w_cantidad_teclado = int(self.uiVentana.spbCantTeclado.value())
        w_cantidad_raton = int(self.uiVentana.sbpCantRaton.value())

        # Se calcula el subtotal de la compra de teclados y ratones.
        w_subtotal_teclado = w_precio_teclado * w_cantidad_teclado
        w_subtotal_raton = w_precio_raton * w_cantidad_raton

        # Se asocia el valor obtenido de los subtotales a cada una de las cajas de texto de Subtotales.
        self.uiVentana.txtSubtotalTeclado.setText(str(w_subtotal_teclado))
        self.uiVentana.txtSubTotalRaton.setText(str(w_subtotal_raton))

        # Se calcula el total de la compra de teclados y ratones.
        w_total = w_subtotal_teclado + w_subtotal_raton

        # Se asocia el valor obtenido del total a la caja de texto de Total.
        self.uiVentana.txtTotal.setText(str(w_total))

        # Se desactivan las cajas de texto de los campos de subtotales y totales para que no puedan ser modificados.
        self.uiVentana.txtSubtotalTeclado.setReadOnly(True)
        self.uiVentana.txtSubTotalRaton.setReadOnly(True)
        self.uiVentana.txtTotal.setReadOnly(True)

# Hacemos referencia al módulo principal de la aplicación.
if __name__ == '__main__':
    # Creamos una aplicación de nuestra ventana.
    app = QApplication(sys.argv)
    # Creamos una instancia de la clase "PuntoVenta_Aplicacion()".
    ventana = PuntoVenta_Aplicacion()
    # Se muestra la pantalla.
    ventana.show()
    # Se indica el método para que cierre la aplicación al pulsar el botón de cerrar.
    sys.exit(app.exec_())
