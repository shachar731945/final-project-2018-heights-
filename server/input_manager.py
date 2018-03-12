from time import sleep
from win32api import GetSystemMetrics, SetCursorPos


class InputManager:

    def __init__(self, pc_matrix, comm, server_pc_address=(0, 0)):
        self._pc_matrix = pc_matrix
        self._communication_pipe_handle = comm
        self._server_pc_address = server_pc_address
        # self._server_pc_coordinates = server_pc_coordinates
        # False if no server pc, use in future for mouse hide if self control

    def data_send(self, q, communication_handle):
        server = q.get()
        while 1:
            data = communication_handle.recv()
            pc = self._pc_matrix.get_pointer_value()
            server.send_message(data, pc.address)

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
            return_data, address = self._communication_pipe_handle.recv()
            # check if the controlled pc returns message
            if return_data and address == \
                    self._pc_matrix.get_pointer_value().address:
                for char in return_data:
                    try:
                        change_matrix_functions = functions_dictionary[char]
                        try:
                            address = change_matrix_functions[1]().address
                            change_matrix_functions[0]()
                            if address == self._server_pc_address:
                                print("A")
                        except:  # exception handling
                            pass
                    except KeyError:
                        pass  # exception handling
                # if self._pc_matrix.get_pointer() == \
                #         self._server_pc_coordinates:
                #     pass
            sleep(0.00001)

    @staticmethod
    def position_mouse_on_middle():
        position = GetSystemMetrics()
        SetCursorPos(position[0] / 2, position[1] / 2)







