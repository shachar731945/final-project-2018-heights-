from io_device_processor import DeviceInputProcessor


class MouseInputProcessor(DeviceInputProcessor):

    def __init__(self, network_manager, current_pc, this_pc, pc_list):
        DeviceInputProcessor.__init__(self, network_manager,
                                      current_pc, this_pc)
        self._pc_list = pc_list
        self._mouse_event_type_dictionary = {
            "c": self.click, "m": self.move, "w": self.wheel
        }

    def process_input(self, io_input):
        event_function = self._mouse_event_type_dictionary[
            io_input.split('|')[0]]
        event_function(io_input[io_input.index('|') + 1:])
        pass

    def click(self, io_input_click):
        pass

    def move(self, io_input_position):
        pass

    def wheel(self, io_input_wheel_state):
        pass
