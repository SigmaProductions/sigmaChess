class EventHandler:

    def __init__(self,hboardClient, hviewClient):
        self.boardClient= hboardClient
        self.viewClient= hviewClient

        #piece we are currently moving
        self.pieceSuspended=None

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

        if(self.pieceSuspended!=None):
            if(self.boardClient.movePiece(self.pieceSuspended, chessCoords[0], chessCoords[1])):
                self.pieceSuspended = None
                self.viewClient.drawBoard(self.boardClient)
                return

        self.pieceSuspended = self.boardClient.getPiece(chessCoords[0], chessCoords[1])

    def networkMove(self,movePacket):
        pieceToMove=self.boardClient.getPiece(movePacket.fromCoords[0],movePacket.fromCoords[1])
        if not self.boardClient.movePiece(pieceToMove,movePacket.toCoords[0],movePacket.toCoords[1]):
            raise(BaseException("illegal move"))








