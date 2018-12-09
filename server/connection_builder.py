from .connection_high_level import ConnectionHighLevel
from .message_factory import MessageFactory
from .connection_low_level import ConnectionLowLevel


class ConnectionBuilder:
    @staticmethod
    def create_connection(socket):
        connection_low_level = ConnectionLowLevel(socket)
        return ConnectionBuilder(connection_low_level) \
            .add_nick() \
            .build()

    def __init__(self, connection_low_level):
        self.__connection = ConnectionHighLevel(connection_low_level)

    def add_nick(self):
        self.__send_server_message("You're connect to chat server. Please type your nick.")
        self.__connection.nick = self.__receive_client_nick()
        self.__send_server_message('Welcome %s!' % self.__connection.nick)
        return self

    def __send_server_message(self, message_txt):
        message = MessageFactory.create_server_message(message_txt)
        self.__connection.send(message)

    def __receive_client_nick(self):
        message = self.__connection.receive()
        return message['content']

    def build(self):
        return self.__connection
