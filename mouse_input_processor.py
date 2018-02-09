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

    def click(self, io_input_click):
        button = io_input_click.split('|')[0]
        click_state = io_input_click.split('|')[1]
        if not self._this_pc == self._current_pc:
            self._network_manager.send_message(self._current_pc.ip, "m|c|" + button + '|' + click_state)

    def wheel(self, io_input_wheel_state):
        wheel_state = io_input_wheel_state
        if not self._this_pc == self._current_pc:
            self._network_manager.send_message(self._current_pc.ip, "m|w|" + wheel_state)

    def move(self, io_input_position):
        position = io_input_position
        if not self._this_pc == self._current_pc:
            self._network_manager.send_message(self._current_pc.ip, "m|m|" + position)
