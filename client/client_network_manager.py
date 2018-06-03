import socket


class ClientNetworkManager:

    def __init__(self, ip, port=8845, recv_length=1024):
        self._recv_length = recv_length
        self._send_ip = ip
        self._send_port = port
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def send_message(self, message):
        self._socket.sendto(message.encode(), (self._send_ip, self._send_port))

    def recv_message(self):
        data, addr = self._socket.recvfrom(self._recv_length)
        return data.decode(), addr

    def close_connection(self):
        self._socket.close()

