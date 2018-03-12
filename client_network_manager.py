import socket


class ClientNetworkManager:

    def __init__(self, ip, port, recv_length=1024):
        self._recv_length = recv_length
        self._send_ip = ip
        self._send_port = port
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def send_message(self, message):
        self._socket.sendto(message.encode(), (self._send_ip, self._send_port))

    def recv_message(self):
        print("gg")
        try:
            data, addr = self._socket.recvfrom(self._recv_length)
            return data.decode(), addr
        except:
            print("asdf")
            return "blaaa", 00

    def close_connection(self):
        self._socket.close()


def main():
    client = ClientNetworkManager("192.168.0.20", 8835)
    client.send_message("gigi")
    data = client.recv_message()[0]
    while data != "da":
        print(data)
        data = client.recv_message()[0]
    client.close_connection()


if __name__ == '__main__':
    main()




