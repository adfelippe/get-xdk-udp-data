# Simple Python script to get data sent from the Bosch XDK
# over UDP
import socket

HOST = ''      # Symbolic name meaning all available interfaces
PORT = 5005             # Port to listen to data
BUFFER_SIZE = 50        # Size of data buffer to be read


print('UDP Server for XDK Accelerometer and Gyroscope Data')
print('\r\nGetting socket...')
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Set socket to non-blocking mode
s.settimeout(1)
print('Binding...')
s.bind((HOST, PORT))

key = input("\r\n<Press ENTER to create log file and start saving data>")
print('\r\nWaiting for data...\r\n')
timeout_cnt = 0
while 1:
    try:
        data, addr = s.recvfrom(BUFFER_SIZE)
        print('Data: {}'.format(data))
        #TODO: Save data to log file
    except socket.timeout:
        #TODO: Close and save data log
        if (timeout_cnt >= 2):
            print('Timeout hit 3 times! Exiting...\r\n')
            break
        timeout_cnt += 1
s.close()
