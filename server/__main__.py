from .server import Server


def main():
    server = Server()
    server.start()

    server.listen()

    server.close()

if __name__ == "__main__":
    main()
