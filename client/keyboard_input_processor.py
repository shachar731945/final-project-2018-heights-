from client.io_device_processor import DeviceInputProcessor
from client.mimik_keyboard import press_key, release_key


class KeyboardInputProcessor(DeviceInputProcessor):

    def __init__(self):
        DeviceInputProcessor.__init__(self)
        self._keyboard_event_type_dictionary = {
            "p": self.press, "r": self.release
        }

    def process_input(self, io_input):
        event_function = self._keyboard_event_type_dictionary[
            io_input.split('|')[0]]
        event_function(io_input[io_input.index('|')+1:])

    @staticmethod
    def press(io_input_key):
        key_id = int(io_input_key)
        press_key(key_id)

    @staticmethod
    def release(io_input_key):
        key_id = int(io_input_key[1:])
        release_key(key_id)







