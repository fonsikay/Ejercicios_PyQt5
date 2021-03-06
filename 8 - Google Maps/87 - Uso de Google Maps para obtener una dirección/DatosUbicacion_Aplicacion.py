# Se importan las librerias necesarias.
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5.QtGui import QIcon
from googlemaps import Client
from DatosUbicacion import frmDatosUbicacion


# Se crea la clase Aplicación.
class DatosUbicacion_Aplicacion(QDialog):

    # Se crea el método del constructor inicializador.
    def __init__(self):

        # Se invoca el constructor padre.
        super().__init__()
        # Se crea una instancia de nuestra ventana diseñada.
        self.uiVentana = frmDatosUbicacion()
        # Se llama al método "setupUi" que esta en la clase "frmDatosUbicacion" del archivo "DatosUbicacion.py".
        self.uiVentana.setupUi(self)
        # Se indica un icono para la ventana principal.
        self.setWindowIcon(QIcon('icono.ico'))
        # Se indica el tamaño de la ventana para que no se pueda modificar su tamaño.
        self.setFixedSize(522, 251)
        # Se muestra la pantalla.
        self.show()

        # Declaración de los controladores de eventos (Event Handler).
        self.uiVentana.btnBuscar.clicked.connect(self.pro_buscar_direccion)

    # Se crea un método para buscar la dirección en la API de Google Maps.
    def pro_buscar_direccion(self):

        # Se obtiene la localidad a buscar introducida en la caja de texto.
        w_ubicacion = self.uiVentana.txtUbicacion.text().strip()

        # Si se ha introducido algo en la caja de texto de localización.
        if len(w_ubicacion) > 0:

            # Se crea un objeto cliente indicando la clave obtenida de la API de Google Maps.
            # Este codigo es personal y privado por lo que se pone "..." al tener el archivo
            # subido a GitHub.
            w_cliente_google = Client(key='...')
            # Se guardan los datos de la localización en un objeto.
            w_datos = w_cliente_google.geocode(w_ubicacion)[0]

            # Se indican los valores recogidos de Google Maps en los campos de texto.
            self.uiVentana.txtCiudad.setText(w_ubicacion)
            self.uiVentana.txtNombreUbicacion.setText(w_datos['formatted_address'])
            self.uiVentana.txtLatitud.setText(str(w_datos['geometry']['location']['lat']))
            self.uiVentana.txtLongitud.setText(str(w_datos['geometry']['location']['lng']))

        # Si no ha introducido una ubicación, se muestra un mensaje de aviso por pantalla.
        else:

            self.pro_mensaje_un_boton('Advertencia', 'No se ha introducido la ubicación a buscar.', 'Ubicación vacía',
                                      None)
            self.uiVentana.txtUbicacion.setFocus(True)

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


# Hacemos referencia al módulo principal de la aplicación.
if __name__ == '__main__':

    # Creamos una aplicación de nuestra ventana.
    app = QApplication(sys.argv)
    # Creamos una instancia de la clase "DatosUbicacion_Aplicacion()".
    ventana = DatosUbicacion_Aplicacion()
    # Se muestra la pantalla.
    ventana.show()
    # Se indica el método para que cierre la aplicación al pulsar el botón de cerrar.
    sys.exit(app.exec_())
