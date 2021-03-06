# Se importan las librerias necesarias.
import sys
import re

from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from Conexion_PHPMyAdmin import conexion_bbdd
from passlib.hash import pbkdf2_sha256
from pymysql import Error
from EliminarUsuario import frmEliminarUsuario


# Se crea la clase Aplicación.
class EliminarUsuario_Aplicacion(QDialog):

    # Se crea el método del constructor inicializador.
    def __init__(self):

        # Se invoca el constructor padre.
        super().__init__()
        # Se crea una instancia de nuestra ventana diseñada.
        self.uiVentana = frmEliminarUsuario()
        # Se llama al método "setupUi" que esta en la clase "frmEliminarUsuario" del archivo "EliminarUsuario.py".
        self.uiVentana.setupUi(self)
        # Se indica un icono para la ventana principal.
        self.setWindowIcon(QIcon('icono.ico'))
        # Se indica el tamaño de la ventana para que no se pueda modificar su tamaño.
        self.setFixedSize(311, 173)
        # Se indica que solo muestre el aspa para cerrar la ventana en la barra de título.
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        # Se muestra la pantalla.
        self.show()

        # Se indica un texto predefinido para ayudar al usuario a saber que el usuario corresponde con el email.
        self.uiVentana.txtUsuario.setPlaceholderText('example@gmail.com')
        # Se indica un texto predefinido para ayudar al usuario a saber que la contraseña son 10 caracteres
        # alfanuméricos
        self.uiVentana.txtContrasena.setPlaceholderText('10 caracteres alfanuméricos')
        # Se indica que el límite de tamaño a introducir es de 20 caracteres.
        self.uiVentana.txtContrasena.setMaxLength(20)

        # Se deshabilita el botón de "Iniciar sesión" y "Modificar Contraseña" y se crean dos variables donde se
        # indican si se ha validado el usuario y contraseña.
        self.uiVentana.btnAceptar.setEnabled(False)
        self.w_validacion_usuario = False
        self.w_validacion_contrasena = False

        # Se crea la variable de conexión y de cursor para que se pueda utilizar en el programa.
        self.w_conexion = None

        # Declaración de los controladores de eventos (Event Handler).
        self.uiVentana.btnAceptar.clicked.connect(self.pro_eliminar_usuario)
        self.uiVentana.btnCancelar.clicked.connect(self.pro_cancelar)
        self.uiVentana.txtUsuario.textChanged.connect(self.pro_validar_usuario)
        self.uiVentana.txtContrasena.textChanged.connect(self.pro_validar_contrasena)

    # Se crea el método que se lanza al pulsar el botón de "Eliminar usuario".
    def pro_eliminar_usuario(self):

        # Se pregunta si de verdad quiere borrar los datos del usuario.
        w_boton_pulsado = self.fun_mensaje_dos_botones('Consulta', '¿Desea eliminar el usuario {} del sistema?.'
                                                       .format(self.uiVentana.txtUsuario.text().strip()),
                                                       'Confirmar borrado de usuario',
                                                       None)

        # Si ha pulsado el botón de Aceptar, se realiza el borrado del usuario de la BBDD.
        if w_boton_pulsado == 'Aceptar':

            # Se realiza la conexion a la BBDD.
            self.pro_conexion_bbdd()

            # Si la conexión ha sido correcta y w_conexion no esta vacía.
            if self.w_conexion is not None:

                # Se guarda el usuario y la contraseña introducida.
                w_usuario = self.uiVentana.txtUsuario.text().strip()
                w_contrasena = self.uiVentana.txtContrasena.text().strip()

                # Se consulta en la tabla usuarios los datos del usuario y contraseña para saber si son los correctos.
                w_cursor_consulta = self.w_conexion.cursor()
                w_sentencia_sql = '''(SELECT * FROM curso_pyqt.usuarios WHERE email = '{}')'''.format(w_usuario)
                w_cursor_consulta.execute(w_sentencia_sql)
                w_registros = w_cursor_consulta.fetchone()

                # Si la consulta ha recuperado datos y no está vacía.
                if w_registros is not None:

                    # Si la contraseña corresponde con la del usuario en BBDD encriptada.
                    if pbkdf2_sha256.verify(w_contrasena, w_registros[4]):

                        # Se borra el usuario indicado de la BBDD.
                        w_cursor_borrar = self.w_conexion.cursor()
                        w_sentencia_sql = '''DELETE FROM curso_pyqt.usuarios WHERE codigo = {}'''.format(w_registros[0])
                        w_cursor_borrar.execute(w_sentencia_sql)
                        self.w_conexion.commit()

                        # Si el nº de registros borrados es de uno.
                        if w_cursor_borrar.rowcount == 1:

                            # Se muestra un mensaje de información al usuario.
                            self.pro_mensaje_un_boton('Información', 'Se ha eliminado el usuario {} {} {} del sistema.'.
                                                      format(w_registros[1], w_registros[2], w_registros[3]),
                                                      'Borrado de usuario', None)

                            # Se limpia el formulario y se coloca el foco.
                            self.uiVentana.txtUsuario.setText('')
                            self.uiVentana.txtContrasena.setText('')
                            self.uiVentana.txtUsuario.setFocus(True)

                        # Si no se ha borrado ningún registro, se informa al usuario por pantalla.
                        else:

                            self.pro_mensaje_un_boton('Error',
                                                      'No se ha podido eliminar el usuario {} del sistema.'
                                                      .format(w_usuario),
                                                      'Error de borrado de usuario',
                                                      None)

                    # Si la contraseña introducida no es la misma que la que hay en la BBDD, se informa al usuario.
                    else:

                        self.pro_mensaje_un_boton('Error',
                                                  'La contraseña introducida es incorrecta.',
                                                  'Contraseña incorrecta',
                                                  None)

                # Si el usuario no existe, se muestra un mensaje al usuario.
                else:

                    self.pro_mensaje_un_boton('Error', 'El usuario {} o la contraseña no son correctos.'
                                              .format(w_usuario), 'Error de borrado de usuario', None)

            # Si no se ha podido realizar la conexión con la BBDD, se informa con un mensaje al usuario.
            else:

                self.pro_mensaje_un_boton('Error', 'Se ha producido un error en la conexión con la BBDD.',
                                          'Error de conexión', None)

        # Si el botón pulsado ha sido el de Cancelar, se oculta la ventana de mensaje.
        elif w_boton_pulsado == 'Cancelar':
            pass

    # Se crea el método que se lanza cuando se pulsa el botón "Cancelar" de la pantalla.
    def pro_cancelar(self):

        # Se muestra un mensaje de advertencia al usuario para que confirme si quiere cancelar el borrado del usuario.
        w_boton_pulsado = self.fun_mensaje_dos_botones('Advertencia',
                                                       '¿Esta seguro/a de querer cancelar el borrado de usuario?.',
                                                       'Cancelar Eliminar usuario',
                                                       None)
        # Si ha pulsado el botón "Aceptar", se cierra la aplicación y si es "Cancelar", no hace nada.
        if w_boton_pulsado == 'Aceptar':
            sys.exit()
        elif w_boton_pulsado == 'Cancelar':
            pass

    # Se declara el método que se lanza cuando se modifica el texto de la caja del usuario.
    def pro_validar_usuario(self):

        # Se guarda el texto que introduce el usuario en una variable.
        w_email = self.uiVentana.txtUsuario.text().strip()

        # Se aplica el patrón de validación para los campos de Email.
        w_patron = '^[a-zA-Z0-9\._-]+@[a-zA-Z0-9-]{2,}[.][a-zA-Z]{2,4}$'
        # Se indica que el campo a comprobar es el email y se guarda en una variable.
        w_validar_email = re.match(w_patron, w_email, re.I)

        # Si el texto del email está vacío.
        if w_email == '':

            # Se muestra la imagen de error auxiliar.
            self.uiVentana.btnValidaUsuario.setStyleSheet('image: url();')
            # Se indica que el usuario no esta validado.
            self.w_validacion_usuario = False

            # Se comprueba la validación de los campos para activar o no el botón "Iniciar Sesión".
            self.pro_comprobar_estado_boton_aceptar()

        # Si el texto del email no ha sido validado por el patrón de emails.
        elif not w_validar_email:

            # Se muestra la imagen de error auxiliar.
            self.uiVentana.btnValidaUsuario.setStyleSheet('image: url(:/iconos/iconos/dato_erroneo.ico);')
            # Se indica que el usuario no esta validado.
            self.w_validacion_usuario = False

            # Se comprueba la validación de los campos para activar o no el botón "Iniciar Sesión".
            self.pro_comprobar_estado_boton_aceptar()

        # Si el usuario ha sido rellenado y validado.
        else:

            # Se muestra la imagen de campo validado auxiliar.
            self.uiVentana.btnValidaUsuario.setStyleSheet('image: url(:/iconos/iconos/dato_correcto.ico);')
            # Se indica que el usuario esta validado.
            self.w_validacion_usuario = True

            # Se comprueba la validación de los campos para activar o no el botón "Iniciar Sesión".
            self.pro_comprobar_estado_boton_aceptar()

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

            # Se comprueba la validación de los campos para activar o no el botón "Iniciar Sesión".
            self.pro_comprobar_estado_boton_aceptar()

    # Se crea un método que comprueba si tanto el usuario como la contraseña estan validados para activar el botón de
    # "Iniciar sesión", mientras tanto, estará desactivado.
    def pro_comprobar_estado_boton_aceptar(self):

        # Si la validación de los dos campos se ha realizado de forma correcta, se activa el botón "Iniciar sesión" y el
        # de modificar contraseña.
        if self.w_validacion_usuario and self.w_validacion_contrasena:

            self.uiVentana.btnAceptar.setEnabled(True)

        else:

            self.uiVentana.btnAceptar.setEnabled(False)

    # Se crea el método para conectar a la BBDD.
    def pro_conexion_bbdd(self):

        # Se crea un bloque de excepciones para controlar los fallos.
        try:

            # Se realiza la conexión a la BBDD del curso.
            self.w_conexion = conexion_bbdd('curso_pyqt')

        # Si se ha producido un error en la conexión a la BBDD, se muestra un mensaje de error.
        except Error as w_error:

            self.pro_mensaje_un_boton('Error', 'Error Conexión: {}'.format(w_error), 'Error de conexión', None)

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
    # Creamos una instancia de la clase "EliminarUsuario_Aplicacion()".
    ventana = EliminarUsuario_Aplicacion()
    # Se muestra la pantalla.
    ventana.show()
    # Se indica el método para que cierre la aplicación al pulsar el botón de cerrar.
    sys.exit(app.exec_())
