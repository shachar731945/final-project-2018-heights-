from client.mouse_input_processor import MouseInputProcessor
from client.keyboard_input_processor import KeyboardInputProcessor
from time import sleep
from win32api import GetCursorPos, GetSystemMetrics
from multiprocessing import Process


class InputProcessor:

    def __init__(self, get_comm_handle, send_comm_handle):
        self._event_type_dictionary = {
            "m": 0,
            "k": 1
        }
        self._get_data_handle = get_comm_handle
        self._send_data_handle = send_comm_handle
        self._io_devices_processors = []
        self._io_devices_processors.append(MouseInputProcessor())
        self._io_devices_processors.append(KeyboardInputProcessor())
        # print(id(self._client_network_manager), "out process")
        self._tracking_input_process = Process(
            target=self.initialize_process, args=())
        self._tracking_changes_process = Process(target=self.track_changes)

    def initialize(self):
        self._tracking_input_process.start()
        self._tracking_changes_process.start()

    def initialize_process(self):
        # print(id(self._client_network_manager), "in process")
        print("gg ez pz")
        # self._send_data_handle.send("test")
        while 1:
            print("damn")
            data, adrr = self._get_data_handle.recv()
            print(data)
            if data:
                io_device_processor_index = self.identify_io_device(data)
                processor = \
                    self._io_devices_processors[io_device_processor_index]
                processor.process_input(data[data.index('|')+1:])

    def track_changes(self):
        # print(id(self._client_network_manager))
        resolution_x, resolution_y = InputProcessor.get_screen_resolution()
        print("resolution is ", resolution_x, " ", resolution_y)
        while 1:
            pos_x, pos_y = InputProcessor.get_mouse__position()
            print(pos_x, " posses ", pos_y)
            return_message = ""
            if pos_x <= 0:
                return_message += "l"
            elif pos_x >= resolution_x:
                return_message += "r"
            if pos_y <= 0:
                return_message += "u"
            elif pos_y >= resolution_y:
                return_message += "d"
            if return_message:
                print("bicth you guessed it?")
                self._send_data_handle.send(return_message)

    def stop(self):
        self._tracking_input_process.terminate()
        self._tracking_changes_process.terminate()

    def identify_io_device(self, data):
        return self._event_type_dictionary[data.split('|')[0]]

    @staticmethod
    def get_mouse__position():
        return GetCursorPos()

    @staticmethod
    def get_screen_resolution():
        return GetSystemMetrics(0), GetSystemMetrics(1)




