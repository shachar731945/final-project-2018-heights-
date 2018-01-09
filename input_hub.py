class InputHub:

    def __init__(self, process_to_input_to):
        self._subprocess_handle = process_to_input_to

    def send_input(self, io_input):
        self._subprocess_handle.stdin.write(io_input)
        # process.stdin.readline() process.stdin.flush()



