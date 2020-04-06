# Simple Python script to get data sent from the Bosch XDK
# over UDP
import socket

HOST = ''               # Symbolic name meaning all available interfaces
PORT = 5005             # Port to listen to data
BUFFER_SIZE = 50        # Size of data buffer to be read


print('UDP Server for XDK Accelerometer and Gyroscope Data')
print('\r\nGetting socket...')
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Set socket to non-blocking mode
s.settimeout(3)
print('Binding...')
s.bind((HOST, PORT))

print('\r\n<Press ENTER to create log file and start saving data>')
key = input("<Press s to stop saving data and close the log file>")
print('\r\nWaiting for data...\r\n')
timeout_cnt = 0

while 1:
    try:
        data, addr = s.recvfrom(BUFFER_SIZE)
        data = data.decode("utf-8")
        print('Data: {}'.format(data))
        #key = input()
        #if (key == 's' or key == 'S'):
        #    break
        timeout_cnt = 0
        #TODO: Save data to log file
    except socket.timeout:
        #TODO: Close and save data log
        print('[WARNING] Socket reception timeout!\r\n')
        timeout_cnt += 1
        if timeout_cnt >= 3:
            print('[ERROR] Maximum timeout reached. Exiting...\r\n')
            break

s.close()
exit()
