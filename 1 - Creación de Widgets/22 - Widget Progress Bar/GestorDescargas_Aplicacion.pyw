# Se importan las librerias necesarias.
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from GestorDescargas import frmGestorDescarga


# Se crea la clase Aplicación.
class GestorDescargas_Aplicacion(QDialog):

    # Se crea el método del constructor inicializador.
    def __init__(self):

        # Se invoca el constructor padre.
        super().__init__()
        # Se crea una instancia de nuestra ventana diseñada.
        self.uiVentana = frmGestorDescarga()
        # Se llama al método "setupUi" que esta en la clase "frmGestorDescarga" del archivo "GestorDescargas.py".
        self.uiVentana.setupUi(self)
        # Se muestra la pantalla.
        self.show()

        # Se indica el método "iniciar_descarga" que se lanza cuando se pulsa el botón.
        self.uiVentana.btnIniciarDescarga.clicked.connect(self.iniciar_descarga)

    # Se crea el método para iniciar la descarga.
    def iniciar_descarga(self):
        # Se inicializa la variable contador.
        w_valor_progreso = 0

        # Mientras que la variable contador sea menor o igual a 100.
        while w_valor_progreso < 100:
            # Se aumenta el valor del contador.
            w_valor_progreso = w_valor_progreso + 0.0001
            # Se indica dicho aumento como el valor que tiene la barra de progreso simulando la descarga y finalizando
            # en el valor 100.
            self.uiVentana.pgbDescargaArchivo.setValue(int(w_valor_progreso))


# Hacemos referencia al módulo principal de la aplicación.
if __name__ == '__main__':

    # Creamos una aplicación de nuestra ventana.
    app = QApplication(sys.argv)
    # Creamos una instancia de la clase "GestorDescargas_Aplicacion()".
    ventana = GestorDescargas_Aplicacion()
    # Se muestra la pantalla.
    ventana.show()
    # Se indica el método para que cierre la aplicación al pulsar el botón de cerrar.
    sys.exit(app.exec_())