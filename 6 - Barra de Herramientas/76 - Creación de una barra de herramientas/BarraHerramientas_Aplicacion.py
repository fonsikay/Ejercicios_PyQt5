# Se importan las librerias necesarias.
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtGui import QIcon
from BarraHerramientas import frmBarraHerramientas
from InsertarRegistrosMySQL_Aplicacion import InsertarRegistrosMySQL_Aplicacion
from BusquedaUsuario_Aplicacion import BusquedaUsuario_Aplicacion
from EliminarUsuario_Aplicacion import EliminarUsuario_Aplicacion


# Se crea la clase Aplicación.
class BarraHerramientas_Aplicacion(QMainWindow):

    # Se crea el método del constructor inicializador.
    def __init__(self, parent=None):

        # Se invoca el constructor padre.
        super().__init__(parent)
        # Se crea una instancia de nuestra ventana diseñada.
        self.uiVentana = frmBarraHerramientas()
        # Se llama al método "setupUi" que esta en la clase "frmBarraHerramientas" del archivo "BarraHerramientas.py".
        self.uiVentana.setupUi(self)
        # Se indica un icono para la ventana principal.
        self.setWindowIcon(QIcon('icono.ico'))
        # Se indica el tamaño de la ventana para que no se pueda modificar su tamaño.
        self.setFixedSize(474, 361)

        # Se muestra la pantalla.
        self.show()

        # Declaración de los controladores de eventos (Event Handler).
        self.uiVentana.mniNuevo.triggered.connect(self.pro_nuevo_usuario)
        self.uiVentana.mniBuscar.triggered.connect(self.pro_buscar_usuario)
        self.uiVentana.mniEliminar.triggered.connect(self.pro_eliminar_usuario)

    # Se crea el método que llama a la ventana de inserción de datos de la clase "InsertarRegistrosMySQL_Aplicacion".
    def pro_nuevo_usuario(self):

        # Se comprueba con el método "hasattr()", si en nuestra ventana actual "self", el objeto "w_ven_nuevo_usuario"
        # no existe y eso querrá decir que la nueva ventana no se está mostrando.
        if not hasattr(self, 'w_ven_nuevo_usuario'):
            # Se crea un objeto de la ventana secundaria "Nuevo usuario" siendo totalmente necesario que tenga el
            # "self" delante y que esta variable no se declare en el "__init__".
            self.w_ven_nuevo_usuario = InsertarRegistrosMySQL_Aplicacion(self)

        # Se muestra la ventana de "Nuevo Usuario".
        self.w_ven_nuevo_usuario.show()

    # Se crea el método que llama a la ventana de busqueda de usuario de la clase "BusquedaUsuario_Aplicacion".
    def pro_buscar_usuario(self):

        # Se comprueba con el método "hasattr()", si en nuestra ventana actual "self", el objeto "w_ven_buscar_usuario"
        # no existe y eso querrá decir que la nueva ventana no se está mostrando.
        if not hasattr(self, 'w_ven_buscar_usuario'):

            # Se crea un objeto de la ventana secundaria "Buscar usuario" siendo totalmente necesario que tenga el
            # "self" delante y que esta variable no se declare en el "__init__"
            self.w_ven_buscar_usuario = BusquedaUsuario_Aplicacion(self)

        # Se muestra la ventana de "Buscar Usuario".
        self.w_ven_buscar_usuario.show()

    # Se crea el método que llama a la ventana para el borrado de datos de la clase "EliminarUsuario_Aplicacion".
    def pro_eliminar_usuario(self):

        # Se comprueba con el método "hasattr()", si en nuestra ventana actual "self", el objeto "w_ven_buscar_usuario"
        # no existe y eso querrá decir que la nueva ventana no se está mostrando.
        if not hasattr(self, 'w_ven_eliminar_usuario'):

            # Se crea un objeto de la ventana secundaria "Eliminar usuario" siendo totalmente necesario que tenga el
            # "self" delante y que esta variable no se declare en el "__init__"
            self.w_ven_eliminar_usuario = EliminarUsuario_Aplicacion(self)

        # Se muestra la ventana de "Eliminar Usuario".
        self.w_ven_eliminar_usuario.show()

    # Se crea un método para mostrar una ventana de mensaje que contiene el botón "Aceptar".
    def pro_mensaje_un_boton(self, w_tipo_ventana, w_mensaje, w_titulo, w_mensaje_secundario):

        # Se crea un objeto de tipo ventana de mensaje.
        w_ventana_mensaje = QMessageBox()
        # Se muestra el mensaje al usuario indicado.
        w_ventana_mensaje.setText(w_mensaje)

        # Según sea el tipo de mensaje indicado, se elige un tipo de icono para la ventana.
        if w_tipo_ventana == 'Consulta':
            w_ventana_mensaje.setIcon(QMessageBox.Question)
        elif w_tipo_ventana == 'Información':
            w_ventana_mensaje.setIcon(QMessageBox.Information)
        elif w_tipo_ventana == 'Advertencia':
            w_ventana_mensaje.setIcon(QMessageBox.Warning)
        elif w_tipo_ventana == 'Error':
            w_ventana_mensaje.setIcon(QMessageBox.Critical)
        else:
            w_ventana_mensaje.setIcon(QMessageBox.NoIcon)

        # Se indica el titulo de la ventana indicado.
        w_ventana_mensaje.setWindowTitle(w_titulo)
        # Se indica el icono de la ventana.
        w_ventana_mensaje.setWindowIcon(QIcon('icono.ico'))
        # Se indica el mensaje secundario indicado.
        w_ventana_mensaje.setInformativeText(w_mensaje_secundario)

        # Se añade el botón de "Aceptar" con el estilo de la aplicación.
        w_boton_aceptar = w_ventana_mensaje.addButton(self.tr("Aceptar"), QMessageBox.AcceptRole)
        w_boton_aceptar.setStyleSheet('QPushButton {color: #ffffff;text-align: center;background-color: '
                                      'qlineargradient(spread:pad, x1:1, y1:0.545, x2:1, y2:0, stop:0 #b6b6b6, stop:1 '
                                      '#e6e6e6);border: 1px solid #828282;padding: 5px 12px 5px 12px;margin: 4px 8px '
                                      '4px 8px;border-radius: 3px;min-width: 14px;min-height: 14px;}QPushButton:hover{'
                                      'color: white;background-color: qlineargradient(spread:pad, x1:1, y1:0.545, x2:1,'
                                      ' y2:0, stop:0 #2eae35, stop:1 #cae44a);}QPushButton:pressed {background-color: '
                                      '#2eae35;}')
        # Se muestra la ventana de aviso.
        w_ventana_mensaje.exec_()

    # Se crea un método para mostrar una ventana de mensaje que contiene el botón "Aceptar" y "Cancelar".
    def fun_mensaje_dos_botones(self, w_tipo_ventana, w_mensaje, w_titulo, w_mensaje_secundario):

        # Se crea un objeto de tipo ventana de mensaje.
        w_ventana_mensaje = QMessageBox()
        # Se muestra el mensaje al usuario indicado.
        w_ventana_mensaje.setText(w_mensaje)

        # Según sea el tipo de mensaje indicado, se elige un tipo de icono para la ventana.
        if w_tipo_ventana == 'Consulta':
            w_ventana_mensaje.setIcon(QMessageBox.Question)
        elif w_tipo_ventana == 'Información':
            w_ventana_mensaje.setIcon(QMessageBox.Information)
        elif w_tipo_ventana == 'Advertencia':
            w_ventana_mensaje.setIcon(QMessageBox.Warning)
        elif w_tipo_ventana == 'Error':
            w_ventana_mensaje.setIcon(QMessageBox.Critical)
        else:
            w_ventana_mensaje.setIcon(QMessageBox.NoIcon)

        # Se indica el titulo de la ventana indicado.
        w_ventana_mensaje.setWindowTitle(w_titulo)
        # Se indica el icono de la ventana.
        w_ventana_mensaje.setWindowIcon(QIcon('icono.ico'))
        # Se indica el mensaje secundario indicado.
        w_ventana_mensaje.setInformativeText(w_mensaje_secundario)

        # Se añade los botones de Aceptar y Cancelar con el estilo de la aplicación.
        w_boton_aceptar = w_ventana_mensaje.addButton(self.tr("Aceptar"), QMessageBox.AcceptRole)
        w_boton_aceptar.setStyleSheet('QPushButton {color: #ffffff;text-align: center;background-color: '
                                      'qlineargradient(spread:pad, x1:1, y1:0.545, x2:1, y2:0, stop:0 #b6b6b6, stop:1 '
                                      '#e6e6e6);border: 1px solid #828282;padding: 5px 12px 5px 12px;margin: 4px 8px '
                                      '4px 8px;border-radius: 3px;min-width: 14px;min-height: 14px;}QPushButton:hover{'
                                      'color: white;background-color: qlineargradient(spread:pad, x1:1, y1:0.545, x2:1,'
                                      ' y2:0, stop:0 #2eae35, stop:1 #cae44a);}QPushButton:pressed {background-color: '
                                      '#2eae35;}')
        w_boton_cancelar = w_ventana_mensaje.addButton(self.tr("Cancelar"), QMessageBox.RejectRole)
        w_boton_cancelar.setStyleSheet('QPushButton {color: #ffffff; text-align: center; background-color: '
                                       'qlineargradient(spread:pad, x1:1, y1:0.545, x2:1, y2:0, stop:0 #b6b6b6, stop:1 '
                                       '#e6e6e6); border: 1px solid #828282; padding: 5px 12px 5px 12px; margin: 4px '
                                       '8px 4px 8px; border-radius: 3px; min-width: 14px; min-height: 14px;}'
                                       'QPushButton:hover{color: white;background-color: qlineargradient(spread:pad, '
                                       'x1:1, y1:0.545, x2:1, y2:0, stop:0 #95050d, stop:1 #ea0a20);} '
                                       'QPushButton:pressed {background-color: #95050d;}')

        # Se muestra la ventana de aviso.
        w_ventana_mensaje.exec_()

        # Si se ha pulsado el botón de aceptar, pues se cierra la aplicación y si pulsa el de cancenlar, pues no hace
        # nada.
        if w_ventana_mensaje.clickedButton() == w_boton_aceptar:
            return 'Aceptar'
        elif w_ventana_mensaje.clickedButton() == w_boton_cancelar:
            return 'Cancelar'


# Hacemos referencia al módulo principal de la aplicación.
if __name__ == '__main__':

    # Creamos una aplicación de nuestra ventana.
    app = QApplication(sys.argv)
    # Creamos una instancia de la clase "BarraHerramientas_Aplicacion()".
    ventana = BarraHerramientas_Aplicacion()
    # Se muestra la pantalla.
    ventana.show()
    # Se indica el método para que cierre la aplicación al pulsar el botón de cerrar.
    sys.exit(app.exec_())
