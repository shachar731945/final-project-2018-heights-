from server.input_tracker import InputTracker
from server.input_manager import data_send, track_changes
from multiprocessing import Process, Queue, Pipe
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

        communication_handle1, communication_handle2 = Pipe()
        matrix_communication_handle1, matrix_communication_handle2 = Pipe()
        update_hooker_state_pipe1, update_hooker_state_pipe2 = Pipe()
        self.__pipes = [communication_handle1, communication_handle2,
                        matrix_communication_handle1,
                        matrix_communication_handle2,
                        update_hooker_state_pipe1, update_hooker_state_pipe2]

        q = Queue()
        q.put(self._server_network_manager)

        set_middle_mouse()

        # creating processes

        if self._pc_matrix.pointer != self._pc_matrix.server_pointer:
            temp = False
        else:
            temp = True

        self.__tracking_process = Process(
            target=self.initialize_tracking_process,
            args=(communication_handle1, get_middle_position(),
                  update_hooker_state_pipe1, temp))

        self.__data_send_process = Process(
            target=data_send,
            args=(communication_handle2, matrix_communication_handle1,
                  send_communication_handle, pc_matrix))

        self.__track_changes_process = Process(
            target=track_changes,
            args=(matrix_communication_handle2, recv_communication_handle,
                  pc_matrix, update_hooker_state_pipe2))

    @staticmethod
    def initialize_tracking_process(communication_handle, static_position,
                                    update_hooker_state_pipe, recv_state):
        InputTracker(communication_handle, static_position,
                     update_hooker_state_pipe, recv_state)

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
        for pipe in self.__pipes:
            pipe.close()






