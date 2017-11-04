class EventHandler:

    def __init__(self,hboardClient, hviewClient):
        self.boardClient= hboardClient
        self.viewClient= hviewClient

        self.pieceSuspended=None
        self.isSuspended=False

    def __translateCoordsToTiles(self, coordX, coordY):
        """when clicked on window event gives values in pixels, in order to perform moves
           we must first convert them to coords on chess board"""
        translatedX = int((coordX) / 64)
        translatedY = int((64 * 8 - (coordY)) / 64)

        return (translatedX, translatedY)

    def boardClicked(self, event):
        """handle click event; move piece"""

        # translate coords so that we can index module
        chessCoords = self.__translateCoordsToTiles(event.x, event.y)

        """"if(self.isSuspended==False):
            pieceSuspended = self.boardClient.getPiece(chessCoords[0], chessCoords[1])
            if(pieceSuspended!=None):
                self.isSuspended = True

        elif(self.isSuspended==True):
            self.boardClient.movePiece(self.pieceSuspended,chessCoords[0],chessCoords[1])
            self.viewClient.drawBoard(self.boardClient)"""""
        if(self.pieceSuspended!=None):
            self.boardClient.movePiece(self.pieceSuspended, chessCoords[0], chessCoords[1])
        self.pieceSuspended = self.boardClient.getPiece(chessCoords[0], chessCoords[1])
        self.viewClient.drawBoard(self.boardClient)










