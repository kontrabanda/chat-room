from .message_factory import MessageFactory


class ConnectionsCollection:
    def __init__(self):
        self.elements = []

    def append(self, client):
        self.elements.append(client)

    def remove(self, client):
        self.elements.remove(client)

    def broadcast_txt(self, message_txt):
        message = MessageFactory.create_server_message(message_txt)
        self.broadcast(message)

    def broadcast(self, message):
        for single_client in self.elements:
            single_client.send(message)
