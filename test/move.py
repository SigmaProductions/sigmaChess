from board import *

##test if piecePawn can move one square
##TODO add test for both factions

board= chessBoard()
piece= board.getPiece(0,1)
board.movePiece(piece,0,2)

board.PRINTBOARD()
