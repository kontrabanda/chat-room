from .connections_collection import ConnectionsCollection
from .connection_low_level import ConnectionLowLevel
from .connection_builder import ConnectionBuilder


class ConnectionListener:
    def __init__(self):
        self.connections = ConnectionsCollection()

    def listen(self, socket):
        client = self.__create_client(socket)
        self.__append(client)
        self.__listen(client)
        self.__remove(client)

    def __create_client(self, socket):
        connection_low_level = ConnectionLowLevel(socket)
        return ConnectionBuilder(connection_low_level) \
            .add_nick() \
            .build()

    def __append(self, client):
        self.connections.append(client)
        self.connections.broadcast_txt("%s has joined the chat!" % client.nick)

    def __listen(self, client):
        while True:
            try:
                msg = client.receive()
            except ConnectionError:
                break

            if msg['content'] and msg['content'] != "exit":
                self.connections.broadcast(msg)
            else:
                break

    def __remove(self, client):
        client.close()
        self.connections.remove(client)
        self.connections.broadcast_txt("%s has left the chat." % client.nick)
