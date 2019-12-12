from socket import *
import sys

if len(sys.argv) < 3:
    print("python3 client.py hostname port")
    sys.exit(1)
# configure client socket
HOST = sys.argv[1]
PORT = int(sys.argv[2])

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((HOST,PORT))

print("connected to server of address {}".format((HOST,PORT)))

while True:
    sent = clientSocket.send(b'A'*1024)

print("ending connection")
clientSocket.close()
sys.exit(0)


