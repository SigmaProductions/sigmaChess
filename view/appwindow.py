from view.boardwindow import BoardWindow
import tkinter as tk
from view.networkwindow import NetworkWindow
from view.chatwindow import ChatWindow


class AppWindow(tk.Frame):
    def __init__(self, master, boardClient):
        super().__init__(master)

        self.uiFrame = tk.Frame(master)
        self.chessBoard = boardClient
        self.viewBoardClient = BoardWindow(self)

        self.viewNetworkClient = NetworkWindow(self.uiFrame)
        self.viewChatClient = ChatWindow(self.uiFrame)
        self.viewNetworkClient.pack(side=tk.TOP)
        self.viewChatClient.pack(side=tk.TOP)

        self.viewBoardClient.pack(side=tk.LEFT)
        self.viewNetworkClient.pack(side=tk.TOP)
        self.uiFrame.pack(side=tk.LEFT)
        self.viewBoardClient.drawBoard(self.chessBoard)
