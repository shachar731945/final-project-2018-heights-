import socket
from wx import PostEvent


def get_local_ip_address():
    """
    :return: this function is used in order to return the current ip of the
    server computer
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


class ServerNetworkManager:
    """
    the ServerNetworkManager is a class that connects through UDP
    socket to other computers as a server and provides services with the socket
    communication such as receiving and sending information
    """

    def __init__(self, port=8845, recv_length=1024):
        """
        this function initializes the ServerNetworkManager class and creates
        the server socket
        :param port: the port to open the socket to
        :param recv_length: the max length of a single receive in bytes
        """
        self.port = port
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._socket.bind(('', self.port))
        self._recv_length = recv_length

    def send_message(self, data, adrr):
        """
        this function sends a message through the socket to a connected client
        socket
        :param data: the data to be sent
        :param adrr: the address of the computer that the data is sent to
        """
        self._socket.sendto(str(data).encode(), adrr)

    def recv_message(self):
        """
        this function receives data from a connected client socket
        to this server socket. this receive is blocking and wont continue until
        a message is received
        :return: the data and the sender of the receiving message
        """
        data, adrr = self._socket.recvfrom(self._recv_length)
        return data.decode(), adrr

    def recv_message_non_block(self):
        """
        this function receives a message like recv_message function in a
        non-blocking way. it means that if a message is not received in a
        determined time range the function will return '', '' and if it
        receives a message it will return (just as recv_message function does)
        the data and the address of the received message
        :return: '', '' if no message is received and data and address of
        sender in case a message is received
        """
        self._socket.settimeout(0.01)  # updating socket timeout
        try:
            temp = self.recv_message()
            return temp[0], temp[1]
        except socket.timeout:
            return "", ""
        finally:
            self._socket.settimeout(0)
        # setting the socket timeout property back

    def recv_clients_function(self, wx_object, custome_event, lock,
                              confirm_state):
        """
        this function is used in cooperation with the gui in order to receive
        client connection attempts and post wxEvent accordingly. this will
        update the gui and the system on the new connected clients.
        :param wx_object: the Frame object to have connection with the event
        posted
        :param custome_event: a wxEvent with a unique wxID to be posted
        :param lock: the thread lock in order to post event data which is the
        new connected computer
        :param confirm_state: a thread event in order to stop the run of this
        thread
        :return: nothing
        """
        while not confirm_state.is_set():
            data, adrr = self.recv_message_non_block()
            if data:
                custome_event.data = adrr
                PostEvent(wx_object, custome_event)
                from time import sleep
                sleep(0.00001)
                lock.acquire()
                self.send_message(custome_event.data, adrr)
                lock.release()
        self._socket.setblocking(1)

    def close_connection(self):
        """
        closing the socket 
        """
        self._socket.close()
