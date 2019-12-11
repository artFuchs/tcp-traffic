
from socket import *
import sys
import os
import time


if (len(sys.argv) < 2):
    print("python3 server.py port")

# configure server socket
BUFFER_SIZE = 2048
MB = 2**20
HOST = 'localhost'
PORT = int(sys.argv[1])
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((HOST,PORT))

print("host = {}".format(HOST))
print("port = {}".format(PORT))

# listen to 1 connection
serverSocket.listen(1)

(client,address) = serverSocket.accept()
print("connected with {}".format(address))

# create log file
if (not os.path.isdir('./logs')):
    os.mkdir('./logs')
logFilename = "logs/tcp_server_{}.log".format(PORT)
logFile = open(logFilename,'w')
print("log file: {}".format(logFilename))

#prepare to receive
dataRcvd = 0
start = time.time()

# receive data until it stops comming
while True:
    data = client.recv(BUFFER_SIZE)
    dataRcvd += len(data)
    # if data is null close application 
    if (not data):
        break;
    # if one second passed, add received size to log
    stop = time.time()
    if stop - start >= 1:
        dataRcvd_mb = int(dataRcvd*8 / int((stop-start)*MB))
        timeStamp = time.strftime("%H:%M:%S",time.localtime(stop))
        logFile.write("[{}] {} Mbits/s \n".format(timeStamp,dataRcvd_mb))
        dataRcvd = 0
        start = time.time()

print("ending connection")
logFile.close()
client.close()
sys.exit(0)
