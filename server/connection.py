class Connection:
    def __init__(self, connection_socket, nick=""):
        self.connection_socket = connection_socket
        self.nick = nick

    def send(self, msg):
        self.connection_socket.send(msg)

    def receive(self):
        return self.connection_socket.receive()

    def close(self):
        self.connection_socket.close()
