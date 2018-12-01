import socket
from config import CONFIG
from threading import Thread


class Server:
    def __init__(self):
        self.socket = socket.socket()
        self.clientsCollection = {}

    def start(self):
        print("Starting server")
        self.socket.bind(('', CONFIG['port']))
        self.socket.listen(CONFIG['listenerCount'])

    def listen(self):
        while True:
            client, addr = self.socket.accept()
            print("Got connection from", addr)
            client.send(bytes("You're connect to chat server", "utf8"))
            Thread(target=self.handle_client, args=(client,)).start()

    def handle_client(self, client):
        client.send(bytes("Please type your nick", "utf8"))
        name = client.recv(CONFIG['bufferSize']).decode("utf8")
        self.clientsCollection[client] = name
        client.send(bytes('Welcome %s!' % name, "utf8"))
        self.broadcast("%s has joined the chat!" % name)

        while True:
            msg = client.recv(CONFIG['bufferSize']).decode("utf8")
            if msg != "exit":
                self.broadcast(msg)
            else:
                client.send(bytes("exit", "utf8"))
                client.close()
                del self.clientsCollection[client]
                self.broadcast("%s has left the chat." % name)
                break

    def broadcast(self, msg):
        for single_client in self.clientsCollection:
            single_client.send(bytes(msg, "utf8"))

    def close(self):
        print("Closing server")
        self.socket.close()
