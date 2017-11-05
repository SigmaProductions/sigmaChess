import socket
import threading

class ConnectionHandler:

    def __init__(self):
        self.port= 9332
        self.address= "192.168.88.13"

        self.receiver= socket.socket(family=socket.AF_INET)
        self.receiver.bind((self.address,self.port))
        self.receiver.listen()

        self.receiverThread= threading.Thread(target=self.Echo)
        self.receiverThread.start()

    def Echo(self):
        connection, address = self.receiver.accept()

        data= connection.recv(1024)
        print(data)
        connection.sendall(data)