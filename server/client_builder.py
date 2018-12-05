from .client_socket import ClientSocket
from .client import Client


class ClientBuilder:
    def __init__(self, socket):
        self.nick = ''
        self.client_socket = ClientSocket(socket)

    def add_nick(self):
        self.client_socket.send("You're connect to chat server.")
        self.client_socket.send("Please type your nick.")
        self.nick = self.client_socket.receive()
        self.client_socket.send('Welcome %s!' % self.nick)
        return self

    def build(self):
        return Client(self.client_socket, self.nick)
