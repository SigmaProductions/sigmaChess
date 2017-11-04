from tkinter import *
from view.piecesimages import *



class BoardWindow(Frame):

    def __init__(self,master):
        super().__init__(master)
        self.piecesOnCanvas=[]
        #load pieces images from graphics/pieces/ folder
        self.piecesImages = PiecesGraphicsDict()
        self.piecesImages.loadImages("graphics/pieces/")



    def drawBoard(self, chessBoard):
        piecesCanvas = Canvas(self.master, width=self.piecesImages["pawn"].width() * 8,
                              height=self.piecesImages["pawn"].height() * 8)
        piecesCanvas.pack()

        for i in range(8):
            for j in range(8):

                if(chessBoard.getPiece(i,j)== None):
                    continue
                piece=piecesCanvas.create_image(self.__translateBoardCoords(i,j), image=self.piecesImages["pawn"])
                self.piecesOnCanvas.append(piece)




    def __translateBoardCoords(self,boardPositionX, boardPositionY):
        return (boardPositionX*64 + 32,(64*8)- (boardPositionY*64)-32)





############################################################################
###############################DEBUG########################################

if __name__ == "__main__":
    from board import chessBoard

    x=chessBoard()
    root= Tk()
    app = BoardWindow(root)
    app.drawBoard(x)
    root.mainloop()

############################################################################
############################################################################