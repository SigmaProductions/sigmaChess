import socket
import threading
from controller.networking.move import movePacket
import pickle
class ConnectionHandler:

    def __init__(self):
        self.online=False
        self.port= 9332
        self.address= ""
        self.receiver = socket.socket(family=socket.AF_INET)
        self.transmitter= socket.socket(family=socket.AF_INET)

    def __del__(self):
        self.goOffline()

    def SendMove(self, pieceToMove, targetCoords):
        if not self.online:
            return False
        print("moved")
        packet= movePacket((pieceToMove.x,pieceToMove.y), targetCoords)
        packetSerial= pickle.dumps(packet)

        self.transmitterThread = threading.Thread(target=self.__SendData, args=[packetSerial])
        self.transmitterThread.start()

    def goOnline(self,moveCallback, address):
        """try to connect and vind callback to network move packet"""

        #listen on every ip address
        self.receiver.bind(('', self.port))
        self.receiver.listen()
        #target address given in param
        self.address = address

        #try to connect if cant run chess in offline mode
        #TODO move it it doesnt work now; waiting for UI implementation
        self.transmitter.connect((self.address, self.port))

        #transmitter has connected so we can consider outselves online
        self.online = True

        #start listening on separate thread
        self.receiverThread = threading.Thread(target=self.__Await, args= [moveCallback])
        self.receiverThread.start()

    def goOffline(self):
        self.online=False

        self.transmitter.close()
        self.receiver.close()

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
        try:
            print("data sent")
            self.transmitter.sendall(data)
        except(TimeoutError):
            self.goOffline()






