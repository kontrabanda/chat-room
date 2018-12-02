from .client import Client


def main():
    client = Client()

    client.connect()

    client.listen()

    client.close()

if __name__ == "__main__":
    main()
