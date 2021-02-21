# Se importan las librerias necesarias.
import sys
import socket
from PyQt5.QtWidgets import QDialog, QApplication
from threading import Thread
from Chat import frmChat

# Se crea una variable global para que se pueda utilizar en el código del programa.
conexion = None


# Se crea la clase Aplicación.
class ChatServidor_Aplicacion(QDialog):

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
        self.ventana.lblTitulo.setText('Servidor')

        self.txteChat = self.ventana.txteChat

    # Se declara el método que realiza la acción de enviar el mensaje al chat.
    def enviar_mensaje(self):
        # Se llama a la variable global "w_conexion".
        global conexion

        # Se guarda el mensaje escrito en la caja de texto a enviar.
        mensaje = self.ventana.txtTexto.text()

        conexion.send(mensaje.encode('utf-8'))

        # Se añade el nuevo texto de la caja de texto en el text edit para que se vea la conversación.
        self.ventana.txteChat.append('Servidor: {}'.format(mensaje))
        # Se limpia la caja de texto.
        self.ventana.txtTexto.setText('')


class ServidorThread(Thread):

    # Se crea el método del constructor inicializador indicando un atributo llamado "ventana".
    def __init__(self, ventana):

        # Se invoca el constructor padre.
        super().__init__()
        # Se añade el atributo "ventana" para poder usarlo.
        self.ventana = ventana

    def run(self):
        # Se indica la IP donde se va a ejecutar el servidor.
        IP = '0.0.0.0'
        # Se indica el puerto donde se va a ejecutar el servidor.
        PUERTO = 20064

        socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # Se asocia la IP y el puerto al socket.
        socket_servidor.bind((IP, PUERTO))

        threads = []
        socket_servidor.listen(4)

        while True:
            global conexion

            (conexion, (ip, puerto)) = socket_servidor.accept()
            t = ClienteThread(ip, puerto, self.ventana)
            t.start()
            threads.append(t)

        for t in threads:
            t.join()


class ClienteThread(Thread):

    def __init__(self, ip, puerto, ventana):
        super().__init__()
        self.ip = ip
        self.puerto = puerto
        self.ventana = ventana

    def run(self):
        while True:
            global conexion
            datos = conexion.recv(1024)
            self.ventana.txteChat.append('Cliente: {}'.format(datos.decode('utf-8')))


# Hacemos referencia al módulo principal de la aplicación.
if __name__ == '__main__':

    # Creamos una aplicación de nuestra ventana.
    app = QApplication(sys.argv)
    # Creamos una instancia de la clase "ChatServidor_Aplicacion()".
    ventana = ChatServidor_Aplicacion()

    st = ServidorThread(ventana)
    st.start()

    # Se muestra la pantalla.
    ventana.exec()
    # Se indica el método para que cierre la aplicación al pulsar el botón de cerrar.
    sys.exit(app.exec_())
