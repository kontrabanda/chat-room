import socket
import json
from config import CONFIG


class Connection:
    def __init__(self):
        self.socket = socket.socket()

    def connect(self):
        self.socket.connect((CONFIG['serverIP'], CONFIG['port']))

    def send(self, msg_txt):
        msg_dict = {
            'content': msg_txt
        }
        self.__send_dict(msg_dict)

    def __send_dict(self, msg):
        msg_bytes = bytes(json.dumps(msg), "utf8")
        self.socket.send(msg_bytes)

    def receive(self):
        msg_txt = self.__receive_txt()
        return json.loads(msg_txt)

    def __receive_txt(self):
        msg_bytes = self.__receive_bytes()
        return msg_bytes.decode(CONFIG['encoding'])

    def __receive_bytes(self):
        msg_bytes = self.socket.recv(CONFIG['bufferSize'])
        if not msg_bytes:
            raise ConnectionError('Connection dropped!')
        return msg_bytes

    def close(self):
        self.socket.close()
