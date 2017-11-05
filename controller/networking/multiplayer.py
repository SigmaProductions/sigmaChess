import socket
import threading
from controller.networking.move import movePacket
import pickle
class ConnectionHandler:

    def __init__(self):
        self.port= 9332
        self.address= "192.168.88.17"


        self.receiver = socket.socket(family=socket.AF_INET)
        self.transmitter= socket.socket(family=socket.AF_INET)

        self.receiver.bind(('',self.port))
        self.receiver.listen()

        self.receiverThread= threading.Thread(target=self.__Await)
        self.receiverThread.start()



    def __Await(self):
        connection, address = self.receiver.accept()
        moveSerial= connection.recv(1024)

        move= pickle.loads(moveSerial)
        print(move)

    def __SendData(self,data):
        self.transmitter.connect((self.address,self.port))
        self.transmitter.sendall(data)

    def SendMove(self, pieceToMove, targetCoords):
        packet= movePacket((pieceToMove.x,pieceToMove.y), targetCoords)
        packetSerial= pickle.dumps(packet)

        self.transmitterThread = threading.Thread(target=self.__SendData, args=[packetSerial])
        self.transmitterThread.start()

