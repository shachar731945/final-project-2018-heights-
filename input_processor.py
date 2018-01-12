mouse_event_type_dictionary = {
    "c": "click", "m": "move", "w": "wheel"
}

keyboard_event_type_dictionary = {
    "p": "press", "r": "release"
}

event_type_dictionary = {
    "m": ("mouse", mouse_event_type_dictionary),
    "k": ("keyboard", keyboard_event_type_dictionary)
}


class InputProcessor:

    def __init__(self, server_network_manager, multiprocess_connection):
        self._server_network_manager = server_network_manager
        self._multiprocess_connection = multiprocess_connection

    def initialize(self):
        while 1:
            data = self._multiprocess_connection.recv()
            if data:
                io_device, io_use_dictionary = \
                    InputProcessor.identify_io_device(data)
                event_type = InputProcessor.identify_event_type(
                    data, io_use_dictionary)


    @staticmethod
    def identify_io_device(data):
        return event_type_dictionary[data.split('|')[0]]

    @staticmethod
    def identify_event_type(data, io_use_dictionary):
        return io_use_dictionary[data.split('|')[1]]



