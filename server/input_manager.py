from time import sleep
from win32api import GetSystemMetrics, SetCursorPos


class InputManager:

    def __init__(self, process_communication_handle, server_network_manager,
                 pc_matrix, server_pc_coordinates):
        self._process_communication_handle = process_communication_handle
        self._server_network_manager = server_network_manager
        self._pc_matrix = pc_matrix
        self._server_pc_coordinates = server_pc_coordinates
        # False if no server pc

    def initialize(self):
        while 1:
            data = self._process_communication_handle.recv()
            if data:
                pc = self._pc_matrix.get_pointer_value()
                self._server_network_manager.send_message(pc.address, data)
            sleep(0.00001)

    def track_changes(self):
        functions_dictionary = {'l': (self._pc_matrix.pointer_left,
                                      self._pc_matrix.check_left),
                                'r': (self._pc_matrix.pointer_right,
                                      self._pc_matrix.check_right),
                                'u': (self._pc_matrix.pointer_up,
                                      self._pc_matrix.check_up),
                                'd': (self._pc_matrix.pointer_down,
                                      self._pc_matrix.check_down)}
        while 1:
            return_data, address = self._server_network_manager.recv_message()
            # check if the controlled pc returns message
            if return_data and address == \
                    self._pc_matrix.get_pointer_value().address:
                for char in return_data:
                    try:
                        change_matrix_functions = functions_dictionary[char]
                        try:
                            address = change_matrix_functions[1]().address
                            change_matrix_functions[0]()
                        except:  # exception handling
                            pass
                    except KeyError:
                        pass  # exception handling
                if self._pc_matrix.get_pointer() == \
                        self._server_pc_coordinates:
                    pass
            sleep(0.00001)

    @staticmethod
    def position_mouse_on_middle():
        position = GetSystemMetrics()
        SetCursorPos(position[0] / 2, position[1] / 2)







