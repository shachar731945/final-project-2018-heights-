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


def send_information(comm, queue):
    servur = queue.get()
    while 1:
        (data, adrr) = comm.recv()
        if data:
            servur.send_message(data, adrr)


def main():
    server = ServerNetworkManager(8845)
    pc_matrix = Matrix(2, 1, (0, 0))
    print(33)
    data, adrr = server.recv_message()
    print("juju ", adrr)
    pc_controlled = Computer(adrr)
    data, adrr = server.recv_message()
    print("juju ", adrr)
    pc_controller = Computer(adrr)
    pc_matrix.set(1, 0, pc_controller)
    pc_matrix.set(0, 0, pc_controlled)
    q1 = Queue()
    q2 = Queue()
    q1.put(server)
    q2.put(server)
    recv_communication_handle1, recv_communication_handle2 = Pipe()
    send_network_comm1, send_network_comm2 = Pipe()
    pipes = [recv_communication_handle1, recv_communication_handle2,
             send_network_comm1, send_network_comm2]
    session_manager = SessionManager(server, pc_matrix,
                                     recv_communication_handle2,
                                     send_network_comm2)
    p = Process(target=getting_information, args=(recv_communication_handle1,
                                                  q1,))
    p2 = Process(target=send_information, args=(send_network_comm1, q2,))
    p.start()
    p2.start()
    print("blasasd")
    session_manager.initialize_session()
    sleep(40)
    p.terminate()
    p2.terminate()
    session_manager.end_session()
    server.close_connection()
    # for pipe in pipes:
    #     pipe.close()


if __name__ == '__main__':
    main()









