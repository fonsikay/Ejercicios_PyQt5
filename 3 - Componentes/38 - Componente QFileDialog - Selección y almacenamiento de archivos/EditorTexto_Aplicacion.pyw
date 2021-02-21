# Se importan las librerias necesarias.
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from EditorTexto import vntEditorTexto
from PyQt5.QtGui import QIcon


# Se crea la clase Aplicación.
class EditorTexto_Aplicacion(QMainWindow):

    # Se crea el método del constructor inicializador.
    def __init__(self):

        # Se invoca el constructor padre.
        super().__init__()
        # Se crea una instancia de nuestra ventana diseñada.
        self.uiVentana = vntEditorTexto()
        # Se llama al método "setupUi" que esta en la clase "vntEditorTexto" del archivo "EditorTexto.py".
        self.uiVentana.setupUi(self)
        # Se indica el tamaño (x, y) que va a tener la ventana forzando a que no se pueda modificar su tamaño.
        self.setFixedSize(519, 409)
        # Se indica un icono para la ventana.
        self.setWindowIcon(QIcon('editor.ico'))
        # Se muestra la pantalla.
        self.show()

        # Declaración de los controladores de eventos (Event Handler) del menú.
        self.uiVentana.mniAbrir.triggered.connect(self.abrir_archivo)
        self.uiVentana.mniGuardar.triggered.connect(self.guardar_archivo)
        self.uiVentana.mniSalir.triggered.connect(self.salir_app)

    # Se crea el método que se lanza cuando se pulsa en el menú en la opción "Abrir".
    def abrir_archivo(self):

        # Se abre la ventana de "Abrir archivo" y se almacena el archivo seleccionado en una variable de tipo Objeto.
        w_archivo = QFileDialog.getOpenFileName(self,                   # Contenedor padre.
                                                'Abrir archivo',        # Titulo de la ventana.
                                                'D:\\',                 # Directorio donde se abre por defecto.
                                                'Archivo texto (.txt)'  # Tipo de archivo a abrir.
                                                )

        # Se comprueba si se ha almacenado el archivo de forma correcta.
        if w_archivo[0]:
            # Se abre el archivo que se ha seleccionado en la ventana indicando que es de lectura de texto "rt".
            with open(w_archivo[0], 'rt') as f:
                # Se lee el contenido del archivo abierto y se guarda el contenido en una variable.
                w_datos = f.read()
                # Se indica el texto del archivo abierto en el Edit Text de nuestra pantalla.
                self.uiVentana.txteTexto.setText(w_datos)

    # Se crea el método que se lanza cuando se pulsa en el menú en la opción "Guardar".
    def guardar_archivo(self):

        # Se almacena el archivo a guardar en una variable de tipo Objeto.
        w_opciones = QFileDialog.Options()
        # Se indica, como prueba, que la ventana a mostrar no sea la nativa de Windows sino la propia de PyQt5.
        w_opciones |= QFileDialog.DontUseNativeDialog
        # Se abre la ventana de "Guardar archivo" y se almacena el archivo a guardar en una variable de tipo Objeto.
        w_archivo, w_boton_sel = QFileDialog.getSaveFileName(self,                    # Contenedor padre.
                                                             'Guardar archivo',       # Titulo de la ventana.
                                                             'D:\\',                  # Directorio donde se abre por
                                                                                      # defecto.
                                                             'Archivo texto (.txt)',  # Tipo de archivo a abrir.
                                                             options = w_opciones)

        # Se comprueba si se ha pulsado el botón de "Guardar".
        if w_boton_sel:
            # Se abre el archivo que se ha seleccionado en la ventana indicando que es de escritura de texto "wt".
            with open(w_archivo, 'wt') as f:
                # Se escribe el contenido del Edit Text en el archivo a guardar pero como los archivo ".txt" son de
                # texto plano, se utiliza el método "toPlainText()".
                f.write(self.uiVentana.txteTexto.toPlainText())

    # Se crea el método que se lanza cuando se pulsa en el menú en la opción "Salir".
    def salir_app(self):
        # Se indica que cierre la aplicación.
        sys.exit(0)


# Hacemos referencia al módulo principal de la aplicación.
if __name__ == '__main__':

    # Creamos una aplicación de nuestra ventana.
    app = QApplication(sys.argv)
    # Creamos una instancia de la clase "EditorTexto_Aplicacion()".
    ventana = EditorTexto_Aplicacion()
    # Se muestra la pantalla.
    ventana.show()
    # Se indica el método para que cierre la aplicación al pulsar el botón de cerrar.
    sys.exit(app.exec_())
