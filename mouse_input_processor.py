from io_device_processor import DeviceInputProcessor

mouse_event_type_dictionary = {
    "c": "click", "m": "move", "w": "wheel"
}


class MouseInputProcessor(DeviceInputProcessor):

    def __init__(self, network_manager, current_pc, pc_list):
        DeviceInputProcessor.__init__(self, network_manager,
                                      current_pc, pc_list)

    def process_input(self, io_input):
        pass
