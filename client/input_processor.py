from client.mouse_input_processor import MouseInputProcessor
from client.keyboard_input_processor import KeyboardInputProcessor
from time import sleep
from win32api import GetCursorPos, GetSystemMetrics, SetCursorPos
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
            input_type = data.split("|")[0]
            data = data[data.index('|') + 1:]
            if input_type == "1":
                print("glida", 1)
                io_device_processor_index = self.identify_io_device(data)
                processor = \
                    self._io_devices_processors[io_device_processor_index]
                processor.process_input(data[data.index('|') + 1:])
            elif input_type == "2":
                print("glida", 2)
                args = data.split('|')
                direction_change, position, resolution = \
                    args[0], eval(args[1]), eval(args[2])
                new_position = self.get_new_position(
                    direction_change, position, resolution)
                print("setting mouse to", new_position)
                SetCursorPos(new_position)

    @staticmethod
    def get_new_position(direction_change, old_position, old_resolution):
        new_resolution_x, new_resolution_y = \
            InputProcessor.get_screen_resolution()
        if direction_change == "l":
            new_position_x = new_resolution_x - 2
            new_position_y = InputProcessor.find_according_to_ratio(
                old_resolution[1], old_position[1], new_resolution_y) - 2
        elif direction_change == "r":
            new_position_x = 2
            new_position_y = InputProcessor.find_according_to_ratio(
                old_resolution[1], old_position[1], new_resolution_y) - 2
        elif direction_change == "u":
            new_position_x = InputProcessor.find_according_to_ratio(
                old_resolution[0], old_position[0], new_resolution_x) - 2
            new_position_y = new_resolution_y - 2
        else:
            new_position_x = InputProcessor.find_according_to_ratio(
                old_resolution[0], old_position[0], new_resolution_x) - 2
            new_position_y = 2
        return new_position_x, new_position_y

    @staticmethod
    def find_according_to_ratio(old_resolution, old_pos, new_resolution):
        return int(old_pos * new_resolution / old_resolution)

    def track_changes(self):
        # print(id(self._client_network_manager))
        resolution_x, resolution_y = InputProcessor.get_screen_resolution()
        check_resolution_x, check_resolution_y = \
            resolution_x - 1, resolution_y - 1
        print("resolution is ", resolution_x, " ", resolution_y)
        while 1:
            pos_x, pos_y = InputProcessor.get_mouse__position()
            print(pos_x, " posses ", pos_y)
            return_message = ""
            if pos_x <= 1:
                return_message = "l"
            elif pos_x >= check_resolution_x:
                return_message = "r"
            if pos_y <= 1:
                return_message = "u"
            elif pos_y >= check_resolution_y:
                return_message = "d"
            if return_message:
                print("bit you guessed it?")
                # SetCursorPos((int(resolution_x/2), int(resolution_y/2)))
                self._send_data_handle.send(str(return_message) + "|" +
                                            str((pos_x, pos_y)) + "|" +
                                            str((resolution_x, resolution_y)))

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




