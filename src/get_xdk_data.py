# Simple Python script to get data sent from the Bosch XDK
# over UDP
import socket
from datetime import datetime

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
# Get current data and time
current_time = datetime.now()
date_time = current_time.strftime("%d-%m-%Y_%H-%M-%S")

# Set file name and open it
filename = 'raw_sensor_data_'
filename += date_time + '.log'
log_file = open(filename, 'a')

print('\r\nWaiting for data...\r\n')
timeout_cnt = 0

while 1:
    try:
        data, addr = s.recvfrom(BUFFER_SIZE)
        data = data.decode("utf-8")
        print('Data: {}'.format(data))
        data = data.rstrip(' \t\r\n\0')
        log_file.write(data + '\n')
        timeout_cnt = 0
    except socket.timeout:
        print('[WARNING] Socket reception timeout!\r\n')
        timeout_cnt += 1
        if timeout_cnt >= 3:
            print('[ERROR] Maximum timeout reached. Exiting...\r\n')
            log_file.close()
            break

s.close()
log_file.close()
exit()
