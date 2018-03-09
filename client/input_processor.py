from mouse_input_processor import MouseInputProcessor
from keyboard_input_processor import KeyboardInputProcessor
from time import sleep
from multiprocessing import Process


class InputProcessor:

    def __init__(self, client_network_manager):
        self._event_type_dictionary = {
            "m": 0,
            "k": 1
        }
        self._client_network_manager = client_network_manager
        self._io_devices_processors = []
        self._io_devices_processors.append(MouseInputProcessor(
            client_network_manager))
        self._io_devices_processors.append(KeyboardInputProcessor(
            client_network_manager))
        self._process = Process(target=self.initialize_process, args=())

    def initialize(self):
        if __name__ == "__main__":
            self._process.start()

    def initialize_process(self):
        self._client_network_manager.send_message("test")
        while 1:
            data = self._client_network_manager.recv_message()
            if data:
                io_device_processor_index = self.identify_io_device(
                    data)
                processor = self._io_devices_processors[
                    io_device_processor_index]
                processor.process_input(
                            data[data.index('|')+1:])
            sleep(0.00000001)

    def stop(self):
        self._process.terminate()

    def identify_io_device(self, data):
        return self._event_type_dictionary[data.split('|')[0]]




