from io_device_processor import DeviceInputProcessor
from mimik_mouse import click_mouse, wheel_mouse, move_mouse
from win32api import GetSystemMetrics
from win32gui import GetCursorPos


class MouseInputProcessor(DeviceInputProcessor):

    def __init__(self):
        DeviceInputProcessor.__init__(self)
        self._mouse_event_type_dictionary = {
            "c": self.click, "m": self.move, "w": self.wheel
        }

    def process_input(self, io_input):
        event_function = self._mouse_event_type_dictionary[
            io_input.split('|')[0]]
        event_function(io_input[io_input.index('|') + 1:])

    @staticmethod
    def click(io_input_click):
        button = io_input_click.split('|')[0]
        click_state = io_input_click.split('|')[1]
        click_mouse(button+click_state)

    @staticmethod
    def wheel(io_input_wheel_state):
        wheel_state = int(io_input_wheel_state)
        wheel_mouse(wheel_state)

    @staticmethod
    def move(io_input_move_position):
        move_position = eval(io_input_move_position)
        # current_position = GetCursorPos()
        # suggested_position = [current_position[0] + move_position[0],
        #                       current_position[1] + move_position[1]]
        # width = GetSystemMetrics(0)
        # height = GetSystemMetrics(1)
        # return_message = ""
        # if suggested_position[0] < 0:
        #     return_message += 'l'
        #     suggested_position[0] = 0
        # elif suggested_position[0] > width:
        #     return_message += 'r'
        #     suggested_position[0] = width
        # if suggested_position[1] < 0:
        #     return_message += 'u'
        #     suggested_position[1] = 0
        # elif suggested_position[1] > height:
        #     return_message += 'd'
        #     suggested_position[1] = height
        move_mouse(move_position)
        # if return_message:
        #     self._client_network_manager.send_message(return_message)





