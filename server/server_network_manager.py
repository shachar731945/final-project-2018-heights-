import socket


class ServerNetworkManager:

    def __init__(self, port, recv_length=1024):
        self.port = port
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._socket.bind(("0.0.0.0", self.port))
        self._recv_length = recv_length

    def send_message(self, data, adrr):
        self._socket.sendto(data.encode(), adrr)

    # def new_connection(self):
    #     data = ""
    #     while not data:
    #         data, adrr = self._socket.recvfrom(self._recv_length)
    #     return adrr

    def recv_message(self):
        data, adrr = self._socket.recvfrom(self._recv_length)
        return data









