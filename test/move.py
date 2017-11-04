from board import *

##test if piecePawn can move one square
##TODO add test for both factions

board= chessBoard()

board.PRINTBOARD()

print("\n")

piece= board.getPiece(1,1)
board.movePiece(piece,1,3)

board.PRINTBOARD()


print("\n")

piece= board.getPiece(2,6)
board.movePiece(piece,2,4)

board.PRINTBOARD()


print("\n")

piece= board.getPiece(2,4)
board.movePiece(piece,1,3)

board.PRINTBOARD()


