from tkinter import *


class ChatWindow(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.sendCallback=None

        self.sendButton= Button(self,text="Send", command=self.sendBtnClick)
        self.sendButton.pack(side=BOTTOM)

        self.textEntry = Entry(self)
        self.textEntry.pack(side=BOTTOM)

        self.messageWindowScroll = Scrollbar(self)
        self.messageWindowScroll.pack(side=RIGHT,fill="y")

        self.messageWindow = Text(self,bd=5,relief=RIDGE,bg="gray90",state=DISABLED,width=20,font=("Comic Sans MS","10"),yscrollcommand=self.messageWindowScroll.set)
        self.messageWindow.pack(side=TOP,fill="both")
        self.messageWindowScroll.config(command=self.messageWindow.yview)

    def sendBtnClick(self):
        self.messageWindow["state"] = NORMAL
        self.messageWindow.insert(END,"You: " + self.textEntry.get() + '\n')
        self.messageWindow["state"] = DISABLED

    def addSendBtnBind(self,callback):
        self.sendCallback=callback