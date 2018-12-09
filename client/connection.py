import socket
import json
from config import CONFIG


class Connection:
    def __init__(self):
        self.socket = socket.socket()

    def connect(self):
        self.socket.connect((CONFIG['serverIP'], CONFIG['port']))

    def send(self, msgTxt):
        msg = {
            'content': msgTxt
        }
        self.socket.send(bytes(json.dumps(msg), "utf8"))

    def receive(self):
        msgBytes = self.socket.recv(CONFIG['bufferSize'])
        if not msgBytes:
            raise ConnectionError('Connection dropped!')
        msgTxt = msgBytes.decode(CONFIG['encoding'])
        print(msgTxt)
        return json.loads(msgTxt)

    def close(self):
        self.socket.close()
