from datetime import datetime


class Client:
    def __init__(self, client_socket, nick):
        self.client_socket = client_socket
        self.nick = nick

    def send(self, msg):
        msgTxt = "(" + msg['datetime'] + ") " + msg['nick'] + ": " + msg['content']
        self.client_socket.send(msgTxt)

    def receive(self):
        txt = self.client_socket.receive()
        return {
            'content': txt,
            'datetime': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'nick': self.nick
        }

    def close(self):
        self.client_socket.close()
