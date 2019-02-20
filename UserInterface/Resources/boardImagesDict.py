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
        tileImage = PhotoImage(file = self.Path+"\graphics\\tiles\chessboard.png")
        rook = PhotoImage(file = self.Path+"\graphics\\pieces\\rook.gif")
        rookBlack= PhotoImage(file=self.Path + "\graphics\\pieces\\rookBlack.gif")
        bishop= PhotoImage(file=self.Path + "\graphics\\pieces\\bishop.gif")
        bishopBlack= PhotoImage(file=self.Path + "\graphics\\pieces\\bishopBlack.gif")
        king= PhotoImage(file=self.Path + "\graphics\\pieces\\king.gif")
        kingBlack= PhotoImage(file=self.Path + "\graphics\\pieces\\kingBlack.gif")
        queen= PhotoImage(file=self.Path + "\graphics\\pieces\\queen.gif")
        queenBlack= PhotoImage(file=self.Path + "\graphics\\pieces\\queenBlack.gif")
        knight= PhotoImage(file=self.Path + "\graphics\\pieces\\knight.gif")
        knightBlack= PhotoImage(file=self.Path + "\graphics\\pieces\\knightBlack.gif")

        self.Images.update({"tile":tileImage})
        self.Images.update({"pawn":pawnImage})
        self.Images.update({"pawnBlack": pawnBlackImage})
        self.Images.update({"rook":rook})
        self.Images.update({"rookBlack":rookBlack})
        self.Images.update({"bishop":bishop})
        self.Images.update({"bishopBlack":bishopBlack})
        self.Images.update({"kingBlack":kingBlack})
        self.Images.update({"king":king})
        self.Images.update({"queen":queen})
        self.Images.update({"queenBlack":queenBlack})
        self.Images.update({"knight":knight})
        self.Images.update({"knightBlack":knightBlack})

    def __getitem__(self, pieceName):
        return self.Images[pieceName]

