from server.input_tracker import InputTracker
from multiprocessing import Process, Queue, Pipe
from threading import Thread, Lock
from win32api import GetSystemMetrics, SetCursorPos


def get_middle_position():
    return int(GetSystemMetrics(0)/2), int(GetSystemMetrics(1)/2)


def set_middle_mouse():
    SetCursorPos(get_middle_position())


class SessionManager:
    def __init__(self, server_network_manager, pc_matrix,
                 recv_communication_handle, send_communication_handle):

        self._pc_matrix = pc_matrix
        self._server_network_manager = server_network_manager

        # create connecting pipes and queues

        self.__recv_communication_handle = recv_communication_handle
        self.__send_communication_handle = send_communication_handle
        self.__ioinput_handle1, self.__ioinput_handle2 = Pipe()
        self.__matrix_communication_handle1, \
            self.__matrix_communication_handle2 = Pipe()
        self.__update_hooker_state_pipe1, \
            self.__update_hooker_state_pipe2 = Pipe()

        q = Queue()
        q.put(self._server_network_manager)

        # creating processes

        if self._pc_matrix.pointer != self._pc_matrix.server_pointer:
            temp = False
        else:
            temp = True

        self.__tracking_process = Process(
            target=self.initialize_tracking_process,
            args=(temp,))

        self.__data_send_process = Process(target=self.data_send)

        self.__track_changes_process = Process(
            target=self.track_changes)

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
            data, address = self.__recv_communication_handle.recv()
            # check if the controlled pc returns message through server
            # communication
            if data and address == \
                    self._pc_matrix.get_pointer_value().address:
                args = data.split('|')
                direction_change, position, resolution = \
                    args[0], eval(args[1]), eval(args[2])
                # print(
                #     "adres ", self._pc_matrix.get_pointer_value().address,
                #     " recieved address ", address)
                change_matrix_functions = functions_dictionary[
                    direction_change]
                try:
                    # print(str(pc_matrix.get_pointer_value().address))
                    address = change_matrix_functions[1]().address
                    # print(str(address) + "address printed1")
                    change_matrix_functions[0]()
                    # print(pc_matrix.get_pointer())
                    self.__send_communication_handle.send(("2|" + data,
                                                           address))
                    # print(str(pc_matrix.get_pointer_value().address))
                    self.__matrix_communication_handle2.send(
                        self._pc_matrix)

                    print("bla bla ", self._pc_matrix.get_pointer(),
                          self._pc_matrix.pointer.get_tuple())
                    print(self._pc_matrix.get_pointer())

                    if self._pc_matrix.pointer != \
                            self._pc_matrix.server_pointer:
                        print("change to other pc00000000 ", address)
                        # SetCursorPos(static_middle_position)
                        self.__update_hooker_state_pipe2.send(str(False))
                    else:
                        print("change to server pc")
                        self.__update_hooker_state_pipe2.send(str(True))

                except Exception as e:  # exception handling
                    print(str(e))

    def initialize_tracking_process(self, recv_state):
        InputTracker(self.__ioinput_handle1, self.__update_hooker_state_pipe1,
                     recv_state)

    def data_send(self):
        class DataSendingThread(Thread):

            def __init__(self, send_network_communication_pipe_handle,
                         recv_network_communication_pipe_handle,
                         matrix_communication_pipe_handle, temp_matrix,
                         thread_lock):
                Thread.__init__(self)
                self._send_handle = send_network_communication_pipe_handle
                self._recv_handle = \
                    recv_network_communication_pipe_handle
                self._matrix_communication_handle = \
                    matrix_communication_pipe_handle
                self._pc_matrix = temp_matrix
                self._lock = thread_lock

            def run(self):
                while 1:
                    data_recv = self._recv_handle.recv()
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
                        self._lock.release()

        threading_lock = Lock()

        functionality_class = DataSendingThread(
            self.__send_communication_handle, self.__ioinput_handle2,
            self.__matrix_communication_handle1, self._pc_matrix,
            threading_lock)
        functionality_class.start()
        functionality_class.change_data()

    def initialize_session(self):
        # initiate processes
        # this "if" below is to check if the pointer is on the server_pointer
        # for check. more needs to be added for tracker check
        self.__tracking_process.start()
        self.__data_send_process.start()
        self.__track_changes_process.start()

    def end_session(self):
        # stop processes
        self.__tracking_process.terminate()
        self.__data_send_process.terminate()
        self.__track_changes_process.terminate()






