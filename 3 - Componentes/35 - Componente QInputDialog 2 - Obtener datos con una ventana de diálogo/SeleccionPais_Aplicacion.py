# Se importan las librerias necesarias.
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QInputDialog
from SeleccionPais import frmPais


# Se crea la clase Aplicación.
class SeleccionPais_Aplicacion(QDialog):

    # Se crea el método del constructor inicializador.
    def __init__(self):

        # Se invoca el constructor padre.
        super().__init__()
        # Se crea una instancia de nuestra ventana diseñada.
        self.uiVentana = frmPais()
        # Se llama al método "setupUi" que esta en la clase "frmPais" del archivo "SeleccionPais.py".
        self.uiVentana.setupUi(self)
        # Se muestra la pantalla.
        self.show()

        # Declaración de los controladores de eventos (Event Handler).
        self.uiVentana.btnSeleccionPais.clicked.connect(self.seleccionar_pais)

    # Creación del método que se lanza cuando se hace click en el botón.
    def seleccionar_pais(self):

        # Se crea una variable de tipo lista con los paises elegibles.
        w_lista_paises = ['España', 'Portugal', 'Francia', 'Alemania', 'Suiza', 'Italia', 'Republica Checa', 'EEUU']
        # Se crea la ventana de diálogo de tipo ComboBox para que elija una de las opciones de los paises y se guarde
        # el país elegido y el botón pulsado.
        w_pais, w_boton_pulsado = QInputDialog.getItem(self,
                                                       'País de Nacimiento',
                                                       'Elije tu país de Nacimiento',
                                                       w_lista_paises,
                                                       0,
                                                       False)

        # Si se ha pulsado el botón "Aceptar" de la ventana de diálogo.
        if w_boton_pulsado:
            # Se guarda en la caja de texto el valor del País elegido.
            self.uiVentana.txtPais.setText(w_pais)
        # Si se ha pulsado el botón "Cancelar"
        else:
            # Se muestra un mensaje de aviso en la caja de texto.
            self.uiVentana.txtPais.setText('No ha pulsado el botón Aceptar.')


# Hacemos referencia al módulo principal de la aplicación.
if __name__ == '__main__':

    # Creamos una aplicación de nuestra ventana.
    app = QApplication(sys.argv)
    # Creamos una instancia de la clase "SeleccionPais_Aplicacion()".
    ventana = SeleccionPais_Aplicacion()
    # Se muestra la pantalla.
    ventana.show()
    # Se indica el método para que cierre la aplicación al pulsar el botón de cerrar.
    sys.exit(app.exec_())