from mouse_input_processor import MouseInputProcessor
from keyboard_input_processor import KeyboardInputProcessor

event_type_dictionary = {
    "m": MouseInputProcessor,
    "k": KeyboardInputProcessor
}


class InputProcessor:

    def __init__(self, server_network_manager, multiprocess_connection):
        self._server_network_manager = server_network_manager
        self._multiprocess_connection = multiprocess_connection
        self._io_devices_processors = []
        self._io_devices_processors.append(MouseInputProcessor)
        self._io_devices_processors.append(KeyboardInputProcessor)

    def initialize(self):
        while 1:
            data = self._multiprocess_connection.recv()
            if data:
                io_device_processor = InputProcessor.identify_io_device(data)
                for processor in self._io_devices_processors:
                    if type(processor) == io_device_processor:
                        processor.process_input(data[data.index('|')+1:])

    @staticmethod
    def identify_io_device(data):
        return event_type_dictionary[data.split('|')[0]]



