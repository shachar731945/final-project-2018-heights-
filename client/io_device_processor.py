from abc import abstractmethod


class DeviceInputProcessor:

    def __init__(self, network_manager):
        self._client_network_manager = network_manager

    @abstractmethod
    def process_input(self, io_input):
        pass
