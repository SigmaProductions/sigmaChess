from board import *

##test if piecePawn can move one square
##TODO add test for both factions

board= chessBoard()

board.PRINTBOARD()

piece= board.getPiece(6,1)
board.movePiece(piece,6,2)

board.PRINTBOARD()


