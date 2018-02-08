from abc import abstractmethod


class DeviceInputProcessor:

    def __init__(self, netwrok_manager, current_pc, this_pc):
        self._network_manager = netwrok_manager
        self._current_pc = current_pc
        self._this_pc = this_pc

    @abstractmethod
    def process_input(self, io_input):
        pass
