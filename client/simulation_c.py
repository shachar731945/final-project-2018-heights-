from client.input_processor import InputProcessor
from client.client_network_manager import ClientNetworkManager
from multiprocessing import Queue, Pipe, Process


def getting_information(comm, queue):
    client = queue.get()
    while 1:
        data = client.recv_message()
        if data:
            comm.send(data)


def send_information(comm, queue):
    client = queue.get()
    while 1:
        data = comm.recv()
        if data:
            client.send_message(data)


def main():
    get_comm1, get_comm2 = Pipe()
    send_comm1, send_comm2 = Pipe()
    pipes = [get_comm1, get_comm2, send_comm1, send_comm2]
    client = ClientNetworkManager("192.168.0.25", 8845)
    client.send_message("test")
    q = Queue()
    q.put(client)
    q.put(client)
    p = Process(target=getting_information, args=(get_comm1, q,))
    p2 = Process(target=send_information, args=(send_comm1, q,))
    p.start()
    p2.start()
    input_processor = InputProcessor(get_comm2, send_comm2)
    input_processor.initialize()
    from time import sleep
    sleep(40)
    p.terminate()
    p2.terminate()
    input_processor.stop()
    client.close_connection()
    # for pipe in pipes:
    #     pipe.close()


class SessionClient:

    def __init__(self, client_manager):
        self.client = client_manager
        get_comm1, get_comm2 = Pipe()
        send_comm1, send_comm2 = Pipe()
        pipes = [get_comm1, get_comm2, send_comm1, send_comm2]
        q = Queue()
        q.put(self.client)
        q.put(self.client)
        self.p = Process(target=getting_information, args=(get_comm1, q,))
        self.p2 = Process(target=send_information, args=(send_comm1, q,))
        self.input_processor = InputProcessor(get_comm2, send_comm2)

    def start_session(self):
        self.p.start()
        self.p2.start()
        self.input_processor.initialize()

    def stop_session(self):
        self.p.terminate()
        self.p2.terminate()
        self.input_processor.stop()


if __name__ == "__main__":
    from time import sleep
    sleep(1.5)
    main()


