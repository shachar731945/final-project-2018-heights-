from threading import Thread, Lock


def data_send(ioinput_communication_handle, matrix_communication_handle,
              send_communication_handle, matrix):

    class DataSendingThread(Thread):

        def __init__(self, send_handle,
                     ioinput_communication_pipe_handle,
                     matrix_communication_pipe_handle, temp_matrix,
                     thread_lock):
            Thread.__init__(self)
            self._send_handle = send_handle
            self._ioinput_communication_handle = \
                ioinput_communication_pipe_handle
            self._matrix_communication_handle = \
                matrix_communication_pipe_handle
            self._pc_matrix = temp_matrix
            self._lock = thread_lock

        def run(self):
            while 1:
                data_recv = self._ioinput_communication_handle.recv()
                if data_recv:
                    self._lock.acquire()

                    pc = self._pc_matrix.get_pointer_value()
                    # print(str(self._pc_matrix.get_pointer()))
                    #     print("send to " + str(pc.address))
                    self._lock.release()
                    self._send_handle.send(("1|" + data_recv, pc.address))

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
        send_communication_handle, ioinput_communication_handle,
        matrix_communication_handle, matrix, threading_lock)
    functionality_class.start()
    functionality_class.change_data()


def track_changes(matrix_communication_handle,
                  recv_communication_pipe_handle, pc_matrix,
                  update_hooker_state_pipe, send_communication_handle):
    functions_dictionary = {'l': (pc_matrix.pointer_left,
                                  pc_matrix.check_left),
                            'r': (pc_matrix.pointer_right,
                                  pc_matrix.check_right),
                            'u': (pc_matrix.pointer_up,
                                  pc_matrix.check_up),
                            'd': (pc_matrix.pointer_down,
                                  pc_matrix.check_down)}
    while 1:
        data, address = recv_communication_pipe_handle.recv()
        # check if the controlled pc returns message through server
        # communication
        if data and address == \
                pc_matrix.get_pointer_value().address:
            args = data.split('|')
            direction_change, position, resolution = args[0], args[1], args[2]
            print(
                "adres ", pc_matrix.get_pointer_value().address,
                " recieved address ", address)
            change_matrix_functions = functions_dictionary[direction_change]
            try:
                # print(str(pc_matrix.get_pointer_value().address))
                address = change_matrix_functions[1]().address
                # print(str(address) + "address printed1")
                change_matrix_functions[0]()

                send_communication_handle.send(("2|" + data, address))

                matrix_communication_handle.send(pc_matrix)

                print("bla bla ", pc_matrix.get_pointer(),
                      pc_matrix.pointer.get_tuple())
                print(pc_matrix.get_pointer())
                if pc_matrix.pointer != pc_matrix.server_pointer:
                    print("change to other pc00000000 ", address)
                    # SetCursorPos(static_middle_position)
                    update_hooker_state_pipe.send(str(False))
                else:
                    print("change to server pc")
                    update_hooker_state_pipe.send(str(True))

            except Exception as e:  # exception handling
                print(str(e))




