from board import chessBoard
from view.boardwindow import BoardWindow

from tkinter import *

class SigmaChess:
    def __init__(self):
        root = Tk()

        self.boardClient = chessBoard()
        self.viewClient = BoardWindow(root)

        self.viewClient.addBinding("<Button-1>",self.boardClicked)
        self.viewClient.drawBoard(self.boardClient)

        self.viewClient.mainloop()

    def boardClicked(self,event):
        """handle click event; move piece"""

        #translate coords so that we can index module
        chessCoords=self.__translateCoordsToTiles(event.x, event.y)

        pieceToMove=self.boardClient.getPiece(chessCoords[0], chessCoords[1])
        self.boardClient.movePiece(pieceToMove,chessCoords[0],chessCoords[1]+1)
        self.viewClient.drawBoard(self.boardClient)


    def __translateCoordsToTiles(self, coordX, coordY):
        translatedX=int((coordX) /64)
        translatedY=int((64*8-(coordY) )/64)

        return(translatedX, translatedY)




############################################################################
###############################DEBUG########################################

if __name__ == "__main__":
    x= SigmaChess()

############################################################################
############################################################################