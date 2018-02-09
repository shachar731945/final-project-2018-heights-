from mouse_input_processor import MouseInputProcessor
from keyboard_input_processor import KeyboardInputProcessor

event_type_dictionary = {
    "m": MouseInputProcessor,
    "k": KeyboardInputProcessor
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
        while 1:
            data = self._client_network_manager.recv_message()
            if data:
                io_device_processor = InputProcessor.identify_io_device(data)
                for processor in self._io_devices_processors:
                    if type(processor) == type(io_device_processor):
                        processor.process_input(
                            data[data.index('|')+1:])

    @staticmethod
    def identify_io_device(data):
        return event_type_dictionary[data.split('|')[0]]



