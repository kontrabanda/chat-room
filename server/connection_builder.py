from .connection import Connection
from .message_factory import MessageFactory


class ConnectionBuilder:
    def __init__(self, connection_socket):
        self.__connection = Connection(connection_socket)

    def add_nick(self):
        self.__send_server_message("You're connect to chat server.")
        self.__send_server_message("Please type your nick.")
        self.__connection.nick = self.__receive_client_nick()
        self.__send_server_message('Welcome %s!' % self.__connection.nick)
        return self

    def __send_server_message(self, msgTxt):
        msg = MessageFactory.create_server_message(msgTxt)
        self.__connection.send(msg)

    def __receive_client_nick(self):
        msg = self.__connection.receive()
        return msg['content']

    def build(self):
        return self.__connection
