import socket


class ClientNetworkManager:

    def __init__(self, ip, port, recv_length=1024):
        self._recv_length = recv_length
        self._send_ip = ip
        self._send_port = port
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send_message(self, message):
        self._socket.sendto(message, (self._send_ip, self._send_port))

    def recv_message(self):
        data, addr = self._socket.recvfrom(self._recv_length)
        return data.decode()




