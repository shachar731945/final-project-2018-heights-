from input_hub import InputHub
from input_tracker import InputTracker
from input_manager import InputManager
from multiprocessing import Process, Pipe


class SessionManager:
    def __init__(self, server_network_manager, pc_matrix):
        communication_handle1, communication_handle2 = Pipe()
        self._server_network_manager = server_network_manager
        self._pc_matrix = pc_matrix
        self._input_hub = InputHub(communication_handle1)
        self._input_manager = InputManager(communication_handle2,
                                           self._server_network_manager,
                                           self._pc_matrix)
        # create processes
        self.__tracking_process = Process(
            target=self.initialize_tracking_process, args=())
        self.__input_managing_process = Process(
            target=self._input_manager.initialize, args=())
        self.__changes_managing_process = Process(
            target=self._input_manager.track_changes, args=())

    def initialize_tracking_process(self):
        temp = InputTracker(False, self._input_hub)

    def initialize_session(self):
        # initiate processes
        self.__tracking_process.start()
        self.__input_managing_process.start()
        self.__changes_managing_process.start()

    def end_session(self):
        # stop processes
        self.__tracking_process.terminate()
        self.__input_managing_process.terminate()
        self.__changes_managing_process.terminate()





