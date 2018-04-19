import socket
from wx import PostEvent
import select

def get_local_ip_address():
    return str(socket.gethostbyname(socket.gethostname()))


class ServerNetworkManager:

    def __init__(self, port=8845, recv_length=1024):
        self.port = port
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._socket.bind(('', self.port))
        self._recv_length = recv_length

    def send_message(self, data, adrr):
        print("gugu? ", data)
        self._socket.sendto(str(data).encode(), adrr)

    # def new_connection(self):
    #     data = ""
    #     while not data:
    #         data, adrr = self._socket.recvfrom(self._recv_length)
    #     return adrr

    def recv_message(self):
        # try:
        #     data, adrr = self._socket.recvfrom(self._recv_length)
        #     return data.decode(), adrr
        # except:
        #     print("qweri")
        #     return 5, 5

        data, adrr = self._socket.recvfrom(self._recv_length)
        return data.decode(), adrr

    def recv_message_non_block(self):
        self._socket.settimeout(0.01)
        try:
            return self.recv_message()
        except socket.timeout:
            return "", ""
        finally:
            self._socket.settimeout(0)

    def recv_clients_function(self, wx_object, custome_event, lock,
                              confirm_state):
        loop = True
        while loop:
            if not confirm_state:
                print("gugugugu i ended the process")
                self._socket.settimeout(0)
                loop = False
            data, adrr = self.recv_message_non_block()
            if data:
                custome_event.data = adrr
                PostEvent(wx_object, custome_event)
                from time import sleep
                sleep(0.00001)
                lock.acquire()
                self.send_message(custome_event.data, adrr)
                lock.release()

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









