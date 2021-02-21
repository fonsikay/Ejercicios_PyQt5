# Se importan las librerias necesarias.
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from ProfesorEmerito import frmProfesorEmerito
from Jerarquia_Clases import Emerito


# Se crea la clase Aplicación.
class ProfesorEmerito_Aplicacion(QDialog):

    # Se crea el método del constructor inicializador.
    def __init__(self):
        # Se invoca el constructor padre.
        super().__init__()
        # Se crea una instancia de nuestra ventana diseñada.
        self.uiVentana = frmProfesorEmerito()
        # Se llama al método "setupUi" que esta en la clase "frmProfesorEmerito" del archivo "ProfesorEmerito.py".
        self.uiVentana.setupUi(self)
        # Se muestra la pantalla.
        self.show()

        # Declaración de los controladores de eventos (Event Handler).
        self.uiVentana.btnRegistrar.clicked.connect(self.registrar_profesor)

    # Se crea el método para obtener los datos introducidos en el formulario y mostrarlos por pantalla.
    def registrar_profesor(self):

        # Se carga la información del formulario en el objeto "obj_emerito".
        obj_emerito = Emerito(self.uiVentana.txtIdentidad.text(),
                              self.uiVentana.txtNombre.text(),
                              self.uiVentana.txtTelefono.text(),
                              self.uiVentana.cmbEspecialidad.itemText(self.uiVentana.cmbEspecialidad.currentIndex()),
                              self.uiVentana.txtReconocimiento.text())

        # Se llama al método para que muestre los datos por pantalla.
        self.mostrar_datos_profesor(obj_emerito)

    # Se crea el método para mostrar los datos por pantalla.
    def mostrar_datos_profesor(self, obj_emerito):

        # Se crea el mensaje y se indica la información a mostrar por pantalla.
        message = QMessageBox()
        message.setText('Identidad: {} - Nombre: {} - Teléfono: {} - Especialidad: {} - Reconocimiento: {}'
                        .format(obj_emerito.identidad, obj_emerito.nombre_completo, obj_emerito.telefono,
                                obj_emerito.especialidad, obj_emerito.reconocimiento))
        message.exec_()


# Hacemos referencia al módulo principal de la aplicación.
if __name__ == '__main__':
    # Creamos una aplicación de nuestra ventana.
    app = QApplication(sys.argv)
    # Creamos una instancia de la clase "ProfesorEmerito_Aplicacion()".
    ventana = ProfesorEmerito_Aplicacion()
    # Se muestra la pantalla.
    ventana.show()
    # Se indica el método para que cierre la aplicación al pulsar el botón de cerrar.
    sys.exit(app.exec_())
