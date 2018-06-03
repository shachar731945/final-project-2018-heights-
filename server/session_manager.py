from server.input_tracker import InputTracker
from multiprocessing import Process, Pipe
from threading import Thread, Lock
from win32api import GetSystemMetrics, SetCursorPos


def get_middle_position():
    return int(GetSystemMetrics(0)/2), int(GetSystemMetrics(1)/2)


def set_middle_mouse():
    SetCursorPos(get_middle_position())


class SessionManager:
    def __init__(self, pc_matrix,
                 recv_communication_handle, send_communication_handle):
        """
        this function is the initializing function of the session manager. it
        creates the required processes for the server side program to work
        :param pc_matrix: the table of computers including the pointer of the
        session manager computer
        :param recv_communication_handle: the pipe to pass received information
        from the internet to the program
        :param send_communication_handle: the pipe to pass information to send
        information from the program to the server
        """

        self._pc_matrix = pc_matrix

        # create connecting pipes and queues

        self.__recv_communication_handle = recv_communication_handle
        self.__send_communication_handle = send_communication_handle
        self.__ioinput_handle1, self.__ioinput_handle2 = Pipe()
        self.__matrix_communication_handle1, \
            self.__matrix_communication_handle2 = Pipe()
        self.__update_hooker_state_pipe1, \
            self.__update_hooker_state_pipe2 = Pipe()

        # creating processes

        self.__tracking_process = Process(
            target=self.initialize_tracking_process,
            args=(self._pc_matrix.pointer == self._pc_matrix.server_pointer,))

        self.__data_send_process = Process(target=self.data_send)

        self.__track_changes_process = Process(
            target=self.track_changes)

    def track_changes(self):
        """
        this function receives input from the clients regarding a change in the
        pc matrix. this process analyzes this input, changes the pointer of the
        matrix accordingly and notifying the new controlled pc and the other
        server-side processes that regard the matrix
        :return: None
        """
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
                # separating the message to the required arguments
                args = data.split('|')
                direction_change, position, resolution = \
                    args[0], eval(args[1]), eval(args[2])
                # getting the functions to check and change matrix according
                # to the border direction
                change_matrix_functions = functions_dictionary[
                    direction_change]
                try:
                    # checking if a computer exists in the supposed location
                    # according to component of Computer class (that's why the
                    # exception exists)
                    address = change_matrix_functions[1]().address
                    # if a transition is possible, change the pointer in the
                    # matrix for the change
                    change_matrix_functions[0]()
                    # send a declaring massage to the new controlled computer
                    # in order for him to change the mouse location
                    self.__send_communication_handle.send(("2|" + data,
                                                           address))
                    # updating the other process that sends io input on the new
                    # updated pc_matrix with new pointer
                    self.__matrix_communication_handle2.send(
                        self._pc_matrix)
                    # updating the hooker of io input if the controlled pc is
                    # the server pc in order to de/confirm io input
                    self.__update_hooker_state_pipe2.send(str(
                        self._pc_matrix.pointer ==
                        self._pc_matrix.server_pointer))
                # exception handling for nothing because this is in case the
                # transition doesn't lead any other pc
                except Exception as e:  # exception handling
                    print(str(e))

    def initialize_tracking_process(self, recv_state):
        InputTracker(self.__ioinput_handle1, self.__update_hooker_state_pipe1,
                     recv_state)

    def data_send(self):
        """
        this function that represents a process receives io input data from the
        tracker and sends it to the controlled pc according to the pc matrix
        pointed Computer object. this function has an inside thread class just
        in order for the pc_matrix to be shared between the 2 threads so when
        the matrix is updated the sender thread will be updated as well.
        :return: None
        """
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
                """
                this function is the one that actually sends the io input
                information that is received by the pipe that connects the
                input_tracker process to this one to the pointed computer on
                the matrix
                :return: None
                """
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
                """
                this function is receiving the new updated matrix by another
                process on the server-side (the track_changes process that
                receives information from client). it updates the matrix
                so the sender thread will send the io input to the appropriate
                computer
                :return: None
                """
                while 1:
                    recv_data = self._matrix_communication_handle.recv()
                    if recv_data:
                        self._lock.acquire()
                        self._pc_matrix = recv_data
                        self._lock.release()

        # creating the thread lock for threading cooperation
        threading_lock = Lock()

        # creating the thread and starting the 2 threads of this process
        functionality_class = DataSendingThread(
            self.__send_communication_handle, self.__ioinput_handle2,
            self.__matrix_communication_handle1, self._pc_matrix,
            threading_lock)
        functionality_class.start()
        functionality_class.change_data()

    def initialize_session(self):
        # initiate processes
        self.__tracking_process.start()
        self.__data_send_process.start()
        self.__track_changes_process.start()

    def end_session(self):
        # stop processes
        self.__tracking_process.terminate()
        self.__data_send_process.terminate()
        self.__track_changes_process.terminate()






