from tkinter import *
from view.boardwindow import BoardWindow
from view.networkwindow import NetworkWindow

class AppWindow(Frame):
    def __init__(self,master, boardClient):
        super().__init__(master)

        self.chessBoard= boardClient
        self.viewBoardClient = BoardWindow(self)
        self.viewNetworkClient = NetworkWindow(self)

        self.viewNetworkClient.pack(side=LEFT)
        self.viewBoardClient.pack(side=LEFT)
        self.viewBoardClient.drawBoard(self.chessBoard)

