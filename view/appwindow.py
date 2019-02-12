from view.boardwindow import BoardWindow
import tkinter as tk
from view.networkwindow import NetworkWindow

class AppWindow(tk.Frame):
    def __init__(self,master, boardClient):
        super().__init__(master)

        self.chessBoard= boardClient
        self.viewBoardClient = BoardWindow(self)
        self.viewNetworkClient = NetworkWindow(self)

        self.viewNetworkClient.pack(side=tk.LEFT)
        self.viewBoardClient.pack(side=tk.LEFT)
        self.viewBoardClient.drawBoard(self.chessBoard)

