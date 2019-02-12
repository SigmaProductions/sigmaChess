from tkinter import *
from view.boardwindow import BoardWindow
from view.networkwindow import NetworkWindow
from view.chatwindow import ChatWindow


class AppWindow(Frame):
    def __init__(self, master, boardClient):
        super().__init__(master)

        self.uiFrame = Frame(master)
        self.chessBoard = boardClient
        self.viewBoardClient = BoardWindow(self)

        self.viewNetworkClient = NetworkWindow(self.uiFrame)
        self.viewChatClient = ChatWindow(self.uiFrame)

        self.viewNetworkClient.pack(side=TOP)
        self.viewChatClient.pack(side=TOP)
        self.uiFrame.pack(side=LEFT)
        self.viewBoardClient.pack(side=LEFT)
        self.viewBoardClient.drawBoard(self.chessBoard)
