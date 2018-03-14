from input_tracker import InputTracker
from input_manager import InputManager
from multiprocessing import Process, Queue, Pipe
from time import sleep


class SessionManager:
    def __init__(self, server_network_manager, pc_matrix,
                 communication_handle):
        self._server_network_manager = server_network_manager
        # self._pc_matrix = pc_matrix
        self._input_manager = InputManager(communication_handle)
        # create connectiong pipes and queues
        communication_handle1, communication_handle2 = Pipe()
        # create processes
        self.__tracking_process = Process(
            target=self.initialize_tracking_process,
            args=(communication_handle1, ))

        q = Queue()
        q.put(self._server_network_manager)

        matrix_communication_handle1, matrix_communication_handle2 = Pipe()

        self.__data_send_process = Process(
            target=self._input_manager.data_send,
            args=(q, communication_handle2,
                  matrix_communication_handle1, pc_matrix))

        self.__track_changes_process = Process(
            target=self._input_manager.track_changes,
            args=(matrix_communication_handle2, pc_matrix))

    @staticmethod
    def initialize_tracking_process(communication_handle):
        InputTracker(communication_handle)

    def initialize_session(self):
        # initiate processes
        self.__tracking_process.start()
        self.__data_send_process.start()
        sleep(0.1)
        self.__track_changes_process.start()

    def end_session(self):
        # stop processes
        self.__tracking_process.terminate()
        self.__data_send_process.terminate()
        sleep(0.1)
        self.__track_changes_process.terminate()





