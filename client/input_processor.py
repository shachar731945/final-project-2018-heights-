from mouse_input_processor import MouseInputProcessor
from keyboard_input_processor import KeyboardInputProcessor
from time import sleep

event_type_dictionary = {
    "m": 0,
    "k": 1
}


class InputProcessor:

    def __init__(self, client_network_manager):
        self._client_network_manager = client_network_manager
        self._io_devices_processors = []
        self._io_devices_processors.append(MouseInputProcessor(
            client_network_manager))
        self._io_devices_processors.append(KeyboardInputProcessor(
            client_network_manager))

    def initialize(self):
        self._client_network_manager.send_message("test")
        while 1:
            data = self._client_network_manager.recv_message()
            if data:
                io_device_processor_index = InputProcessor.identify_io_device(
                    data)
                processor = self._io_devices_processors[
                    io_device_processor_index]
                processor.process_input(
                            data[data.index('|')+1:])
            sleep(0.1)

    @staticmethod
    def identify_io_device(data):
        return event_type_dictionary[data.split('|')[0]]


# for check
from client_network_manager import ClientNetworkManager
a = InputProcessor(ClientNetworkManager("localhost", 8897))
a.initialize()



