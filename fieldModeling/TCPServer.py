#This shouldn't be here
#Really
#For real
#Please put it somewhere else
#Pretty please
#Pretty pretty please

import socketserver as SocketServer
import socket


HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 13000        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            #if not data:
            #    break
            sendData = b"Vsauce Michael Here"
            conn.sendall(sendData)