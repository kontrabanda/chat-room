from config import CONFIG


class Client:
    def __init__(self, socket_client):
        self.nick = ''
        self.socket_client = socket_client

    def fetch_nick(self):
        self.send("You're connect to chat server.")
        self.send("Please type your nick.")
        self.nick = self.receive()
        self.send('Welcome %s!' % self.nick)
        return self.nick

    def send(self, msg):
        self.socket_client.send(bytes(msg, "utf8"))

    def receive(self):
        return self.socket_client.recv(CONFIG['bufferSize']).decode("utf8")

    def close(self):
        self.send("exit")
        self.socket_client.close()
