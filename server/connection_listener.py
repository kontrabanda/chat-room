from .connection_builder import ConnectionBuilder
from .connections_collection import ConnectionsCollection


class ConnectionListener:
    def __init__(self):
        self.connections = ConnectionsCollection()

    def handle_connection(self, socket):
        client = ConnectionBuilder.create_connection(socket)
        self.__append(client)
        self.__listen_with_error_handling(client)
        self.__remove(client)

    def __append(self, client):
        self.connections.append(client)
        self.connections.broadcast_txt("%s has joined the chat!" % client.nick)

    def __listen_with_error_handling(self, client):
        try:
            self.__listen(client)
        except ConnectionError:
            print('Broken connection!')

    def __listen(self, client):
        while True:
            msg = client.receive()
            if msg['content'] != "exit":
                self.connections.broadcast(msg)
            else:
                break

    def __remove(self, client):
        client.close()
        self.connections.remove(client)
        self.connections.broadcast_txt("%s has left the chat." % client.nick)
