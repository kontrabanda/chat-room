from .connection_builder import ConnectionBuilder
from .connection_socket import ConnectionSocket
from .message_factory import MessageFactory


class ConnectionsCollection:
    def __init__(self):
        self.elements = []

    def handle_connection(self, socket_client):
        client = self.__create_client(socket_client)
        self.__append_client(client)
        self.__listen(client)
        self.__remove_client(client)

    def __create_client(self, socket_client):
        connection_socket = ConnectionSocket(socket_client)
        return ConnectionBuilder(connection_socket) \
            .add_nick() \
            .build()

    def __append_client(self, client):
        self.elements.append(client)
        self.__broadcast_from_server("%s has joined the chat!" % client.nick)

    def __listen(self, client):
        while True:
            try:
                msg = client.receive()
            except ConnectionError:
                break

            if msg['content'] and msg['content'] != "exit":
                self.__broadcast(msg)
            else:
                break

    def __remove_client(self, client):
        client.close()
        self.elements.remove(client)
        self.__broadcast_from_server("%s has left the chat." % client.nick)

    def __broadcast_from_server(self, msgTxt):
        msg = MessageFactory.create_server_message(msgTxt)
        self.__broadcast(msg)

    def __broadcast(self, msg):
        for single_client in self.elements:
            single_client.send(msg)
