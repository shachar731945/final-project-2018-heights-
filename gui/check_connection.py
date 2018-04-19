import socket
from time import sleep

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
while 1:
    sock.sendto("gugu".encode(), ("127.0.0.1", 8845))
    print("ok")
    sleep(1)




