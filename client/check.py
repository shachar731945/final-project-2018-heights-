import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 8897))

stuff = ["k|p|" + str(0x30), "k|r|" + str(0x30), "m|m|" + str((300, 300)),
         "m|w|" + str(5), "m|c|l|d", "m|c|l|u", "m|c|m|d", "m|c|m|u",
         "m|c|r|d", "m|c|r|u"]
a = len(stuff)

import time
import random
data = ""
while not data:
    data, adrr = sock.recvfrom(1024)
raw_input("nibba")
time.sleep(5)
while 1:
    # index = random.randint(0, 1)
    index = 3
    sock.sendto(stuff[index], adrr)
    print "hi"
    import time
    time.sleep(0.1)




