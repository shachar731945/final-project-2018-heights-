from io_device_processor import DeviceInputProcessor
from mimik_keyboard import press_key, release_key


class KeyboardInputProcessor(DeviceInputProcessor):

    def __init__(self, network_manager):
        DeviceInputProcessor.__init__(self, network_manager)
        self._keyboard_event_type_dictionary = {
            "p": self.press, "r": self.release
        }

    def process_input(self, io_input):
        event_function = self._keyboard_event_type_dictionary[
            io_input.split('|')[0]]
        event_function(io_input[io_input.index('|')+1:])

    @staticmethod
    def press(io_input_key):
        key_id = io_input_key[1:]
        press_key(key_id)
        print "press another pc",
        print "press this pc",
        print key_id

    @staticmethod
    def release(io_input_key):
        key_id = io_input_key[1:]
        release_key(key_id)
        print "release another pc",
        print "release this pc",
        print key_id








