# Se importan las librerias necesarias para actuar en el programa.
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from pymysql import Error
from CreacionTablas_MySQL import frmCreacionTablas
from Conexion import conexion_bbdd

# Se declaran las dos variables "globales" que se van a utilizar para guardar el nº de columnas creadas y la sentencia
# que se crea con todos las columnas a crear en la tabla.
w_num_columna = 0
w_sentencia_columnas = ''


# Se crea la clase Aplicación.
class CreacionTablas_Aplicacion(QDialog):

    # Se crea el método del constructor inicializador.
    def __init__(self):

        # Se invoca el constructor padre.
        super().__init__()
        # Se crea una instancia de nuestra ventana diseñada.
        self.uiVentana = frmCreacionTablas()
        # Se llama al método "setupUi" que esta en la clase "frmCreacionTablas" del archivo "CreacionTablas_MySQL.py".
        self.uiVentana.setupUi(self)
        # Se muestra la pantalla.
        self.show()

        # Declaración de los controladores de eventos (Event Handler).
        self.uiVentana.btnAgregarColumna.clicked.connect(self.agregar_columna)
        self.uiVentana.btnCrearTabla.clicked.connect(self.crear_tabla)

    # Se crea el método que se lanza cuando se pulsa el botón de agregar columna para crearla en la tabla.
    def agregar_columna(self):

        # Se ha tenido que utilizar estas dos variables globales para almacenar varios datos.
        # Almacena el nº de veces que ha pulsado la persona el botón "Agregar campo" ya que si es la primera vez
        # que lo pulsa, no añade la "," antes del nombre del campo pero si ya la ha pulsado una vez, la añade.
        global w_num_columna
        # Almacena las columnas que se van a crear en la nueva tabla.
        global w_sentencia_columnas

        # Si se ha rellenado algo en el campo del nombre de la tabla y del nombre de la columna.
        if len(self.uiVentana.txtNombreTabla.text()) > 0 and len(self.uiVentana.txtNombreColumna.text()) > 0:

            # Si es la primera vez que pulsa el botón de "Agregar columna".
            if w_num_columna == 0:

                # Se guarda el nombre de la columna a crear.
                w_nombrecolumna = self.uiVentana.txtNombreColumna.text()
                # Se guarda el tipo de de la columna a crear.
                w_tipocolumna = self.uiVentana.cmbTipoDato.itemText(self.uiVentana.cmbTipoDato.currentIndex())
                # Se guarda el tamaño de la columna a crear.
                w_tamanocolumna = self.uiVentana.spbTamano.value()

                # Si el tipo de dato que se quiere crear no es de tipo Date.
                if w_tipocolumna != 'DATE':
                    # Se crea la sentencia con el tamaño del campo incluido.
                    w_sentencia_columnas = '{} {}({})'.format(w_nombrecolumna, w_tipocolumna, w_tamanocolumna)
                # Si el tipo de datos es de tipo Date.
                else:
                    # Se crea la sentencia sin el tamaño del campo ya que el Date no tiene tamaño.
                    w_sentencia_columnas = '{} {}'.format(w_nombrecolumna, w_tipocolumna)

                # Se indica que una vez que se haya agregado una columna a la tabla, el nombre de la tabla ya no se
                # puede modificar.
                self.uiVentana.txtNombreTabla.setReadOnly(True)
                # Se aumenta el nº de columnas para indicar que ya se crearía la segunda columna la proxima vez que
                # pulse el botón por lo que ya no entraría en esta condición.
                w_num_columna = w_num_columna + 1

            # Si se ha agregado ya una columna a crear en la tabla.
            else:

                # Se guarda el nombre de la columna a crear.
                w_nombrecolumna = self.uiVentana.txtNombreColumna.text()
                # Se guarda el tipo de de la columna a crear.
                w_tipocolumna = self.uiVentana.cmbTipoDato.itemText(self.uiVentana.cmbTipoDato.currentIndex())
                # Se guarda el tamaño de la columna a crear.
                w_tamanocolumna = self.uiVentana.spbTamano.value()

                # Si el tipo de dato que se quiere crear no es de tipo Date.
                if w_tipocolumna != 'DATE':

                    # Se crea la sentencia con el tamaño del campo incluido.
                    w_sentencia_columnas = w_sentencia_columnas + ', {} {}({})'.format(w_nombrecolumna, w_tipocolumna,
                                                                                       w_tamanocolumna)

                # Si el tipo de datos es de tipo Date.
                else:

                    # Se crea la sentencia sin el tamaño del campo ya que el Date no tiene tamaño.
                    w_sentencia_columnas = w_sentencia_columnas + ', {} {}'.format(w_nombrecolumna, w_tipocolumna)

            # Una vez que se ha creado la columna a agregar se muestran los campos a añadir en el campo de información
            # y se limpian los demás campos incluido poner de nuevo el foco en la caja de texto del nombre de la
            # columnna.
            self.uiVentana.txtInformacion.setText(w_sentencia_columnas)
            self.uiVentana.txtNombreColumna.setText('')
            self.uiVentana.cmbTipoDato.setCurrentIndex(0)
            self.uiVentana.spbTamano.setValue(1)
            self.uiVentana.txtNombreColumna.setFocus()

        # Si no se ha rellenado nada en el campo del nombre de la Tabla.
        elif len(self.uiVentana.txtNombreTabla.text()) == 0:
            # Se crea un mensaje de texto indicando que sea de tipo Información.
            w_mensaje = QMessageBox()
            w_mensaje.setIcon(QMessageBox.Information)
            w_mensaje.setText('Debe escribir el nombre de la Tabla.')
            w_mensaje.setWindowTitle('Mensaje de Información')
            self.uiVentana.txtNombreTabla.setFocus()
            w_mensaje.exec_()

        # Si no se ha rellenado nada en el campo del nombre de la columna.
        elif len(self.uiVentana.txtNombreColumna.text()) == 0:
            # Se crea un mensaje de texto indicando que sea de tipo Información.
            w_mensaje = QMessageBox()
            w_mensaje.setIcon(QMessageBox.Information)
            w_mensaje.setText('Debe escribir el nombre de la columna.')
            w_mensaje.setWindowTitle('Mensaje de Información')
            self.uiVentana.txtNombreColumna.setFocus()
            w_mensaje.exec_()

    # Se crea el método que se lanza cuando se pulsa el botón para crear la tabla con los campos indicados.
    def crear_tabla(self):
        # Almacena las columnas que se van a crear en la nueva tabla.
        global w_sentencia_columnas

        # Se almacena el nombre de la BBDD en una variable para su uso mas fácil.
        w_nombrebbdd = self.uiVentana.txtNombreBBDD.text()
        # Se almacena el nombre de la tabla en una variable para su uso mas fácil.
        w_nombretabla = self.uiVentana.txtNombreTabla.text()

        # Se crea un bloque de excepciones para asi poder controlar si se produce un fallo en la creación de la tabla.
        try:

            # Se crea la sentencia para crear la tabla con el nombre de la BBDD, el de la tabla y las columnas.
            w_sentencia_creartabla = 'CREATE TABLE {}.{} ({})'.format(w_nombrebbdd, w_nombretabla, w_sentencia_columnas)
            # Se crea la conexión de la BBDD utilizando el método "conexion_bbdd" del archivo "Conexion.py".
            w_conexion = conexion_bbdd()
            # Se crea el cursor de conexión.
            w_cursor = w_conexion.cursor()
            # Se ejecuta la sentencia de la creación de la tabla.
            w_cursor.execute(w_sentencia_creartabla)
            # Se cierra el cursor de conexión.
            w_cursor.close()
            # Se cierra la conexión con la BBDD.
            w_conexion.close()
            # Se indica en el campo de información que se ha creado la tabla de forma correcta.
            self.uiVentana.txtInformacion.setText('La tabla "{}" se ha creado de forma correcta.'.format(w_nombretabla))

        # Si se ha producido un error en la creación de la tabla.
        except Error as w_error:

            # Se muestra el error que se ha producido en el campo de información.
            self.uiVentana.txtInformacion.setText('Error: {}'.format(w_error))


# Hacemos referencia al módulo principal de la aplicación.
if __name__ == '__main__':

    # Creamos una aplicación de nuestra ventana.
    app = QApplication(sys.argv)
    # Creamos una instancia de la clase "CreacionTablas_Aplicacion()".
    ventana = CreacionTablas_Aplicacion()
    # Se muestra la pantalla.
    ventana.show()
    # Se indica el método para que cierre la aplicación al pulsar el botón de cerrar.
    sys.exit(app.exec_())
