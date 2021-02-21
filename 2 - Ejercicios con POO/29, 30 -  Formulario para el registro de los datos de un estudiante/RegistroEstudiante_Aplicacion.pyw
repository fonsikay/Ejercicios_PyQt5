# Se importan las librerias necesarias.
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from RegistroEstudiante import frmRegistroEstudiante
from Jerarquia_Herencia_Clases import Estudiante


# Se crea la clase Aplicación.
class RegistroEstudiante_Aplicacion(QDialog):

    # Se crea el método del constructor inicializador.
    def __init__(self):

        # Se invoca el constructor padre.
        super().__init__()
        # Se crea una instancia de nuestra ventana diseñada.
        self.uiVentana = frmRegistroEstudiante()
        # Se llama al método "setupUi" que esta en la clase "frmRegistroEstudiante" del archivo "RegistroEstudiante.py".
        self.uiVentana.setupUi(self)
        # Se muestra la pantalla.
        self.show()

        # Declaración de los controladores de eventos (Event Handler).
        self.uiVentana.btnRegistro.clicked.connect(self.registrar_alumno)

    # Se crea el método que se lanza cuando se pulse el botón de "Registrar".
    def registrar_alumno(self):

        # Se crea un objeto llamado "obj_estudiante" de la clase importada "Estudiante" del archivo
        # "Jerarquia_Herencia_Clases.py" indicando el valor de los campos rellenos en el formulario para cada uno de
        # los atributos de la clase "Estudiante", esto hace que toda la información se quede encapsulada una unica
        # variable pero de tipo Objeto "Estudiante".
        obj_estudiante = Estudiante(self.uiVentana.txtIdentidad.text(), self.uiVentana.txtNombre.text(),
                                    self.uiVentana.txtTelefono.text(), self.uiVentana.txtCarnet.text(),
                                    self.uiVentana.txtCarrera.text())

        '''
        - Ya no se tendría que realizar estas asignaciones de los valores a las variables sino que se guardaría todo
        en el objeto "estudiante" de la clase "Estudiante".
        
        # Se guardan los datos introducidos en los campos de texto en variables.
        self.w_identidad = self.uiVentana.txtIdentidad.text()
        self.w_nombre = self.uiVentana.txtNombre.text()
        self.w_telefono = self.uiVentana.txtTelefono.text()
        self.w_carnet = self.uiVentana.txtCarnet.text()
        self.w_carrera = self.uiVentana.txtCarrera.text()
        '''

        # Se llama al método "mostrar_datos_estudiante" para que muestre los datos almancenados en el objeto en un
        # mensaje por pantalla.
        self.mostrar_datos_estudiante(obj_estudiante)

    # Se crea un método para mostrar los datos del objeto "obj_estudiante" en un mensaje por pantalla.
    def mostrar_datos_estudiante(self, obj_estudiante):

        # Se crea una mensaje por pantalla para poder visualizar los datos rellenados en el formulario.
        ventana_resumen = QMessageBox()
        # Se accede a la información de cada uno de los atributos con el "nombre_objeto"."nombre_atributo".
        ventana_resumen.setText('Nombre: {} - Identidad: {} - Teléfono: {} - Carnet: {} - Carrera: {}'.format(
                        obj_estudiante.nombre_completo, obj_estudiante.identidad, obj_estudiante.telefono,
                        obj_estudiante.carnet, obj_estudiante.carrera))
        # Se ejecuta la pantalla de Mensaje.
        ventana_resumen.exec_()


# Hacemos referencia al módulo principal de la aplicación.
if __name__ == '__main__':

    # Creamos una aplicación de nuestra ventana.
    app = QApplication(sys.argv)
    # Creamos una instancia de la clase "RegistroEstudiante_Aplicacion()".
    ventana = RegistroEstudiante_Aplicacion()
    # Se muestra la pantalla.
    ventana.show()
    # Se indica el método para que cierre la aplicación al pulsar el botón de cerrar.
    sys.exit(app.exec_())
