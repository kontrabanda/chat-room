import json


class ConnectionHighLevel:
    def __init__(self, connection_low_level, nick=""):
        self.connection_low_level = connection_low_level
        self.nick = nick

    def send(self, message):
        message_json_txt = json.dumps(message)
        self.connection_low_level.send(message_json_txt)

    def receive(self):
        message_txt = self.connection_low_level.receive()
        message = json.loads(message_txt)
        message['nick'] = self.nick
        return message

    def close(self):
        self.connection_low_level.close()
