from config import CONFIG


class ConnectionLowLevel:
    def __init__(self, socket):
        self.socket = socket

    def send(self, message_txt):
        message_bytes = bytes(message_txt, CONFIG['encoding'])
        self.socket.send(message_bytes)

    def receive(self):
        message_bytes = self.socket.recv(CONFIG['bufferSize'])
        if not message_bytes:
            raise ConnectionError('Connection dropped!')
        return message_bytes.decode(CONFIG['encoding'])

    def close(self):
        self.socket.close()
