from threading import Thread, Lock


def data_send(network_communication_handle, matrix_communication_handle,
              send_communication_handle, matrix):

    class DataSendingThread(Thread):

        def __init__(self, send_handle,
                     network_communication_pipe_handle,
                     matrix_communication_pipe_handle, temp_matrix,
                     thread_lock):
            Thread.__init__(self)
            self._send_handle = send_handle
            self._network_communication_handle = \
                network_communication_pipe_handle
            self._matrix_communication_handle = \
                matrix_communication_pipe_handle
            self._pc_matrix = temp_matrix
            self._lock = thread_lock

        def run(self):
            while 1:
                data_recv = self._network_communication_handle.recv()
                if data_recv:
                    self._lock.acquire()

                    pc = self._pc_matrix.get_pointer_value()
                    # print(str(self._pc_matrix.get_pointer()))
                    #     print("send to " + str(pc.address))
                    self._lock.release()
                    self._send_handle.send((data_recv, pc.address))

        def change_data(self):
            while 1:
                recv_data = self._matrix_communication_handle.recv()
                if recv_data:
                    self._lock.acquire()
                    self._pc_matrix = recv_data
                    # print("updated " + str(self._pc_matrix.get_pointer()))
                    self._lock.release()

    threading_lock = Lock()

    functionality_class = DataSendingThread(
        send_communication_handle, network_communication_handle,
        matrix_communication_handle, matrix, threading_lock)
    functionality_class.start()
    functionality_class.change_data()


def track_changes(matrix_communication_handle,
                  communication_pipe_handle, pc_matrix,
                  static_middle_position, update_hooker_state_pipe,
                  server_pc_coordinates=(1, 0)):
    functions_dictionary = {'l': (pc_matrix.pointer_left,
                                  pc_matrix.check_left),
                            'r': (pc_matrix.pointer_right,
                                  pc_matrix.check_right),
                            'u': (pc_matrix.pointer_up,
                                  pc_matrix.check_up),
                            'd': (pc_matrix.pointer_down,
                                  pc_matrix.check_down)}
    while 1:
        return_data, address = communication_pipe_handle.recv()
        # check if the controlled pc returns message through server
        # communication
        if return_data and address == \
                pc_matrix.get_pointer_value().address:
            for char in return_data:
                change_matrix_functions = functions_dictionary[char]
                try:
                    # print(str(pc_matrix.get_pointer_value().address))
                    address = change_matrix_functions[1]().address
                    # print(str(address) + "address printed1")
                    change_matrix_functions[0]()
                    # print(pc_matrix.get_pointer())
                    # print(str(pc_matrix.get_pointer_value().address))
                    matrix_communication_handle.send(pc_matrix)
                    # if address == self._server_pc_address:
                    #     print("A")
                    print("bla bla ", pc_matrix.get_pointer(),
                          server_pc_coordinates)
                    print(pc_matrix.get_pointer(), " ", server_pc_coordinates)
                    if pc_matrix.get_pointer() != server_pc_coordinates:
                        print("change to other pc00000000 ", address)
                        # SetCursorPos(static_middle_position)
                        update_hooker_state_pipe.send(str(False))
                    else:
                        print("change to server pc")
                        update_hooker_state_pipe.send(str(True))

                except Exception as e:  # exception handling
                    print(str(e))
                    # if pc_matrix.get_pointer() == \
                    #         self._server_pc_coordinates:
                    #     pass



