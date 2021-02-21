# Se importan las librerias necesarias.
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QInputDialog, QListWidgetItem
from ComidaFavorita import frmComidaFavorita


# Se crea la clase Aplicación.
class ComidaFavorita_Aplicacion(QDialog):

    # Se crea el método del constructor inicializador.
    def __init__(self):

        # Se invoca el constructor padre.
        super().__init__()
        # Se crea una instancia de nuestra ventana diseñada.
        self.uiVentana = frmComidaFavorita()
        # Se llama al método "setupUi" que esta en la clase "frmComidaFavorita" del archivo "ComidaFavorita.py".
        self.uiVentana.setupUi(self)
        # Se muestra la pantalla.
        self.show()

        # Se indican los módulos que se llaman al activar el evento de pulsar los botones.
        self.uiVentana.btnAnadir.clicked.connect(self.anadir_elemento_lista)
        self.uiVentana.btnEditar.clicked.connect(self.editar_elemento_lista)
        self.uiVentana.btnEliminar.clicked.connect(self.eliminar_elemento_lista)
        self.uiVentana.btnEliminarTodo.clicked.connect(self.eliminar_todo_lista)

        # Se precarga la lista con algunos elementos iniciales.
        self.uiVentana.listComida.addItem('Pizza')
        self.uiVentana.listComida.addItem('Macarrones')
        self.uiVentana.listComida.addItem('Filete de pollo empanado')

    # Se crea el método para el evento de añadir un elemento a la lista.
    def anadir_elemento_lista(self):
        # Se obtiene el texto de la caja de texto.
        w_elemento = self.uiVentana.txtComida.text()
        # Se añade como nuevo elemento el texto a la lista.
        self.uiVentana.listComida.addItem(w_elemento)
        # Se limpia la caja de texto.
        self.uiVentana.txtComida.setText('')
        # Se pone el foco de nuevo en la caja de texto.
        self.uiVentana.txtComida.setFocus()

    # Se crea el método para el evento de editar un elemento de la lista.
    def editar_elemento_lista(self):

        # Se obtiene la posición o fila donde se encuentra en la lista nuestro elemento a modificar.
        w_posicion_elemento_a_modificar = self.uiVentana.listComida.currentRow()
        # Se crea una ventana de diálogo para solicitar al usuario cual va a ser el nuevo nombre del elemento a
        # modificar de la lista.
        # El método "getText" devuelve dos valores: el texto del nombre a modificar y el valor del botón pulsado en
        # la ventana de diálogo.
        w_nuevo_nombre, w_boton_pulsado = QInputDialog.getText(self, 'Editar comida', 'Ingrese el nuevo nombre: ')

        # Si se ha pulsado el botón de la ventana de diálogo y se ha escrito algo en la caja de texto de la ventana
        # de diálogo.
        if w_boton_pulsado == True and len(w_nuevo_nombre) > 0:

            # Se elimina de la lista el elemento a modificar.
            self.uiVentana.listComida.takeItem(w_posicion_elemento_a_modificar)
            # Se inserta el nuevo elemento modificado en la posición de la lista del elemento a modificar con el texto
            # que se ha indicado en la ventana de diálogo.
            self.uiVentana.listComida.insertItem(w_posicion_elemento_a_modificar, QListWidgetItem(w_nuevo_nombre))

    # Se crea el método para eliminar el elemento de la lista.
    def eliminar_elemento_lista(self):
        # Se obtiene la posición o fila donde se encuentra en la lista nuestro elemento a eliminar.
        w_posicion_elemento_a_borrar = self.uiVentana.listComida.currentRow()
        # Se elimina de la lista el elemento a borrar.
        self.uiVentana.listComida.takeItem(w_posicion_elemento_a_borrar)

    # Se crea el método para eliminar todos los elementos de la lista.
    def eliminar_todo_lista(self):
        # Se limpia la lista.
        self.uiVentana.listComida.clear()
        # Se limpia la caja de texto.
        self.uiVentana.txtComida.setText('')
        # Se pone el foco de nuevo en la caja de texto.
        self.uiVentana.txtComida.setFocus()


# Hacemos referencia al módulo principal de la aplicación.
if __name__ == '__main__':

    # Creamos una aplicación de nuestra ventana.
    app = QApplication(sys.argv)
    # Creamos una instancia de la clase "Diagnosticos_Aplicacion()".
    ventana = ComidaFavorita_Aplicacion()
    # Se muestra la pantalla.
    ventana.show()
    # Se indica el método para que cierre la aplicación al pulsar el botón de cerrar.
    sys.exit(app.exec_())
