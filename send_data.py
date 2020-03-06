# Echo client program
import socket
import time

HOST = '192.168.88.48'    # The remote host
PORT = 5005              # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((HOST, PORT))

for i in range(0, 100):
    s.sendto(b'Hello, world', (HOST, PORT))
    #time.sleep(0.1)
s.close()
