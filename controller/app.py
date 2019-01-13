from board import chessBoard
from view.appwindow import AppWindow
from controller.events import EventHandler
from controller.networking.multiplayer import ConnectionHandler
from tkinter import *
import physics
class SigmaChess:
    def __init__(self):
        self.root = Tk()

        #board client handles logic of chess board moves and attacks
        self.boardClient = chessBoard()
        physics.PhysicsSingleton.BindToBoard(self.boardClient)
        #view client handles drawing everything
        self.viewClient= AppWindow(self.root,self.boardClient)
        self.viewClient.pack()

        # connection handler makes chess playable in multiplayer
        self.multiplayerClient = ConnectionHandler()
        #event handler handles event performed on windows
        self.eventsClient = EventHandler(self.boardClient, self.viewClient,self.multiplayerClient)


        #this binds functions in event handler to actions performed on window
        self.bindEvents()

        self.mainLoop()

    def mainLoop(self):
        while(True):
            physics.PhysicsSingleton.run()
            self.viewClient.viewBoardClient.drawBoard(self.boardClient)     
            self.root.update_idletasks()
            self.root.update()
 
        

    def bindEvents(self):
        """bind events to event handler; here go every event handle"""
        self.viewClient.viewBoardClient.addBinding("<Button-1>", self.eventsClient.boardClicked)
        self.viewClient.viewNetworkClient.addConnectBtnBind(self.eventsClient.networkConnect)





############################################################################
###############################DEBUG########################################

if __name__ == "__main__":
    x= SigmaChess()

############################################################################
############################################################################