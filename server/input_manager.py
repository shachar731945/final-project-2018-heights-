from time import sleep
from win32api import GetSystemMetrics, SetCursorPos
from threading import Thread, Lock
from multiprocessing import Queue


class InputManager:
    def __init__(self, comm, server_pc_address=(0, 0)):
        self._communication_pipe_handle = comm
        self._server_pc_address = server_pc_address
        # self._server_pc_coordinates = server_pc_coordinates
        # False if no server pc, use in future for mouse hide if self control

    @staticmethod
    def data_send(q, network_communication_handle, matrix_communication_handle,
                  matrix):

        class DataSendingThread(Thread):

            def __init__(self, communication_server,
                         network_communication_pipe_handle,
                         matrix_communication_pipe_handle, temp_matrix,
                         thread_lock):
                Thread.__init__(self)
                self._server = communication_server
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
                        print(str(self._pc_matrix.get_pointer()))
                        #     print("send to " + str(pc.address))
                        self._lock.release()
                        self._server.send_message(data_recv, pc.address)

            def change_data(self):
                while 1:
                    recv_data = self._matrix_communication_handle.recv()
                    if recv_data:
                        self._lock.acquire()
                        self._pc_matrix = recv_data
                        print("updated " + str(self._pc_matrix.get_pointer()))
                        self._lock.release()

        threading_lock = Lock()
        server = q.get()

        functionality_class = DataSendingThread(
            server, network_communication_handle,
            matrix_communication_handle, matrix, threading_lock)
        functionality_class.start()
        functionality_class.change_data()

    def track_changes(self, matrix_communication_handle, pc_matrix):
        functions_dictionary = {'l': (pc_matrix.pointer_left,
                                      pc_matrix.check_left),
                                'r': (pc_matrix.pointer_right,
                                      pc_matrix.check_right),
                                'u': (pc_matrix.pointer_up,
                                      pc_matrix.check_up),
                                'd': (pc_matrix.pointer_down,
                                      pc_matrix.check_down)}
        while 1:
            return_data, address = self._communication_pipe_handle.recv()
            # check if the controlled pc returns message
            if return_data and address == \
                    pc_matrix.get_pointer_value().address:
                print(return_data)
                for char in return_data:
                    print(char + " this is the char")
                    change_matrix_functions = functions_dictionary[char]
                    try:
                        print(str(pc_matrix.get_pointer_value().address))
                        address = change_matrix_functions[1]().address
                        print(str(address) + "address printed1")
                        change_matrix_functions[0]()
                        print(pc_matrix.get_pointer())
                        print(str(pc_matrix.get_pointer_value().address))
                        matrix_communication_handle.send(pc_matrix)
                        # if address == self._server_pc_address:
                        #     print("A")
                    except Exception as e:  # exception handling
                        print(str(e))
                        # if pc_matrix.get_pointer() == \
                        #         self._server_pc_coordinates:
                        #     pass

    @staticmethod
    def position_mouse_on_middle():
        position = GetSystemMetrics()
        SetCursorPos(position[0] / 2, position[1] / 2)
