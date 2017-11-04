from board import *

##test if piecePawn can move
##TODO add test for both factions

board= chessBoard()
piece= board.getPiece(7,1)
board.movePiece(piece,6,2)

board.PRINTBOARD()