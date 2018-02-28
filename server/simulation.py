from server_network_manager import ServerNetworkManager
from matrix import Matrix
from computer import Computer
from session_manager import SessionManager

server = ServerNetworkManager(8820)
pc_matrix = Matrix(1, 2)
pc_controller = Computer(("192.168.0.20", 8821))
pc_controlled = Computer(("192.168.0.25", 8822))
pc_matrix.set(0, 1, pc_controller)
pc_matrix.set(0, 0, pc_controlled)
session_manager = SessionManager(server, pc_matrix)
session_manager.initialize_session()
a = raw_input("4")
while a != "*":
    a = raw_input("4")
session_manager.end_session()



