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

    def __del__(self):
        self.transmitter.close()
        self.receiver.close()

    def SendMove(self, pieceToMove, targetCoords):
        packet= movePacket((pieceToMove.x,pieceToMove.y), targetCoords)
        packetSerial= pickle.dumps(packet)

        self.transmitterThread = threading.Thread(target=self.__SendData, args=[packetSerial])
        self.transmitterThread.start()

    def goOnline(self,moveCallback):
        self.online = True

        self.receiver.bind(('', self.port))
        self.receiver.listen()
        self.transmitter.connect((self.address, self.port))

        self.receiverThread = threading.Thread(target=self.__Await, args= [moveCallback])
        self.receiverThread.start()


    def __Await(self, moveCallback):
        connection=None

        #TODO remove clusterfuck
        #while self.online is True try to connect and receive
        while(self.online):
            while(connection==None and self.online):
                #try to connect until successful
                connection, address=self.receiver.accept()
            while(self.online):
                moveSerial = connection.recv(1024)
                if( not moveSerial):
                    continue
                move = pickle.loads(moveSerial)
                moveCallback(move)

    def __SendData(self,data):

        print(pickle.dumps(data))
        self.transmitter.sendall(data)



