from UserInterface.boardView import BoardView
import tkinter as tk
from UserInterface.networkView import NetworkView
from UserInterface.chatView import ChatView


class AppWindow(tk.Frame):
    def __init__(self, master, physicsClient, chessBoard):
        super().__init__(master)
        self.chessBoard=chessBoard

        self.uiFrame = tk.Frame(master)
        self.physicsClient = physicsClient
        self.viewBoardClient = BoardView(self)

        self.viewNetworkClient = NetworkView(self.uiFrame)
        self.viewChatClient = ChatView(self.uiFrame)
        self.viewNetworkClient.pack(side=tk.TOP)
        self.viewChatClient.pack(side=tk.TOP)

        self.viewBoardClient.pack(side=tk.LEFT)
        self.viewNetworkClient.pack(side=tk.TOP)
        self.uiFrame.pack(side=tk.LEFT)
        self.viewBoardClient.drawBoard(self.physicsClient, self.chessBoard)

    def Step(self):
        self.viewBoardClient.drawBoard(self.physicsClient, self.chessBoard)
        self.master.update_idletasks()
        self.master.update()