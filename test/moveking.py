from board import *

##test if pieceKing can move
##TODO add test for both factions


board= chessBoard()

board.boardArray[2][2]= pieceKing(2,2,factionColor.FACTION_WHITE)
piece= board.getPiece(2,2)

board.PRINTBOARD()
print("\n")

board.movePiece(piece,1,1)

board.PRINTBOARD()

wasSuccessful=board.movePiece(piece,2,2)
print("\nWas successful: "+wasSuccessful.__str__())