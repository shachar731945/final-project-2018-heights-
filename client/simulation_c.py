from input_processor import InputProcessor
from client_network_manager import ClientNetworkManager


def main():
    client = ClientNetworkManager("192.168.0.20", 8845)
    input_processor = InputProcessor(client)
    input_processor.initialize()
    from time import sleep
    sleep(10)
    input_processor.stop()
    client.close_connection()


if __name__ == "__main__":
    from time import sleep
    sleep(1.5)
    main()


