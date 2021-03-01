# Se importan las librerias necesarias.
import sys
import re

from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5.QtGui import QIcon
from pymysql import Error
from Conexion_PHPMyAdmin import conexion_bbdd
from passlib.hash import pbkdf2_sha256
from ModificarContrasena_UI import frmModificarContrasena


# Se crea la clase Aplicación.
class ModificarContrasena_App(QDialog):

    # Se crea el método del constructor inicializador.
    def __init__(self, w_usuario):

        # Se invoca el constructor padre.
        super().__init__()

        self.w_usuario = w_usuario

        # Se crea una instancia de nuestra ventana diseñada.
        self.uiVentana = frmModificarContrasena()
        # Se llama al método "setupUi" que esta en la clase "frmModificarContrasena" del archivo
        # "ModificarContrasena_UI.py".
        self.uiVentana.setupUi(self)
        # Se indica un icono para la ventana principal.
        self.setWindowIcon(QIcon('icono.ico'))
        # Se indica el tamaño de la ventana para que no se pueda modificar su tamaño.
        self.setFixedSize(380, 200)
        # Se muestra la pantalla.
        self.show()

        # Se indica un texto predefinido para ayudar al usuario a saber que el usuario corresponde con el email.
        self.uiVentana.txtUsuario.setPlaceholderText('example@gmail.com')
        # Se indica un texto predefinido para ayudar al usuario a saber que la contraseña son 10 caracteres
        # alfanuméricos
        self.uiVentana.txtContrasena.setPlaceholderText('10 caracteres alfanuméricos')
        # Se indica que el límite de tamaño a introducir es de 20 caracteres.
        self.uiVentana.txtContrasena.setMaxLength(20)

        # Se indica el codigo de usuario a modificar que viene de la ventana de inicio de sesión.
        self.uiVentana.txtUsuario.setText(self.w_usuario)
        # Se deshabilita el cuadro de texto del usuario.
        self.uiVentana.txtUsuario.setEnabled(False)

        # Se deshabilita el botón de "Modificar" y se crean dos variables donde se indican si se ha validado
        # las dos contraseñas.
        self.uiVentana.btnModificar.setEnabled(False)
        self.w_validacion_contrasena = False
        self.w_validacion_nueva_contrasena = False

        # Se crea la variable de conexión y de cursor para que se pueda utilizar en el programa.
        self.w_conexion = None

        # Declaración de los controladores de eventos (Event Handler).
        self.uiVentana.btnModificar.clicked.connect(self.pro_modificar_contrasena)
        self.uiVentana.btnCancelar.clicked.connect(self.pro_cancelar_sesion)
        self.uiVentana.txtContrasena.textChanged.connect(self.pro_validar_contrasena)
        self.uiVentana.txtNuevaContrasena.textChanged.connect(self.pro_validar_nueva_contrasena)


    # Se declara el método que se lanza cuando se modifica el texto de la caja de la contraseña.
    def pro_validar_contrasena(self):

        w_contrasena = self.uiVentana.txtContrasena.text().strip()

        # Se aplica el patrón de validación para los campos de texto alfanuméricos.
        w_patron = '^[a-zA-Z0-9]*$'
        # Se indica que el campo a comprobar es la contraseña y se guarda en una variable.
        w_validar_contrasena = re.match(w_patron, w_contrasena, re.I)

        # Si la contraseña esta vacía.
        if w_contrasena == '':
            # Se quita la imagen de error auxiliar.
            self.uiVentana.btnValidaContrasena.setStyleSheet('image: url();')
            # Se indica que la contraseña no esta validada.
            self.w_validacion_contrasena = False

            # Se comprueba la validación de los campos para activar o no el botón "Iniciar Sesión".
            self.pro_comprobar_estado_boton_aceptar()

        # Si la contraseña no ha sido validada por el patrón de alfanuméricos.
        elif not w_validar_contrasena:

            # Se quita la imagen de error auxiliar.
            self.uiVentana.btnValidaContrasena.setStyleSheet('image: url(:/iconos/iconos/dato_erroneo.ico);')
            # Se indica que la contraseña no esta validada.
            self.w_validacion_contrasena = False

            # Se comprueba la validación de los campos para activar o no el botón "Iniciar Sesión".
            self.pro_comprobar_estado_boton_aceptar()

        # Si la contraseña ha sido rellena y validada por el patrón.
        else:

            # Se muestra la imagen de campo validado auxiliar.
            self.uiVentana.btnValidaContrasena.setStyleSheet('image: url(:/iconos/iconos/dato_correcto.ico);')
            # Se indica que la contraseña esta validada.
            self.w_validacion_contrasena = True

    # Se declara el método que se lanza cuando se modifica el texto de la caja de la contraseña.
    def pro_validar_nueva_contrasena(self):

        w_contrasena = self.uiVentana.txtNuevaContrasena.text().strip()

        # Se aplica el patrón de validación para los campos de texto alfanuméricos.
        w_patron = '^[a-zA-Z0-9]*$'
        # Se indica que el campo a comprobar es la contraseña y se guarda en una variable.
        w_validar_contrasena = re.match(w_patron, w_contrasena, re.I)

        # Si la contraseña esta vacía.
        if w_contrasena == '':
            # Se quita la imagen de error auxiliar.
            self.uiVentana.btnValidaNuevaContrasena.setStyleSheet('image: url();')
            # Se indica que la contraseña no esta validada.
            self.w_validacion_nueva_contrasena = False

            # Se comprueba la validación de los campos para activar o no el botón "Iniciar Sesión".
            self.pro_comprobar_estado_boton_aceptar()

        # Si la contraseña no ha sido validada por el patrón de alfanuméricos.
        elif not w_validar_contrasena:

            # Se quita la imagen de error auxiliar.
            self.uiVentana.btnValidaNuevaContrasena.setStyleSheet('image: url(:/iconos/iconos/dato_erroneo.ico);')
            # Se indica que la contraseña no esta validada.
            self.w_validacion_nueva_contrasena = False

            # Se comprueba la validación de los campos para activar o no el botón "Iniciar Sesión".
            self.pro_comprobar_estado_boton_aceptar()

        # Si la contraseña ha sido rellena y validada por el patrón.
        else:

            # Se muestra la imagen de campo validado auxiliar.
            self.uiVentana.btnValidaNuevaContrasena.setStyleSheet('image: url(:/iconos/iconos/dato_correcto.ico);')
            # Se indica que la contraseña esta validada.
            self.w_validacion_nueva_contrasena = True

            # Se comprueba la validación de los campos para activar o no el botón "Iniciar Sesión".
            self.pro_comprobar_estado_boton_aceptar()

    # Se crea un método que comprueba si tanto el usuario como la contraseña estan validados para activar el botón de
    # "Iniciar sesión", mientras tanto, estará desactivado.
    def pro_comprobar_estado_boton_aceptar(self):

        # Si la validación de los dos campos se ha realizado de forma correcta, se activa el botón "Iniciar sesión".
        if self.w_validacion_nueva_contrasena and self.w_validacion_contrasena:
            self.uiVentana.btnModificar.setEnabled(True)
        else:
            self.uiVentana.btnModificar.setEnabled(False)

    # Se crea el método que modifica la contraseña del usuario en la BBDD.
    def pro_modificar_contrasena(self):

        w_usuario = self.uiVentana.txtUsuario.text().strip()
        w_antigua_contrasena = self.uiVentana.txtContrasena.text().strip()
        w_nueva_contrasena = self.uiVentana.txtNuevaContrasena.text().strip()

        # Si la nueva contraseña es distinta a la anterior contraseña.
        if w_antigua_contrasena != w_nueva_contrasena:

            # Se crea la nueva contraseña de forma encriptada.
            w_nueva_contrasena_encriptada = pbkdf2_sha256.hash(w_nueva_contrasena)

            # Se realiza la conexion a la BBDD.
            self.pro_conexion_bbdd()

            # Si la conexión ha sido correcta y w_conexion no esta vacía.
            if self.w_conexion is not None:

                # Se actualiza la contraseña encriptada para el usuario indicado.
                w_cursor = self.w_conexion.cursor()
                w_sentencia_sql = '''UPDATE curso_pyqt.usuarios SET password = '{}' WHERE email = '{}' '''\
                                  .format(w_nueva_contrasena_encriptada, w_usuario)
                print(w_sentencia_sql)
                w_cursor.execute(w_sentencia_sql)
                # Se comita el insert realizado.
                self.w_conexion.commit()

                # Se muestra un mensaje de información de sesión al usuario.
                self.pro_mensaje_un_boton('Información',
                                          'Se ha actualizado la contraseña del usuario: {}.'.format(w_usuario),
                                          'Contraseña actualizada',
                                          None)

        else:
            self.pro_mensaje_un_boton('Información',
                                      'La nueva contraseña introducida es la misma que la contraseña anterior por lo '
                                      'que debe de indicar una distinta.',
                                      'Contraseñas iguales',
                                      None)
            self.uiVentana.txtContrasena.setText('')
            self.uiVentana.txtNuevaContrasena.setText('')
            self.uiVentana.txtContrasena.setFocus(True)

    # Se crea el método para conectar a la BBDD.
    def pro_conexion_bbdd(self):

        # Se crea un bloque de excepciones para controlar los fallos.
        try:

            # Se realiza la conexión a la BBDD del curso.
            self.w_conexion = conexion_bbdd('curso_pyqt')

        # Si se ha producido un error en la conexión a la BBDD, se muestra un mensaje de error.
        except Error as w_error:

            self.pro_mensaje_un_boton('Error', 'Error Conexión: {}'.format(w_error), 'Error de conexión', None)

    # Se crea el método para cancelar la sesión.
    def pro_cancelar_sesion(self):

        # Se muestra un mensaje de advertencia al usuario para que confirme si quiere cancelar el login.
        w_boton_pulsado = self.fun_mensaje_dos_botones('Advertencia',
                                                       '¿Esta seguro/a de querer cancelar la modificación de la '
                                                       'contraseña?.',
                                                       'Cancelar Modificación de contraseña',
                                                       None)

        # Si ha pulsado el botón "Aceptar", se cierra la ventana y si es "Cancelar", no hace nada.
        if w_boton_pulsado == 'Aceptar':

            self.hide()

        elif w_boton_pulsado == 'Cancelar':

            pass

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
                                      '4px 8px;border-radius: 3px;min-width: 14px;min-height: 14px;}QPushButton:hover, '
                                      'QPushButton:focus{color: white;background-color: qlineargradient(spread:pad, '
                                      'x1:1, y1:0.545, x2:1, y2:0, stop:0 #2eae35, stop:1 #cae44a);}QPushButton:pressed'
                                      ' {background-color: #2eae35;}')
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
                                      '4px 8px;border-radius: 3px;min-width: 14px;min-height: 14px;}QPushButton:hover, '
                                      'QPushButton:focus{color: white;background-color: qlineargradient(spread:pad, '
                                      'x1:1, y1:0.545, x2:1, y2:0, stop:0 #2eae35, stop:1 #cae44a);}QPushButton:pressed'
                                      ' {background-color: #2eae35;}')
        w_boton_cancelar = w_ventana_mensaje.addButton(self.tr("Cancelar"), QMessageBox.RejectRole)
        w_boton_cancelar.setStyleSheet('QPushButton {color: #ffffff; text-align: center; background-color: '
                                       'qlineargradient(spread:pad, x1:1, y1:0.545, x2:1, y2:0, stop:0 #b6b6b6, stop:1 '
                                       '#e6e6e6); border: 1px solid #828282; padding: 5px 12px 5px 12px; margin: 4px '
                                       '8px 4px 8px; border-radius: 3px; min-width: 14px; min-height: 14px;}'
                                       'QPushButton:hover, QPushButton:focus{color: white;background-color: '
                                       'qlineargradient(spread:pad, x1:1, y1:0.545, x2:1, y2:0, stop:0 #95050d, stop:1'
                                       ' #ea0a20);} QPushButton:pressed {background-color: #95050d;}')

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
    # Creamos una instancia de la clase "ModificarContrasena_App()".
    ventana = ModificarContrasena_App()
    # Se muestra la pantalla.
    ventana.show()
    # Se indica el método para que cierre la aplicación al pulsar el botón de cerrar.
    sys.exit(app.exec_())
