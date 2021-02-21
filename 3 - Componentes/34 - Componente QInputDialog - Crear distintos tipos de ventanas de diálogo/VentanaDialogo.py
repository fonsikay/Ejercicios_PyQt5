# Se importan las librerias necesarias.
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QInputDialog, QLabel, QPushButton


# Creamos la clase "UsoQImputDialog" que va a heredar los métodos de la clase "QDialog".
class UsoQImputDialog(QDialog):

    # Se define el método inicializador de la clase.
    def __init__(self):

        # Se indica el constructor de la clase padre "QDialog".
        super(UsoQImputDialog, self).__init__()
        # Se indica un titulo a la ventana.
        self.setWindowTitle('Uso de QInputDialog')
        # Se indica la posicion que se va a mostrar la ventana y su tamaño.
        self.setGeometry(500, 400, 300, 200)
        # Se crea un boton indicando su texto y que esta contenida en ésta ventana.
        btn_obtener_datos = QPushButton('Obtener datos', self)
        # Se coloca el botón en la ventana indicando su posición.
        btn_obtener_datos.move(30, 30)
        # Se indica el método que se lanza cuando pulse el botón "obtener_datos".
        btn_obtener_datos.clicked.connect(self.obtener_datos)
        # Se muestra la ventana.
        self.show()

    # Se define el método que va a obtener todos los datos.
    def obtener_datos(self):

        # Se crea una label indicando que no tiene texto y estará contenida en ésta ventana.
        lblResultado = QLabel(self)
        # Se coloca la etiqueta en la ventana indicando su posición.
        lblResultado.move(30, 60)

        # Se crea una lista vacía donde se va a almacenar los datos recogidos de la ventana de diálogo.
        lista_valores = []

        # 1 - CAPTURA DE VALORES ENTEROS. Uso del método "getInt()" que muestra un comboBox con el rango de valores.
        # Se llama al "InputDialog()" para que el usuario pueda indicar los valores enteros solicitados.
        # El método "QInputDialog()" devuelve dos variables por lo que la primera es el valor indicado y la segunda es
        # la opción del botón elegido, como no nos interesa dicho valor, pues se pone un "_" en vez de la variable.
        w_entero, _ = QInputDialog.getInt(self,                         # Componente Padre.
                                          'Obtener enteros',            # Titulo de la ventana de diálogo.
                                          'Escriba un número entero:',  # Texto de la ventana de diálogo.
                                          21,                            # Valor por defecto.
                                          0,                            # Valor mínimo elegible.
                                          100,                          # Valor máximo elegible.
                                          1)                            # El aumento del valor va a ser de 1 en 1.
        # Se añade el valor obtenido a la lista "lista_valores".
        lista_valores.append(w_entero)

        # 2 - CAPTURA DE VALORES DECIMALES. Uso del método "getDouble()" que muestra un comboBox con el rango de
        # valores.
        # Se llama al "InputDialog()" para que el usuario pueda indicar los valores decimales solicitados.
        # El método "QInputDialog()" devuelve dos variables por lo que la primera es el valor indicado y la segunda es
        # la opción del botón elegido, como no nos interesa dicho valor, pues se pone un "_" en vez de la variable.
        w_decimales, _ = QInputDialog.getDouble(self,                           # Componente Padre.
                                                'Obtener decimales',            # Titulo de la ventana de diálogo.
                                                'Escriba un número decimal:',   # Texto de la ventana de diálogo.
                                                3.1415,                         # Valor por defecto.
                                                1,                              # Valor mínimo elegible.
                                                100,                            # Valor máximo elegible.
                                                2)                              # El aumento va a ser de 2 en 2.
        # Se añade el valor obtenido a la lista "lista_valores".
        lista_valores.append(w_decimales)

        # 3 - CAPTURA DE UNA OPCIÓN (COLORES DE UNA LISTA). Uso del método "getItem()" que muestra un comboBox con los
        # valores de la lista indicada.
        # Se crea una lista con los colores que puede elegir el usuario.
        lista_colores = ['Rojo', 'Verde', 'Azul']
        # Se llama al "InputDialog()" para que el usuario pueda elegir el color de la lista.
        # El método "QInputDialog()" devuelve dos variables por lo que la primera es el valor indicado y la segunda es
        # la opción del botón elegido, como no nos interesa dicho valor, pues se pone un "_" en vez de la variable.
        w_color, _ = QInputDialog.getItem(self,                # Componente Padre.
                                          'Obtener color',     # Titulo de la ventana de diálogo.
                                          'Escoja su color:',  # Texto de la ventana de diálogo.
                                          lista_colores,       # Lista de valores a elegir.
                                          0,                   # Posición en la lista que tiene el valor inicial (Rojo).
                                          False)               # Se indica que no se pueda añadir valores nuevos a la
                                                               # lista indicada.
        # Se añade el valor obtenido a la lista "lista_valores".
        lista_valores.append(w_color)

        # 4 - CAPTURA DE TEXTO. Uso del método "getText()" que muestra una caja de texto para introducir el texto.
        # Se llama al "InputDialog()" para que el usuario pueda introducir su nombre en la caja de texto.
        # El método "QInputDialog()" devuelve dos variables por lo que la primera es el valor indicado y la segunda es
        # la opción del botón elegido, como no nos interesa dicho valor, pues se pone un "_" en vez de la variable.
        w_nombre, _ = QInputDialog.getText(self,                    # Componente Padre.
                                           'Captura texto',         # Titulo de la ventana de diálogo.
                                           'Escriba su nombre:')    # Texto de la ventana de diálogo.
        # Se añade el valor obtenido a la lista "lista_valores".
        lista_valores.append(w_nombre)

        # Se asigna la lista a la label creada para mostrar los datos introducidos por el usuario.
        lblResultado.setText(', '.join([str(lista_valores_cadena) for lista_valores_cadena in lista_valores]))
        lblResultado.show()


# Hacemos referencia al módulo principal de la aplicación.
if __name__ == '__main__':
    # Creamos una aplicación de nuestra ventana.
    app = QApplication(sys.argv)
    # Creamos una instancia de la clase "UsoQImputDialog()".
    ventana = UsoQImputDialog()
    # Se muestra la pantalla.
    ventana.show()
    # Se indica el método para que cierre la aplicación al pulsar el botón de cerrar.
    sys.exit(app.exec_())