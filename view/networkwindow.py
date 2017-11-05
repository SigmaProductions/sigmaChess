from tkinter import *

class NetworkWindow(Frame):
    """window responsible for entering ip address and event calling multiplayer to engage"""
    def __init__(self,master):
        super().__init__(master)
        #the callback used for connect button
        self.connectCallback=None

        self.addressLabel= Label(self,text="Adres IP:")
        self.addressLabel.pack()

        self.addressEntry = Entry(self)
        self.addressEntry.pack()

        self.connectButton= Button(self,text="connect", command=self.connectBtnClick)
        self.connectButton.pack()

    def connectBtnClick(self):
        self.connectCallback(self.addressEntry.get())

    def addConnectBtnBind(self,callback):
        self.connectCallback=callback