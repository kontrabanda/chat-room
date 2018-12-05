from datetime import datetime


class MessageFactory:
    @staticmethod
    def create_server_message(msg):
        return MessageFactory.create_message('SERVER', msg)

    @staticmethod
    def create_message(nick, msg):
        return {
            'content': msg,
            'datetime': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'nick': nick
        }
