from input_processor import InputProcessor
from client_network_manager import ClientNetworkManager

client = ClientNetworkManager("192.168.0.20", 8821)
input_processor = InputProcessor(client)
input_processor.initialize()
a = raw_input("5")
while a != "*":
    a = raw_input("5")
input_processor.stop()


