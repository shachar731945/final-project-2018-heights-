from io_device_processor import DeviceInputProcessor


class KeyboardInputProcessor(DeviceInputProcessor):

    def __init__(self, network_manager, current_pc, this_pc):
        DeviceInputProcessor.__init__(self, network_manager,
                                      current_pc, this_pc)
        self._keyboard_event_type_dictionary = {
            "p": self.press, "r": self.release
        }

    def process_input(self, io_input):
        event_function = self._keyboard_event_type_dictionary[
            io_input.split('|')[0]]
        event_function(io_input[io_input.index('|')+1:])

    def press(self, io_input_key):
        key_id = io_input_key[1:]
        if not self._this_pc == self._current_pc:
            self._network_manager.send_message(self._current_pc.ip, "k|p|" +
                                               key_id)
            print "press another pc",
        print "press this pc",
        print key_id

    def release(self, io_input_key):
        key_id = io_input_key[1:]
        if not self._this_pc == self._current_pc:
            self._network_manager.send_message(self._current_pc.ip, "k|r|" +
                                               key_id)
            print "release another pc",
        print "release this pc",
        print key_id








