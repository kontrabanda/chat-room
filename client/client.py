import socket
from config import CONFIG
from threading import Thread


class Client:
    def __init__(self):
        self.socket = socket.socket()

    def connect(self):
        self.socket.connect((CONFIG['serverIP'], CONFIG['port']))
        Thread(target=self.receive).start()

    def listen(self):
        txt = ''

        while txt != 'exit':
            print('test3')
            txt = input('Enter message:')
            self.send(txt)

        self.close()

    def receive(self):
        while True:
            try:
                msg = self.socket.recv(CONFIG['bufferSize']).decode("utf8")
                print(msg)
            except OSError:
                break

    def send(self, msg):
        self.socket.send(bytes(msg, "utf8"))

    def close(self):
        self.socket.close()


