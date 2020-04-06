# Echo client program
import socket
import time

HOST = '192.168.0.3'    # The remote host
PORT = 5005              # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((HOST, PORT))

for i in range(0, 25):
    s.sendto(b'DATAG', (HOST, PORT))
    time.sleep(1)
s.close()
