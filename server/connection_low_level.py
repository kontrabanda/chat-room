from config import CONFIG
import json


class ConnectionLowLevel:
    def __init__(self, socket):
        self.socket = socket

    def send(self, msg):
        msgTxt = json.dumps(msg)
        msgBytes = bytes(msgTxt, CONFIG['encoding'])
        self.socket.send(msgBytes)

    def receive(self):
        msgBytes = self.socket.recv(CONFIG['bufferSize'])
        if not msgBytes:
            raise ConnectionError('Connection dropped!')
        msgTxt = msgBytes.decode(CONFIG['encoding'])
        return json.loads(msgTxt)

    def close(self):
        self.socket.close()
