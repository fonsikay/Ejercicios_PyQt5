# Se importan las librerias necesarias.
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from ReservasHotel import frmReservaHotel
from datetime import datetime, timedelta


# Se crea la clase Aplicación.
class ReservasHotel_Aplicacion(QDialog):

    # Se crea el método del constructor inicializador.
    def __init__(self):

        # Se invoca el constructor padre.
        super().__init__()
        # Se crea una instancia de nuestra ventana diseñada.
        self.uiVentana = frmReservaHotel()
        # Se llama al método "setupUi" que esta en la clase "frmReservaHotel" del archivo "ReservaHotel.py".
        self.uiVentana.setupUi(self)
        # Se muestra la pantalla.
        self.show()

        # Declaración de los controladores de eventos (Event Handler).
        self.uiVentana.calCalendario.selectionChanged.connect(self.calcular_fecha)
        self.uiVentana.spbCantDias.editingFinished.connect(self.calcular_dias)
        self.uiVentana.cmbTipoHab.currentIndexChanged.connect(self.calcular_tipohab)
        self.uiVentana.btnCalcular.clicked.connect(self.calcular_importe)

    # Declaración de los métodos lanzados por los eventos de los Widgets.

    # Se crea el método "calcular_fecha()" que obtiene la fecha elegida en el calendario.
    def calcular_fecha(self):

        # Se guarda la fecha elegida en el calendario.
        w_fecha = self.uiVentana.calCalendario.selectedDate()
        # Se guarda la fecha transformada en cadena para que tenga el formato correcto y se retorna.
        w_fecha_cadena = str(w_fecha.toPyDate())
        return w_fecha_cadena

    # Se crea el método que obtiene el nº de días elegido.
    def calcular_dias(self):

        # Se obtiene el nº de días elegido en el SpinBox y se retorna.
        w_cantidad_dias = self.uiVentana.spbCantDias.value()
        return w_cantidad_dias

    # Se crea el método "calcular_tipohab()" para calcular el precio y el nombre del tipo de habitación elegida.
    def calcular_tipohab(self):

        # Se obtiene el texto de la opción elegida en el ComboBox.
        w_tipohab = self.uiVentana.cmbTipoHab.itemText(self.uiVentana.cmbTipoHab.currentIndex())

        # Según sea el nombre del tipo de habitación, se asigna un precio al tipo de habitación y se retorna los dos
        # valores.
        if w_tipohab == 'Simple':
            w_precio = 20
        elif w_tipohab == 'Doble':
            w_precio = 30
        elif w_tipohab == 'Superior':
            w_precio = 40
        elif w_tipohab == 'Suite':
            w_precio = 50
        else:
            w_precio = 60

        return w_precio, w_tipohab

    # Se crea el método "calcular_importe()" para realizar el cálculo del importe y el texto del Resúmen.
    def calcular_importe(self):

        # Se llama al método "calcular_dias()" para obtener el nº de días de la reserva.
        w_cantidad_dias = self.calcular_dias()
        # Se llama al método "calcular_tipohab()" para obtener el precio y el nombre del tipo de habitación.
        w_precio_hab, w_tipohab = self.calcular_tipohab()
        # Se calcula el importe de la reserva.
        w_importe_reserva = w_cantidad_dias * w_precio_hab
        # Se indica el importe de la reserva en el textBox.
        self.uiVentana.txtImporte.setText('{} €'.format(w_importe_reserva))

        # Se llama al método de "calcular_fecha" para obtener la fecha seleccionada en el calendario.
        w_fecha_entrada = self.calcular_fecha()
        # Se indica la máscara de fecha actual que tiene la fecha obtenida, en este caso, (YYYY-MM-DD).
        w_fecha_entrada = datetime.strptime(w_fecha_entrada, "%Y-%m-%d")

        # Se le suma a la fecha de entrada el nº de días de estancia para calcular la fecha de salida.
        w_fecha_salida = w_fecha_entrada + timedelta(days=w_cantidad_dias)

        # Se indica la máscara de formato (DD/MM/YYYY) a las fecha de inicio y fin.
        w_fecha_entrada = datetime.strftime(w_fecha_entrada, "%d/%m/%Y")
        w_fecha_salida = datetime.strftime(w_fecha_salida, "%d/%m/%Y")

        # Se indica en el campo "Resumen de reserva" los datos de la reserva calculados.
        self.uiVentana.txtResumen.setText('Check In: {} - Check Out: {} - Nº días: {} - Habitación: {}.'.
                                          format(w_fecha_entrada, w_fecha_salida, w_cantidad_dias, w_tipohab))


# Hacemos referencia al módulo principal de la aplicación.
if __name__ == '__main__':

    # Creamos una aplicación de nuestra ventana.
    app = QApplication(sys.argv)
    # Creamos una instancia de la clase "ReservasHotel_Aplicacion()".
    ventana = ReservasHotel_Aplicacion()
    # Se muestra la pantalla.
    ventana.show()
    # Se indica el método para que cierre la aplicación al pulsar el botón de cerrar.
    sys.exit(app.exec_())
