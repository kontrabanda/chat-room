import socket
from config import CONFIG
from threading import Thread
from .connection_listener import ConnectionListener


class Server:
    def __init__(self):
        self.socket = socket.socket()
        self.connection_listener = ConnectionListener()

    def start(self):
        print("Starting server")
        self.socket.bind(('', CONFIG['port']))
        self.socket.listen(CONFIG['listenerCount'])

    def listen(self):
        while True:
            socket_client, addr = self.socket.accept()
            print("Got connection from", addr)
            Thread(target=self.connection_listener.handle_connection, args=(socket_client,)).start()

    def close(self):
        print("Closing server")
        self.socket.close()
