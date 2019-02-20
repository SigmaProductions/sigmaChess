from tkinter import StringVar


class Chat:
    def __init__(self):
        self.content = StringVar()
        self.dummyStr = self.content.get()

    def addContent(self,msg):
        self.dummyStr += "Player: " + msg + '\n'
        self.content.set(self.dummyStr)
