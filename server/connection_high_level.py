class ConnectionHighLevel:
    def __init__(self, connection_low_level, nick=""):
        self.connection_low_level = connection_low_level
        self.nick = nick

    def send(self, msg):
        self.connection_low_level.send(msg)

    def receive(self):
        return self.connection_low_level.receive()

    def close(self):
        self.connection_low_level.close()
