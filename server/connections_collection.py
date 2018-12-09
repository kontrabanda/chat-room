from .message_factory import MessageFactory


class ConnectionsCollection:
    def __init__(self):
        self.elements = []

    def append(self, client):
        self.elements.append(client)

    def remove(self, client):
        self.elements.remove(client)

    def broadcast_txt(self, msgTxt):
        msg = MessageFactory.create_server_message(msgTxt)
        self.broadcast(msg)

    def broadcast(self, msg):
        for single_client in self.elements:
            single_client.send(msg)
