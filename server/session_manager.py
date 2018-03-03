from input_tracker import InputTracker
from input_manager import InputManager
from multiprocessing import Process, Queue, Pipe


class SessionManager:
    def __init__(self, server_network_manager, pc_matrix,
                 communication_handle):
        self._server_network_manager = server_network_manager
        self._pc_matrix = pc_matrix
        self._input_manager = InputManager(
            self._pc_matrix, communication_handle)
        # create connectiong pipes and queues
        communication_handle1, communication_handle2 = Pipe()
        q = Queue()
        q.put(self._server_network_manager)
        # create processes
        self.__tracking_process = Process(
            target=self.initialize_tracking_process,
            args=(communication_handle1, ))

        self.__send_input_process = Process(
            target=self._input_manager.data_send,
            args=(q, communication_handle2))

        self.__changes_managing_process = Process(
            target=self._input_manager.track_changes, args=())

    @staticmethod
    def initialize_tracking_process(communication_handle):
        InputTracker(False, communication_handle)

    def initialize_session(self):
        # initiate processes
        self.__tracking_process.start()
        self.__changes_managing_process.start()
        self.__send_input_process.start()

    def end_session(self):
        # stop processes
        self.__tracking_process.terminate()
        self.__changes_managing_process.terminate()
        self.__send_input_process.terminate()





