# Se importan las librerias necesarias.
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from NivelSalud import frmNiveles


# Se crea la clase Aplicación.
class Niveles_Aplicacion(QDialog):

    # Se crea el método del constructor inicializador.
    def __init__(self):

        # Se invoca el constructor padre.
        super().__init__()
        # Se crea una instancia de nuestra ventana diseñada.
        self.uiVentana = frmNiveles()
        # Se llama al método "setupUi" que esta en la clase "frmNiveles" del archivo "NivelSalud.py".
        self.uiVentana.setupUi(self)
        # Se muestra la pantalla.
        self.show()

        # Se indica el método que lanza al modificar el valor del SliderBar Horizontal.
        self.uiVentana.sbhAzucar.valueChanged.connect(self.mostrar_nivel_azucar)
        # Se indica el método que lanza al modificar el valor del SliderBar Vertical.
        self.uiVentana.sbvPulso.valueChanged.connect(self.mostrar_pulso)
        # Se indica el método que lanza al modificar el valor del Slider Horizontal.
        self.uiVentana.slhPresion.valueChanged.connect(self.mostrar_presion_arterial)
        # Se indica el método que lanza al modificar el valor del SliderBar Vertical.
        self.uiVentana.slvColesterol.valueChanged.connect(self.mostrar_nivel_colesterol)

    # Se define el método "mostrar_nivel_azucar" llamado al modificar el valor del SliderBar Horizontal "sbhAzucar".
    # Se pasa internamente el valor del Slider en una variable llamada "valor".
    def mostrar_nivel_azucar(self, valor):

        self.uiVentana.txtResultado.setText('Nivel de azucar: {}'.format(valor))

    # Se define el método "mostrar_pulso" llamado al modificar el valor del SliderBar Vertical "sbvPulso".
    # Se pasa internamente el valor del Slider en una variable llamada "valor".
    def mostrar_pulso(self, valor):

        self.uiVentana.txtResultado.setText('Pulso: {}'.format(valor))

    # Se define el método "mostrar_presion_arterial" llamado al modificar el valor del Slider Horizontal "slhPresion".
    # Se pasa internamente el valor del Slider en una variable llamada "valor".
    def mostrar_presion_arterial(self, valor):

        self.uiVentana.txtResultado.setText('Presión arterial: {}'.format(valor))

    # Se define el método "mostrar_nivel_colesterol" llamado al modificar el valor del Slider Vertical "slvColesterol".
    # Se pasa internamente el valor del Slider en una variable llamada "valor".
    def mostrar_nivel_colesterol(self, valor):

        self.uiVentana.txtResultado.setText('Nivel de Colesterol: {}'.format(valor))


# Hacemos referencia al módulo principal de la aplicación.
if __name__ == '__main__':

    # Creamos una aplicación de nuestra ventana.
    app = QApplication(sys.argv)
    # Creamos una instancia de la clase "Niveles_Aplicacion()".
    ventana = Niveles_Aplicacion()
    # Se muestra la pantalla.
    ventana.show()
    # Se indica el método para que cierre la aplicación al pulsar el botón de cerrar.
    sys.exit(app.exec_())