from tkinter import *
from view.boardimages import *
import pieces
import physics

class BoardWindow(Frame):

    def __init__(self,master):
        super().__init__(master)
        #load pieces images from graphics/pieces/ folder
        self.piecesImages = BoardGraphicsDict()
        self.piecesImages.loadImages()

        #create boardCanvas on which tiles and pieces will be drawn
        self.piecesCanvas = Canvas(self, width=64 * 8,
                              height=64 * 8)
        self.piecesCanvas.pack()

    def drawBoard(self, chessBoard):
        """this method wipes canvas in the frame and draws it anew"""
        self.piecesCanvas.delete("all")

        for i in range(8):
            for j in range(8):
                self.piecesCanvas.create_image(self.__translateBoardCoords(i, j, None), image=self.piecesImages["tile"])
                

        for i in range(8):
            for j in range(8):
                tilePiece= chessBoard.getPiece(i,j)

                if(tilePiece is not None):
                    if(tilePiece.faction== pieces.factionColor.FACTION_WHITE):
                        self.piecesCanvas.create_image(self.__translateBoardCoords(i,j, chessBoard.whoMoved), image=self.piecesImages[tilePiece.name])
                    elif(tilePiece.faction== pieces.factionColor.FACTION_BLACK):
                        self.piecesCanvas.create_image(self.__translateBoardCoords(i,j, chessBoard.whoMoved),image=self.piecesImages[tilePiece.name + "Black"])




    def addBinding(self, eventName, function):
        self.piecesCanvas.bind(eventName, function)


    def __translateBoardCoords(self,boardPositionX, boardPositionY, whoMoved):
        """translates integer position on the chess board to pixel position in canvas"""
        figure=physics.PhysicsSingleton.figures[boardPositionX][boardPositionY]
        if(whoMoved is None):
            x=boardPositionX
            y=boardPositionY
        else:
            x=figure.position[0]
            y=figure.position[1]
        if whoMoved == pieces.factionColor.FACTION_WHITE:
            x = 7 - x
            y = 7 - y 
        return (x*64 + 32,(64*8)- (
            y*64)-32)





############################################################################
###############################DEBUG########################################

if __name__ == "__main__":
    from board import chessBoard

    x=chessBoard()
    root= Tk()
    app = BoardWindow(root)
    app.drawBoard(x)

    input("w")
    p=x.getPiece(0,1)
    x.movePiece(p,0,2)
    app.drawBoard(x)
    root.mainloop()

############################################################################
############################################################################