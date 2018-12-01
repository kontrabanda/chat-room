from .client import Client


def main():
    print('Start client')
    client = Client()
    print('test1')
    client.connect()

    print('test2')
    client.listen()

    client.close()

if __name__ == "__main__":
    main()
