import socket


class ServerNetworkManager:

    def __init__(self, port, recv_length=1024):
        self.port = port
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._socket.bind(('', self.port))
        self._recv_length = recv_length

    def send_message(self, data, adrr):
        self._socket.sendto(data.encode(), adrr)

    # def new_connection(self):
    #     data = ""
    #     while not data:
    #         data, adrr = self._socket.recvfrom(self._recv_length)
    #     return adrr

    def recv_message(self):
        try:
            data, adrr = self._socket.recvfrom(self._recv_length)
            return data.decode(), adrr
        except:
            print("qweri")
            return 5, 5

    def close_connection(self):
        print("wuhu?")
        self._socket.close()

#
# def main():
#     ser = ServerNetworkManager(8835)
#     data, address = ser.recv_message()
#     print(data)
#     data = input("a")
#     while data != "gu":
#         ser.send_message(data, address)
#         data = input("a")
#     ser.close_connection()
#
#
# if __name__ == '__main__':
#     main()









