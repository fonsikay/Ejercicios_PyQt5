# Se importan las librerias necesarias.
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QRect, Qt
from BarraMenu import winEditorGrafico


# Se crea la clase Aplicación.
class BarraMenu_Aplicacion(QMainWindow):

    # Se crea el método del constructor inicializador.
    def __init__(self):

        # Se invoca el constructor padre.
        super().__init__()
        # Se crea una instancia de nuestra ventana diseñada.
        self.uiVentana = winEditorGrafico()
        # Se llama al método "setupUi" que esta en la clase "winEditorGrafico" del archivo "BarraMenu.py".
        self.uiVentana.setupUi(self)

        # Declaración de variables necesarias.
        self.w_posicion1 = [0, 0]
        self.w_posicion2 = [0, 0]
        self.w_tipo_dibujo = ''

        # Declaración de los controladores de eventos (Event Handler).
        self.uiVentana.mniDibujar_circulo.triggered.connect(self.dibujar_circulo)
        self.uiVentana.mniDibujar_rectangulo.triggered.connect(self.dibujar_rectangulo)
        self.uiVentana.mniDibujar_linea.triggered.connect(self.dibujar_linea)
        self.uiVentana.mniCopiar.triggered.connect(self.copiar)
        self.uiVentana.mniCortar.triggered.connect(self.cortar)
        self.uiVentana.mniPegar.triggered.connect(self.pegar)
        self.uiVentana.mniEstablecer_contrasena.triggered.connect(self.establecer_password)
        self.uiVentana.mniConfigurar_pagina.triggered.connect(self.configurar_pagina)

        # Se muestra la pantalla.
        self.show()

    # Se sobreescribe el método "paintEvent" predefinido de Python.
    def paintEvent(self, event):

        qp = QPainter()
        qp.begin(self)

        # Se dibuja un circulo.
        # w_posicion1[0]: Eje X
        # w_posicion1[1]: Eje Y
        if self.w_tipo_dibujo == 'circulo':
            w_ancho = self.w_posicion1[0] - self.w_posicion2[0]
            w_alto = self.w_posicion1[1] - self.w_posicion2[1]
            w_rectangulo = QRect(self.w_posicion1[0], self.w_posicion1[1], w_ancho, w_alto)
            w_angulo_inicio = 0
            w_longitud_arco = 360 * 16
            qp.drawArc(w_rectangulo, w_angulo_inicio, w_longitud_arco)

        # Se dibuja un rectángulo.
        # w_posicion1[0]: Eje X
        # w_posicion1[1]: Eje Y
        if self.w_tipo_dibujo == 'rectangulo':
            w_ancho = self.w_posicion2[0] - self.w_posicion1[0]
            w_alto = self.w_posicion2[1] - self.w_posicion1[1]
            qp.drawRect(self.w_posicion1[0], self.w_posicion1[1], w_ancho, w_alto)

        # Se dibuja una línea.
        # w_posicion1[0]: Eje X
        # w_posicion1[1]: Eje Y
        if self.w_tipo_dibujo == 'linea':
            qp.drawLine(self.w_posicion1[0], self.w_posicion1[1], self.w_posicion2[0], self.w_posicion2[1])

        qp.end()

    # Se sobreescribe el método cuando se presiona el botón del raton propio de Python.
    def mousePressEvent(self, event):

        # Si se ha pulsado el botón Izquierdo del ratón.
        if event.buttons() & Qt.LeftButton:

            # Se guarda en las dos variables la posición clicada en el eje X y en el eje Y.
            self.w_posicion1[0], self.w_posicion1[1] = event.pos().x(), event.pos().y()

    def mouseReleaseEvent(self, event):

        # Se guarda en las dos variables la posición clicada en el eje X y en el eje Y.
        self.w_posicion2[0], self.w_posicion2[1] = event.pos().x(), event.pos().y()
        self.update()

    def dibujar_circulo(self):

        self.uiVentana.lblEstado.setText('')
        self.w_tipo_dibujo = 'circulo'

    def dibujar_rectangulo(self):

        self.uiVentana.lblEstado.setText('')
        self.w_tipo_dibujo = 'rectangulo'

    def dibujar_linea(self):

        self.uiVentana.lblEstado.setText('')
        self.w_tipo_dibujo = 'linea'

    def configurar_pagina(self):
        self.uiVentana.lblEstado.setText('Se usó la opción de configurar página.')

    def establecer_password(self):
        self.uiVentana.lblEstado.setText('Se usó la opción de establecer contraseña.')

    def copiar(self):
        self.uiVentana.lblEstado.setText('Se usó la opción de copiar.')

    def cortar(self):
        self.uiVentana.lblEstado.setText('Se usó la opción de cortar.')

    def pegar(self):
        self.uiVentana.lblEstado.setText('Se usó la opción de pegar.')


# Hacemos referencia al módulo principal de la aplicación.
if __name__ == '__main__':

    # Creamos una aplicación de nuestra ventana.
    app = QApplication(sys.argv)
    # Creamos una instancia de la clase "BarraMenu_Aplicacion()".
    ventana = BarraMenu_Aplicacion()
    # Se muestra la pantalla.
    ventana.show()
    # Se indica el método para que cierre la aplicación al pulsar el botón de cerrar.
    sys.exit(app.exec_())
