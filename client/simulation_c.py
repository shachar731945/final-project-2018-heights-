from input_processor import InputProcessor
from client_network_manager import ClientNetworkManager


def main():
    client = ClientNetworkManager("192.168.0.20", 8821)
    input_processor = InputProcessor(client)
    input_processor.initialize()
    from time import sleep
    sleep(10)
    input_processor.stop()


if __name__ == "__main__":
    main()


