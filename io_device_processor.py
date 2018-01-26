from abc import abstractmethod


class DeviceInputProcessor:

    def __init__(self, netwrok_manager, current_pc, pc_list):
        self._network_manager = netwrok_manager
        self._current_pc = current_pc
        self._pc_list = pc_list

    @abstractmethod
    def process_input(self, io_input):
        pass
