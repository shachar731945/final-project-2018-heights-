from server_network_manager import ServerNetworkManager
from matrix import Matrix
from computer import Computer
from session_manager import SessionManager
from multiprocessing import Process, Queue, Pipe
from time import sleep


def getting_information(comm, queue):
    servur = queue.get()
    while 1:
        data = servur.recv_message()
        if data:
            comm.send(data)


def main():
    server = ServerNetworkManager(8820)
    pc_matrix = Matrix(1, 2)
    pc_controller = Computer(("192.168.0.20", 8821))
    pc_controlled = Computer(("192.168.0.25", 8822))
    pc_matrix.set(0, 1, pc_controller)
    pc_matrix.set(0, 0, pc_controlled)
    q = Queue()
    q.put(server)
    comm1, comm2 = Pipe()
    session_manager = SessionManager(server, pc_matrix, comm2)
    p = Process(target=getting_information, args=(comm1, q,))
    p.start()
    print("bla")
    session_manager.initialize_session()
    sleep(10)
    p.terminate()
    session_manager.end_session()


if __name__ == '__main__':
    main()









