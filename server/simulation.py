from server.server_network_manager import ServerNetworkManager
from server.server_matrix import ServerMatrix
from server.computer import Computer
from server.session_manager import SessionManager
from multiprocessing import Process, Queue, Pipe
from time import sleep


def getting_information(comm, queue):
    servur = queue.get()
    while 1:
        data = servur.recv_message()
        if data:
            comm.send(data)


def send_information(comm, queue):
    servur = queue.get()
    while 1:
        (data, adrr) = comm.recv()
        if data:
            servur.send_message(data, adrr)


def main():
    server = ServerNetworkManager(8845)
    pc_matrix = ServerMatrix(1, 2, 0, 0, 0, 1)
    print(33)
    data, adrr = server.recv_message()
    print("juju ", adrr)
    pc_controlled = Computer(adrr)
    data, adrr = server.recv_message()
    print("juju ", adrr)
    pc_controller = Computer(adrr)
    pc_matrix.set(0, 1, pc_controller)
    pc_matrix.set(0, 0, pc_controlled)
    q = Queue()
    q.put(server)
    q.put(server)
    recv_communication_handle1, recv_communication_handle2 = Pipe()
    send_network_comm1, send_network_comm2 = Pipe()
    pipes = [recv_communication_handle1, recv_communication_handle2,
             send_network_comm1, send_network_comm2]
    session_manager = SessionManager(pc_matrix,
                                     recv_communication_handle2,
                                     send_network_comm2)
    p = Process(target=getting_information, args=(recv_communication_handle1,
                                                  q,))
    p2 = Process(target=send_information, args=(send_network_comm1, q,))
    p.start()
    p2.start()
    print("blasasd")
    session_manager.initialize_session()
    sleep(20)
    p.terminate()
    p2.terminate()
    session_manager.end_session()
    server.close_connection()
    # for pipe in pipes:
    #     pipe.close()


class SessionMain:
    def __init__(self, server, pc_matrix):
        self.server = server
        self.pc_matrix = pc_matrix
        # self.server_pc_coordinates = server_pc_coordinates
        q = Queue()
        q.put(server)
        q.put(server)
        recv_communication_handle1, recv_communication_handle2 = Pipe()
        send_network_comm1, send_network_comm2 = Pipe()
        pipes = [recv_communication_handle1, recv_communication_handle2,
                 send_network_comm1, send_network_comm2]
        self.session_manager = SessionManager(pc_matrix,
                                              recv_communication_handle2,
                                              send_network_comm2)
        self.p = Process(target=getting_information,
                         args=(recv_communication_handle1,
                               q,))
        self.p2 = Process(target=send_information, args=(
            send_network_comm1, q,))

    def start_main(self):
        self.p.start()
        self.p2.start()
        self.session_manager.initialize_session()

    def stop_session(self):
        self.p.terminate()
        self.p2.terminate()
        self.session_manager.end_session()


if __name__ == '__main__':
    main()
