from .client import Client


class ClientsCollection:
    def __init__(self):
        self.elements = []

    def handle_new_client(self, socket_client):
        client = Client(socket_client=socket_client)
        self.__append_client(client)
        self.__listen(client)
        self.__remove_client(client)

    def __listen(self, client):
        msg = ''
        while msg != "exit":
            msg = client.receive()
            self.__broadcast(msg)

    def __append_client(self, client):
        client.fetch_nick()
        self.elements.append(client)
        self.__broadcast("%s has joined the chat!" % client.nick)

    def __remove_client(self, client):
        client.close()
        self.elements.remove(client)
        self.__broadcast("%s has left the chat." % client.nick)

    def __broadcast(self, msg):
        for single_client in self.elements:
            single_client.send(msg)
