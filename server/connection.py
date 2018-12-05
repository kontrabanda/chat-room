from .message_factory import MessageFactory


class Connection:
    def __init__(self, connection_socket, nick=""):
        self.connection_socket = connection_socket
        self.nick = nick

    def send(self, msg):
        msgTxt = "(" + msg['datetime'] + ") " + msg['nick'] + ": " + msg['content']
        self.connection_socket.send(msgTxt)

    def receive(self):
        txt = self.connection_socket.receive()
        return MessageFactory.create_message(nick=self.nick, msg=txt)

    def close(self):
        self.connection_socket.close()
