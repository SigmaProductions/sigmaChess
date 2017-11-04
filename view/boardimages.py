from tkinter import PhotoImage
from tkinter import Canvas




class BoardGraphicsDict:
    Images=dict()

    def __init__(self):
        return

    def loadImages(self):
        """loads images into dict"""
        pawnImage= PhotoImage(file = "graphics/pieces/pawn.gif")
        tileImage = PhotoImage(file = "graphics/tiles/placeholder.gif")

        self.Images.update({"tile":tileImage})
        self.Images.update({"pawn":pawnImage})

    def __getitem__(self, pieceName):
        return self.Images[pieceName]

