from config import CONFIG


class ConnectionSocket:
    def __init__(self, socket):
        self.socket = socket

    def send(self, msgTxt):
        msgBytes = bytes(msgTxt, CONFIG['encoding'])
        self.socket.send(msgBytes)

    def receive(self):
        msgBytes = self.socket.recv(CONFIG['bufferSize'])
        return msgBytes.decode(CONFIG['encoding'])

    def close(self):
        self.socket.close()
