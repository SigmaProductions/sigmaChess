from board import *

##test if pieceKing can attack
##TODO add test for both factions


board= chessBoard()

board.boardArray[6][6]= pieceKing(6,6,factionColor.FACTION_WHITE)
board.boardArray[5][7]= piecePawn(5,7,factionColor.FACTION_BLACK)
pieceWhite= board.getPiece(6,6)
pieceBlack= board.getPiece(5,7)

board.PRINTBOARD()
print("\n")

wasSuccessful=board.movePiece(pieceWhite,5,7)
board.movePiece(pieceWhite,5,7)

board.PRINTBOARD()


print("\nWas successful: "+wasSuccessful.__str__())