
def main():
    from multiprocessing import Process, Pipe
    father, child = Pipe()
    p_track = Process(target=create_traking, args=(father, ))
    p_process = Process(target=track_input, args=(child, ))
    p_track.start()
    p_process.start()
    from time import sleep
    sleep(3)
    print("geezzzzzzzzzzzzzzzzzzzz")
    p_track.terminate()
    p_process.terminate()


def create_traking(comm):
    from input_hub import InputHub
    input_hub = InputHub(comm)
    a = InputTracker(True, input_hub)


def track_input(comm):
    print("bla there")
    while 1:
        data = comm.recv()
        print("hi3 " + data)
        if data:
            print(data)
            print("hi4")


if __name__ == '__main__':
    main()


