import socket
from config import CONFIG
from threading import Thread
from .consoleui import ConsoleUI


class Client:
    def __init__(self):
        self.socket = socket.socket()
        self.console_ui = ConsoleUI()

    def connect(self):
        self.socket.connect((CONFIG['serverIP'], CONFIG['port']))
        Thread(target=self.receive).start()

    def listen(self):
        txt = ''

        while txt != 'exit':
            txt = self.console_ui.user_input()
            self.socket.send(bytes(txt, "utf8"))

    def receive(self):
        while True:
            try:
                msg = self.socket.recv(CONFIG['bufferSize']).decode("utf8")
                self.console_ui.display(msg)
            except OSError:
                break

    def send(self, msg):
        if msg != '':
            self.socket.send(bytes(msg, "utf8"))

    def close(self):
        self.socket.close()
