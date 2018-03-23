from abc import abstractmethod


class DeviceInputProcessor:

    def __init__(self):
        pass

    @abstractmethod
    def process_input(self, io_input):
        pass
