# Se importan las librerias necesarias.
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidgetItem
from TablaLenguajes import frmTabla


# Se crea la clase Aplicación.
class TablaLenguajes_Aplicacion(QDialog):

    # Se crea el método del constructor inicializador.
    def __init__(self):

        # Se invoca el constructor padre.
        super().__init__()
        # Se crea una instancia de nuestra ventana diseñada.
        self.uiVentana = frmTabla()
        # Se llama al método "setupUi" que esta en la clase "frmTabla" del archivo "TablaLenguajes.py".
        self.uiVentana.setupUi(self)
        # Se muestra la pantalla.
        self.show()

        # Se llama al método "inicializar_datos()" para indicar los datos a insertar en la tabla.
        self.inicializar_datos()

        # Se llama al método "agregar.contenido_tabla()" para añadir los elementos de la lista a la tabla.
        self.agregar_contenido_tabla()

    # Se crea un método para inicializar los datos que se van a insertar en la tabla.
    def inicializar_datos(self):
        # Se crea una lista que va a contener los datos que se quieren cargar en la tabla pero se crea vacía de forma
        # inicial.
        self.w_datos = []

        # Se añade todos los registro a cargar en la lista con los datos de cada fila, primero el nombre y
        # luego la versión.
        self.w_datos.append(('Python', '3.7.3'))
        self.w_datos.append(('Java', '8'))
        self.w_datos.append(('PHP', '7.3'))
        self.w_datos.append(('C#', '8'))
        self.w_datos.append(('C++', '17'))

    # Se crea un método para cargar los datos de la lista creada en la tabla.
    def agregar_contenido_tabla(self):

        # Se crea un contador de fila.
        w_numfila = 0

        # Se recorre la lista de datos creada fuera de éste método que se va a utilizar para rellenar la tabla.
        for r_filas in self.w_datos:

            # Se crea un contador de columna.
            w_numcolumna = 0
            # Cada vez que haya una columna nueva, pues se inserta una nueva fila con la posición del contador de fila.
            self.uiVentana.tabLenguajes.insertRow(w_numfila)

            # Se recorren las columnas para cada una de las filas.
            for r_columnas in r_filas:

                # Se guarda la información que se va a insertar en cada una de las celdas de la tabla.
                w_datos_celda = QTableWidgetItem(r_columnas)

                # Se inserta en cada una de las celdas, la información a añadir en la tabla indicando la fila y la
                # columna donde se va a guardar.
                self.uiVentana.tabLenguajes.setItem(w_numfila, w_numcolumna, w_datos_celda)

                # Se aumenta el contador de columnas.
                w_numcolumna = w_numcolumna + 1

            # Se aumenta el contador de filas.
            w_numfila = w_numfila + 1


# Hacemos referencia al módulo principal de la aplicación.
if __name__ == '__main__':

    # Creamos una aplicación de nuestra ventana.
    app = QApplication(sys.argv)
    # Creamos una instancia de la clase "TablaLenguajes_Aplicacion()".
    ventana = TablaLenguajes_Aplicacion()
    # Se muestra la pantalla.
    ventana.show()
    # Se indica el método para que cierre la aplicación al pulsar el botón de cerrar.
    sys.exit(app.exec_())
