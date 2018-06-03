from client.mouse_input_processor import MouseInputProcessor
from client.keyboard_input_processor import KeyboardInputProcessor
from win32api import GetCursorPos, GetSystemMetrics, SetCursorPos
from multiprocessing import Process


class InputProcessor:

    def __init__(self, get_comm_handle, send_comm_handle):
        """
        this function is the initializing function of the instance of this
        class. it creates the 2 processes in order from the client to function
        and it sets the io input processors when io input comes from the server
        :param get_comm_handle: the pipe to pass received information
        from the network to the program (through ClientNetworkManager)
        :param send_comm_handle: the pipe to pass information for sending
        from the program to the server through network
        """
        self._event_type_dictionary = {
            "m": 0,
            "k": 1
        }
        self._get_data_handle = get_comm_handle
        self._send_data_handle = send_comm_handle
        self._io_devices_processors = []
        self._io_devices_processors.append(MouseInputProcessor())
        self._io_devices_processors.append(KeyboardInputProcessor())
        # sets the processes of the client
        self._tracking_input_process = Process(
            target=self.track_input_initialize, args=())
        self._tracking_changes_process = Process(target=self.track_changes)

    def initialize(self):
        self._tracking_input_process.start()
        self._tracking_changes_process.start()

    def track_input_initialize(self):
        """
        this function tracks the received information from the server and
        analyzes it. If it is an io input it sends it to the correct input
        processor. On the other hand, if this input is an input that declares
        a change in pc control oto this client it analyzes the information and
        changes the mouse position accordingly
        :return: None
        """
        while 1:
            data, adrr = self._get_data_handle.recv()
            input_type = data.split("|")[0]
            data = data[data.index('|') + 1:]
            if input_type == "1":
                io_device_processor_index = self.identify_io_device(data)
                processor = \
                    self._io_devices_processors[io_device_processor_index]
                processor.process_input(data[data.index('|') + 1:])
            elif input_type == "2":
                args = data.split('|')
                direction_change, position, resolution = \
                    args[0], eval(args[1]), eval(args[2])
                new_position = self.get_new_position(
                    direction_change, position, resolution)
                print("setting mouse to", new_position)
                SetCursorPos(new_position)

    @staticmethod
    def get_new_position(direction_change, old_position, old_resolution):
        """
        this function builds the new position of the mouse that should be
        set in order to create smooth transition between 2 computers
        :param direction_change: the border that the previous controlled pc
        collided with
        :param old_position: the position of the previous controlled pc at the
        moment of collision
        :param old_resolution: the resolution of the previous controlled pc
        :return: the new position that should be updated
        """
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
        """
        this function is a mathematical tool in order form the "new position"
        according to the ratio function in math which states
        old_resolution/old_pos = new_resolution/new_pos
        of course that the names of position and resolution are only here for
        understanding of code and can be replaced with any other option
        :param old_resolution: the old resolution (single number for single
        dimension)
        :param old_pos: the old position (single number for single dimension)
        :param new_resolution: the new resolution (single number for single
        dimension)
        :return: the new_pos according to the math ratio function
        """
        return int(old_pos * new_resolution / old_resolution)

    def track_changes(self):
        """
        this function checks if the mouse collides with one the screen's
        borders and according to so sends msg to the server about the change
        :return: None
        """
        # build the resolution to check for changes
        resolution_x, resolution_y = InputProcessor.get_screen_resolution()
        check_resolution_x, check_resolution_y = \
            resolution_x - 1, resolution_y - 1
        while 1:
            pos_x, pos_y = InputProcessor.get_mouse__position()
            # building the return msg according to the side of the screen's
            # border that the mouse collides (if there is one)
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
                # return the side of collision, current position and resolution
                # for ratio checking in the other client's pc
                SetCursorPos((int(resolution_x/2), int(resolution_y/2)))
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




