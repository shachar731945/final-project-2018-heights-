from io_device_processor import DeviceInputProcessor


class KeyboardInputProcessor(DeviceInputProcessor):

    def __init__(self, network_manager, current_pc, pc_list):
        DeviceInputProcessor.__init__(self, network_manager,
                                      current_pc, pc_list)
        self._keyboard_event_type_dictionary = {
            "p": self.press, "r": self.release
        }

    def process_input(self, io_input):
        event_function = self._keyboard_event_type_dictionary[
            io_input.split('|')[0]]
        event_function(io_input[io_input.index('|')+1:])

    def press(self, io_input_key):
        key_id = io_input_key[1:]
        self._network_manager.send_message(self._current_pc.ip, "k|p|")
        print self

    def release(self):
        print self








