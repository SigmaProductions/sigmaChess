from main import *
from pieces import *


board= chessBoard()

board.boardArray[4][4]= piecePawn(4,4,factionColor.FACTION_WHITE)
board.boardArray[3][5]= piecePawn(4,4,factionColor.FACTION_BLACK)
pieceWhite= board.getPiece(4,4)
pieceBlack= board.getPiece(3,5)

board.PRINTBOARD()
print("\n\n\n-------------------------------------------------")

pieceWhite= board.getPiece(4,4)
pieceBlack= board.getPiece(3,5)

wasSuccessful=board.movePiece(pieceWhite,3,5)

board.PRINTBOARD()
print("\nWas successful: "+wasSuccessful.__str__())