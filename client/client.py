import socket
from config import CONFIG
from threading import Thread
from .consoleui import ConsoleUI
import json


class Client:
    def __init__(self):
        self.socket_closed = True
        self.socket = socket.socket()
        self.console_ui = ConsoleUI()

    def connect(self):
        self.socket.connect((CONFIG['serverIP'], CONFIG['port']))
        self.socket_closed = False
        Thread(target=self.receive).start()

    def listen(self):
        txt = ''

        while txt != 'exit':
            txt = self.console_ui.user_input()
            if not self.socket_closed:
                msg = {
                    'content': txt
                }

                self.socket.send(bytes(json.dumps(msg), "utf8"))
            else:
                self.console_ui.display("Connection closed!")
                break

    def receive(self):
        while True:
            msgTxt = self.socket.recv(CONFIG['bufferSize']).decode("utf8")

            if msgTxt:
                msg = json.loads(msgTxt)
                self.console_ui.display(msg['content'])
            else:
                self.close()
                self.console_ui.display('Server closed!')
                break

    def send(self, msg):
        if msg != '':
            self.socket.send(bytes(msg, "utf8"))

    def close(self):
        self.socket_closed = True
        self.socket.close()
