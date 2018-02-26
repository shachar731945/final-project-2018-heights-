class InputHub:

    def __init__(self, process_communication):
        self._process_communication_handle = process_communication

    def send_input(self, io_input):
        self._process_communication_handle.send(io_input)


# this functions should be on the main program


# def f(childi):
#     from input_processor import InputProcessor
#     a = InputProcessor("a", childi)
#     a.initialize()
#  parent, child = multiprocessing.Pipe()
#
# def main():
#     import multiprocessing
#     import time
#     parent, child = multiprocessing.Pipe()
#     p = multiprocessing.Process(target=f, args=(child,))
#     p.start()
#     current = time.time()
#     while time.time() < current + 5:
#         time.sleep(0.8)
#         print "damn"
#         parent.send("ma kore")
#     p.terminate()









