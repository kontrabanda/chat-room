import collections
from blessings import Terminal
from threading import RLock

BUFFER_SIZE = 10


class ConsoleUI:
    def __init__(self):
        self.term = Terminal()
        self.msgs = self.__create_messages()
        self.lock = RLock()

    def __create_messages(self):
        msgs = []
        for i in range(0, BUFFER_SIZE):
            msgs.append("")
        return collections.deque(iterable=msgs, maxlen=BUFFER_SIZE)

    def display(self, msg):
        self.lock.acquire()

        self.msgs.append(msg)
        self.__refresh_screen()

        self.lock.release()

    def __refresh_screen(self):
        for idx, value in enumerate(self.msgs):
            print(self.term.move(idx))
            print("                                                       ")
            print(self.term.move(idx))
            print("%s-> : " % idx + value)
        print(self.term.move(BUFFER_SIZE))
        print('Enter message: ')
        print("                                                       ")
        print(self.term.move(BUFFER_SIZE + 1))

    def user_input(self):
        print(self.term.move(BUFFER_SIZE))
        print('Enter message: ')
        print("                                                       ")
        print(self.term.move(BUFFER_SIZE + 1))
        return input()
