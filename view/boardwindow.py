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
        # TODO rewrite it to make it more efficient possibly moving every piece's graphic to canvas widget

        self.piecesCanvas.delete("all")

        for i in range(8):
            for j in range(8):
                iRender = i
                jRender = j
                if chessBoard.whoMoved == pieces.factionColor.FACTION_WHITE:
                    iRender = 7 - i
                    jRender = 7 - j
                tilePiece= chessBoard.getPiece(i,j)

                if(tilePiece== None):
                    self.piecesCanvas.create_image(self.__translateBoardCoords(iRender, jRender), image=self.piecesImages["tile"])
                    continue
                else:
                    if(tilePiece.faction== pieces.factionColor.FACTION_WHITE):
                        self.piecesCanvas.create_image(self.__translateBoardCoords(iRender, jRender), image=self.piecesImages[tilePiece.name])
                    elif(tilePiece.faction== pieces.factionColor.FACTION_BLACK):
                        self.piecesCanvas.create_image(self.__translateBoardCoords(iRender, jRender),image=self.piecesImages[tilePiece.name + "Black"])




    def addBinding(self, eventName, function):
        self.piecesCanvas.bind(eventName, function)


    def __translateBoardCoords(self,boardPositionX, boardPositionY):
        """translates integer position on the chess board to pixel position in canvas"""
        figure=physics.PhysicsSingleton.figures[boardPositionX][boardPositionY]
        if(figure is None):
            x=1
            y=1
        else:
            x=figure.position[0]/64*8

            y=figure.position[1]/64*8
        return (x*boardPositionX*64 + 32,(64*8)- (
            y*boardPositionY*64)-32)





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