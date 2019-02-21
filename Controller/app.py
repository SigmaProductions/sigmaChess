from ChessEngine.board import chessBoard
from UserInterface.appWindow import AppWindow
from Controller.events import EventHandler
from Networking.multiplayer import ConnectionHandler
from tkinter import *
from PhysicsEngine.physics import Physics
import winsound

class SigmaChessApp:
    def __init__(self):
        #winsound.PlaySound(Path + "\\music.wav", winsound.SND_ASYNC)
        #board client handles logic of chess board moves and attacks
        self.boardClient = chessBoard()

        #initialize physics engine
        self.physicsClient= Physics(self.boardClient)
        self.physicsClient.initFigures()
        self.boardClient.observer.Bind(self.physicsClient.MoveCallback)

        #view client handles drawing everything
        self.viewClient= AppWindow(Tk(),self.physicsClient,self.boardClient)
        self.viewClient.pack()

        # connection handler makes chess playable in multiplayer
        self.multiplayerClient = ConnectionHandler()

        #event handler handles event performed on windows
        self.eventsClient = EventHandler(self.boardClient, self.viewClient,self.multiplayerClient,self.physicsClient)

        self.mainLoop()

    def mainLoop(self):
        while(True):
            self.physicsClient.Step()
            self.viewClient.Step()
 
        



