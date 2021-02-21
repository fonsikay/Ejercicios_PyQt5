# Se importan las librerias necesarias.
import sys
import sqlite3
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from sqlite3 import Error
from CreacionTablas_SQLite3 import frmCreacionTablas
# Se utiliza esta libreria para crear una estructura básica en donde podemos especificar los nombres de los atributos
# para poder almacenar cada nueva columna creada ya que tiene dos atributos "Nombre" y "Tipo de dato".
from collections import namedtuple
# Se utiliza la libreria de expresiones regulares para validar que los datos que se introducen en un campo de texto
# sean válidos, por ejemplo, que un campo no puede contener numeros.
import re


# Creamos la tupla de nombre "Columna" que va a tener dos elementos "Nombre del campo - Tipo de dato".
w_columna = namedtuple('Columna', ['nombre', 'tipo_dato'])


# Se crea la clase Aplicación.
class CreacionTablas_Aplicacion(QDialog):

    # Se crea el método del constructor inicializador.
    def __init__(self):

        # Se invoca el constructor padre.
        super().__init__()
        # Se crea una instancia de nuestra ventana diseñada.
        self.uiVentana = frmCreacionTablas()
        # Se llama al método "setupUi" que esta en la clase "frmCreacionTablas" del archivo "CreacionTablas_SQLite3.py".
        self.uiVentana.setupUi(self)

        # Se crea una instancia de nuestra tupla "Columnas".
        self.w_listacolumnas = []
        # Se indica que el patrón de caracteres que se puede introducir en las cajas de texto sea sólo letras mayúsculas
        # y minúsculas.
        w_patron = '[a-zA-Z]+'
        # Se crea la variable de tipo expresión regular indicando el patrón a aplicar.
        self.w_expreg = re.compile(w_patron)

        # Se crea una instancia de la ventana de mensajes.
        self.w_ventana_mensajes = QMessageBox(self)

        # Se muestra la pantalla.
        self.show()

        # Declaración de los controladores de eventos (Event Handler).
        self.uiVentana.btnAgregarColumna.clicked.connect(self.agregar_columna)
        self.uiVentana.btnCrearBBDD.clicked.connect(self.crear_bbdd)

    # Se crea el método que se lanza cuando se pulsa el botón de "Agregar columna"
    def agregar_columna(self):
        w_nombrecolumna = self.uiVentana.txtNombreColumna.text().strip()

        # Si el texto introducido no cumple con el patrón de la expresión regular va a retornar None por lo que se
        # pregunta si el texto introducido es válido.
        if self.w_expreg.match(w_nombrecolumna) is not None:

            # Se obtiene el tipo de dato elegido por pantalla convertido a cadena de caracteres.
            w_tipo_dato = str(self.uiVentana.cmbTipoDato.currentText())
            # Se añade los datos de la columna a la tupla creda para almacenar la lista de columnas.
            self.w_listacolumnas.append(w_columna(w_nombrecolumna, w_tipo_dato))
            # Se limpia el campo de texto de "Nombre columna".
            self.uiVentana.txtNombreColumna.setText('')
            # Se pone el foco en el campo "Nombre columna".
            self.uiVentana.txtNombreColumna.setFocus()
        # Si el texto introducido no es válido, se muestra un mensaje al usuario.
        else:
            self.w_ventana_mensajes.setText('Debe escribir un nombre de columna válido (sólo caracteres alfabéticos).')
            self.w_ventana_mensajes.setWindowTitle('Nombre de la columna errónea')
            self.w_ventana_mensajes.setIcon(QMessageBox.Warning)
            self.w_ventana_mensajes.exec_()

    # Se crea el método que se lanza cuando se pulsa el botón de "Crear Base de datos".
    def crear_bbdd(self):

        # Se obtiene el nombre de la bbdd a crear quitando los espacios en blanco que pueda tener al inicio y al final
        # de la cadena de caracteres.
        w_nombrebbdd = self.uiVentana.txtNombreBBDD.text().strip()
        # Se obtiene el nombre de la tabla a crear quitando los espacios en blanco que pueda tener al inicio y al final
        # de la cadena de caracteres.
        w_nombretabla = self.uiVentana.txtNombreTabla.text().strip()

        # Comprobamos que el nombre de la BBDD y de la tabla cumplan la expresion regular.
        if self.w_expreg.match(w_nombrebbdd) is not None:
            if self.w_expreg.match(w_nombretabla) is not None:

                # Se comprueba si ya existe alguna columna en la lista de columnas.
                if len(self.w_listacolumnas) > 0:

                    # Se crea la sentencia SQL para crear la tabla.
                    w_sql = f'CREATE TABLE {w_nombretabla}('
                    w_plantilla_campos = '{} {}'
                    w_campos = []

                    for r_columnas in self.w_listacolumnas:
                        w_campos.append(w_plantilla_campos.format(r_columnas.nombre, r_columnas.tipo_dato))

                    w_listacampos = ', '.join(w_campos)

                    w_sql = w_sql + w_listacampos + ')'

                    # Se crea un bloque de excepciones donde se crea la bbdd y se ejecuta la creación de la sentencia
                    # de crear la tabla.

                    try:

                        self.w_conexion = sqlite3.connect(w_nombrebbdd + '.db')
                        self.w_cursor = self.w_conexion.cursor()
                        self.w_cursor.execute(w_sql)
                        self.w_ventana_mensajes.setText(
                            'Se ha creado la Base de datos y la tabla con sus columnas de forma correcta.')
                        self.w_ventana_mensajes.setWindowTitle('Mensaje de información')
                        self.w_ventana_mensajes.setIcon(QMessageBox.Information)
                        self.w_ventana_mensajes.exec_()

                    # Si se ha producido un error, pues se muestra el mensaje por pantalla.
                    except Error as w_error:
                        self.w_ventana_mensajes.setText(
                            'Error al crear la BBDD: . {}'.format(w_error))
                        self.w_ventana_mensajes.setWindowTitle('Tabla sin columnas')
                        self.w_ventana_mensajes.setIcon(QMessageBox.Warning)
                        self.w_ventana_mensajes.exec_()

                    # Al final del bloque siempre hay que cerrar el cursor y la conexión con la BBDD.
                    finally:
                        self.w_cursor.close()
                        self.w_conexion.close()

                # Si no existe columnas en la lista, se muestra un mensaje de error.
                else:
                    self.w_ventana_mensajes.setText(
                        'Debe agregar al menos una columna a la tabla.')
                    self.w_ventana_mensajes.setWindowTitle('Tabla sin columnas')
                    self.w_ventana_mensajes.setIcon(QMessageBox.Warning)
                    self.w_ventana_mensajes.exec_()
            # Si el texto introducido del nombre de la tabla no es válido, se muestra un mensaje al usuario.
            else:
                self.w_ventana_mensajes.setText('Debe escribir un nombre de tabla válido (sólo caracteres alfabéticos).')
                self.w_ventana_mensajes.setWindowTitle('Nombre de la tabla errónea')
                self.w_ventana_mensajes.setIcon(QMessageBox.Warning)
                self.w_ventana_mensajes.exec_()

        # Si el texto introducido del nombre de la base de datos no es válido, se muestra un mensaje al usuario.
        else:
            self.w_ventana_mensajes.setText('Debe escribir un nombre de Base de datos válido (sólo caracteres '
                                            'alfabéticos).')
            self.w_ventana_mensajes.setWindowTitle('Nombre de la Base de datos errónea')
            self.w_ventana_mensajes.setIcon(QMessageBox.Warning)
            self.w_ventana_mensajes.exec_()


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
