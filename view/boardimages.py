from tkinter import PhotoImage
from tkinter import Canvas
import os.path



class BoardGraphicsDict:
    Images=dict()
    Path= None

    def __init__(self):
        self.Path= os.path.dirname(os.path.abspath(__file__))
        return

    def loadImages(self):
        """loads images into dict"""
        pawnImage= PhotoImage(file = self.Path+ "\graphics\pieces\pawn.gif")
        pawnBlackImage = PhotoImage(file=self.Path + "\graphics\pieces\pawnBlack.gif")
        tileImage = PhotoImage(file = self.Path+"\graphics\\tiles\placeholder.gif")

        self.Images.update({"tile":tileImage})
        self.Images.update({"pawn":pawnImage})
        self.Images.update({"pawnBlack": pawnBlackImage})

    def __getitem__(self, pieceName):
        return self.Images[pieceName]

