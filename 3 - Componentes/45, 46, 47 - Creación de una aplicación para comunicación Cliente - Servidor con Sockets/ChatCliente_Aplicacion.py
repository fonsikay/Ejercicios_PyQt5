# Se importan las librerias necesarias.
import sys
import socket
from PyQt5.QtWidgets import QDialog, QApplication
from threading import Thread
from Chat import frmChat

# Se crea una variable global para que se pueda utilizar en el código del programa.
socket_cliente = None


# Se crea la clase Aplicación.
class ChatCliente_Aplicacion(QDialog):

    # Se crea el método del constructor inicializador.
    def __init__(self):

        # Se invoca el constructor padre.
        super().__init__()
        # Se crea una instancia de nuestra ventana diseñada.
        self.ventana = frmChat()
        # Se llama al método "setupUi" que esta en la clase "frmChat" del archivo "Chat.py".
        self.ventana.setupUi(self)
        # Se muestra la pantalla.
        self.show()

        # Declaración de los controladores de eventos (Event Handler).
        self.ventana.btnEnviar.clicked.connect(self.enviar_mensaje)
        # Se indica el texto inicial que va a tener la label.
        self.ventana.lblTitulo.setText('Cliente')
        self.txteChat = self.ventana.txteChat

    # Se declara el método que realiza la acción de enviar el mensaje al chat.
    def enviar_mensaje(self):

        # Se guarda el mensaje escrito en la caja de texto a enviar.
        mensaje = self.ventana.txtTexto.text()
        # Se añade el nuevo texto de la caja de texto en el text edit para que se vea la conversación.
        self.ventana.txteChat.append('Cliente: {}'.format(self.ventana.txtTexto.text()))
        # Se envía el mensaje al servidor.
        socket_cliente.send(mensaje.encode('utf-8'))
        # Se limpia la caja de texto.
        self.ventana.txtTexto.setText('')


class ClienteThread(Thread):

    # Se crea el método del constructor inicializador indicando un atributo llamado "ventana".
    def __init__(self, ventana):

        # Se invoca el constructor padre.
        Thread.__init__(self)
        # Se añade el atributo "ventana" para poder usarlo.
        self.window = ventana

    def run(self):

        global socket_cliente

        host = socket.gethostname()
        port = 20064

        socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_cliente.connect((host, port))

        while True:

            mensaje = socket_cliente.recv(1024)
            ventana.txteChat.append('Servidor: '.format(mensaje.decode('utf-8')))
            socket_cliente.close()


# Hacemos referencia al módulo principal de la aplicación.
if __name__ == '__main__':

    # Creamos una aplicación de nuestra ventana.
    app = QApplication(sys.argv)
    # Creamos una instancia de la clase "ChatCliente_Aplicacion()".
    ventana = ChatCliente_Aplicacion()

    t = ClienteThread(ventana)
    t.start()

    # Se muestra la pantalla.
    ventana.exec()
    # Se indica el método para que cierre la aplicación al pulsar el botón de cerrar.
    sys.exit(app.exec_())
