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
            print(self.term.clear_eol)
            print(self.term.move(idx))
            print("%s-> : " % idx + value)
        self.__clear_screen()

    def user_input(self):
        self.__clear_screen()
        return input()

    def __clear_screen(self):
        print(self.term.move(BUFFER_SIZE))
        print("Enter message: ")
        print(self.term.clear_eol)
        print(self.term.move(BUFFER_SIZE + 1))
