from board import chessBoard
from view.boardwindow import BoardWindow
from controller.events import EventHandler
from controller.networking.multiplayer import ConnectionHandler
from tkinter import *

class SigmaChess:
    def __init__(self):
        root = Tk()

        #board client handles logic of chess board moves and attacks
        self.boardClient = chessBoard()
        #view client handles drawing chessboard and pieces
        self.viewClient = BoardWindow(root)
        #event handler handles event performed on windows
        self.eventsClient = EventHandler(self.boardClient, self.viewClient)
        #connection handler makes chess playable in multiplayer
        self.multiplayerClient= ConnectionHandler()

        #this binds functions in event handler to actions performed on window
        self.bindEvents()

        self.multiplayerClient.goOnline(self.eventsClient.networkMove)

        #draw window and enter mainloop
        self.viewClient.drawBoard(self.boardClient)
        self.viewClient.mainloop()

    def bindEvents(self):
        """bind events to event handler; here go every event handle"""
        self.viewClient.addBinding("<Button-1>", self.eventsClient.boardClicked)





############################################################################
###############################DEBUG########################################

if __name__ == "__main__":
    x= SigmaChess()

############################################################################
############################################################################