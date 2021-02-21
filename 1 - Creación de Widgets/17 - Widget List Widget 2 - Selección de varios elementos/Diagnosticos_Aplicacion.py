# Se importan las librerias necesarias.
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from Diagnosticos import frmDiagnostico


# Se crea la clase Aplicación.
class Diagnosticos_Aplicacion(QDialog):

    # Se crea el método del constructor inicializador.
    def __init__(self):

        # Se invoca el constructor padre.
        super().__init__()
        # Se crea una instancia de nuestra ventana diseñada.
        self.uiVentana = frmDiagnostico()
        # Se llama al método "setupUi" que esta en la clase "frmDiagnostico" del archivo "Diagnosticos.py".
        self.uiVentana.setupUi(self)
        # Se muestra la pantalla.
        self.show()

        # Se lanza el evento cuando cambia la selección de un elemento o varios elementos de la lista.
        self.uiVentana.listDiagnosticos.itemSelectionChanged.connect(self.mostrar_seleccion)

    # Se crea el método que se lanza cuando se elige varios elementos de la lista.
    def mostrar_seleccion(self):

        # Se limpia los elementos de la lista.
        self.uiVentana.listDiagnosSelec.clear()
        # Se guarda los elementos marcados de la lista en una variable de tipo lista.
        w_diagnostico_selec = self.uiVentana.listDiagnosticos.selectedItems()

        # Se recorren los elementos de la lista marcados con un bucle "for".
        for r_diagnostico in list(w_diagnostico_selec):
            # Se añaden los elementos seleccionados en la segunda lista.
            self.uiVentana.listDiagnosSelec.addItem(r_diagnostico.text())


# Hacemos referencia al módulo principal de la aplicación.
if __name__ == '__main__':

    # Creamos una aplicación de nuestra ventana.
    app = QApplication(sys.argv)
    # Creamos una instancia de la clase "Diagnosticos_Aplicacion()".
    ventana = Diagnosticos_Aplicacion()
    # Se muestra la pantalla.
    ventana.show()
    # Se indica el método para que cierre la aplicación al pulsar el botón de cerrar.
    sys.exit(app.exec_())
