from .client_builder import ClientBuilder
from datetime import datetime


class ClientsCollection:
    def __init__(self):
        self.elements = []

    def handle_new_client(self, socket_client):
        client = ClientBuilder(socket_client)\
            .add_nick()\
            .build()
        self.__append_client(client)
        self.__listen(client)
        self.__remove_client(client)

    def __listen(self, client):
        while True:
            msg = client.receive()
            if msg['content'] != "exit":
                self.__broadcast(msg)
            else:
                break

    def __append_client(self, client):
        self.elements.append(client)
        self.__broadcast({
            'content': "%s has joined the chat!" % client.nick,
            'datetime': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'nick': 'SERVER'
        })

    def __remove_client(self, client):
        client.close()
        print(len(self.elements))
        self.elements.remove(client)
        print(len(self.elements))
        self.__broadcast({
            'content': "%s has left the chat." % client.nick,
            'datetime': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'nick': 'SERVER'
        })

    def __broadcast(self, msg):
        for single_client in self.elements:
            single_client.send(msg)
