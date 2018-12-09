from threading import Thread

from .connection import Connection
from .consoleui import ConsoleUI


class Client:
    def __init__(self):
        self.socket_closed = True
        self.connection = Connection()
        self.console_ui = ConsoleUI()

    def start(self):
        self.__connect()
        self.__listen()
        self.__close()

    def __connect(self):
        self.connection.connect()
        self.socket_closed = False
        Thread(target=self.__receive).start()

    def __listen(self):
        txt = ''

        while txt != 'exit':
            txt = self.console_ui.user_input()
            if not self.socket_closed:
                self.connection.send(txt)
            else:
                self.console_ui.display("Connection closed!")
                break

    def __receive(self):
        while True:
            try:
                msg = self.connection.receive()
                self.console_ui.display_with_color(msg)
            except ConnectionError:
                self.console_ui.display('Server closed!')
                self.__close()
                break

    def __close(self):
        self.socket_closed = True
        self.connection.close()
