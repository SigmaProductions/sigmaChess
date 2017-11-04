from board import *
from pieces import *


board= chessBoard()

board.boardArray[2][2]= piecePawn(2,2,factionColor.FACTION_WHITE)
board.boardArray[3][3]= piecePawn(3,3,factionColor.FACTION_BLACK)
pieceWhite= board.getPiece(2,2)
pieceBlack= board.getPiece(3,3)

board.PRINTBOARD()
print("\n\n\n-------------------------------------------------")

pieceWhite= board.getPiece(2,2)
pieceBlack= board.getPiece(3,3)

wasSuccessful=board.movePiece(pieceWhite,3,3)

board.PRINTBOARD()
print("\nWas successful: "+wasSuccessful.__str__())