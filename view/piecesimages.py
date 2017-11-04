from tkinter import PhotoImage
from tkinter import Canvas


class PiecesGraphicsDict:
    Images=dict()

    def __init__(self):
        return

    def loadImages(self, folderPath):
        """loads images into dict"""
        pawnImage= PhotoImage(file= folderPath+"pawn.gif")
        #pawnImage.zoom(190,)

        self.Images.update({"pawn":pawnImage})

    def __getitem__(self, pieceName):
        return self.Images[pieceName]

    def getPieceCanvas(self,master, pieceName):
        pieceCanvas = Canvas(master, width=self.Images[pieceName].width(), height=self.Images[pieceName].height())
        return pieceCanvas
