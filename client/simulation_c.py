from input_processor import InputProcessor
from client_network_manager import ClientNetworkManager


def main():
    client = ClientNetworkManager("10.200.200.100", 8845)
    input_processor = InputProcessor(client)
    input_processor.initialize()
    from time import sleep
    sleep(10)
    input_processor.stop()
    client.close_connection()


if __name__ == "__main__":
    main()


