from tkinter import PhotoImage
from tkinter import Canvas
from PIL import Image
from PIL import ImageTk
import os.path


class BoardGraphicsDict:
    Images=dict()
    Path= None

    def __init__(self):
        self.Path= os.path.dirname(os.path.abspath(__file__))
        dummy = Image.open(self.Path + "/graphics/tiles/highlight.gif").convert('RGBA')
        self.highlightTk = ImageTk.PhotoImage(image=dummy)
        return

    def loadImages(self):
        """loads images into dict"""
        tileImage = PhotoImage(file=self.Path+"/graphics/tiles/chessboard.png")
        pawnImage = Image.open(self.Path + "/graphics/pieces/pawn.gif").convert('RGBA')
        pawnBlackImage = Image.open(self.Path + "/graphics/pieces/pawnBlack.gif").convert('RGBA')
        rook = Image.open(self.Path + "/graphics/pieces/rook.gif").convert('RGBA')
        rookBlack = Image.open(self.Path + "/graphics/pieces/rookBlack.gif").convert('RGBA')
        bishop = Image.open(self.Path + "/graphics/pieces/bishop.gif").convert('RGBA')
        bishopBlack = Image.open(self.Path + "/graphics/pieces/bishopBlack.gif").convert('RGBA')
        king = Image.open(self.Path + "/graphics/pieces/king.gif").convert('RGBA')
        kingBlack = Image.open(self.Path + "/graphics/pieces/kingBlack.gif").convert('RGBA')
        queen = Image.open(self.Path + "/graphics/pieces/queen.gif").convert('RGBA')
        queenBlack = Image.open(self.Path + "/graphics/pieces/queenBlack.gif").convert('RGBA')
        knight = Image.open(self.Path + "/graphics/pieces/knight.gif").convert('RGBA')
        knightBlack = Image.open(self.Path + "/graphics/pieces/knightBlack.gif").convert('RGBA')
        highlight = Image.open(self.Path + "/graphics/tiles/highlight.gif").convert('RGBA')
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
        self.Images.update({"highlight":highlight})

    def __getitem__(self, pieceName):
        return self.Images[pieceName]

