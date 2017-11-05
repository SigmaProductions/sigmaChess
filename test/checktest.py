from board import *

board= chessBoard()
board.boardArray[5][4]= pieceKing(5,4,factionColor.FACTION_WHITE)
board.boardArray[3][3]= pieceKing(3,3,factionColor.FACTION_BLACK)
board.boardArray[1][4]= pieceKnight(1,4,factionColor.FACTION_WHITE)
board.boardArray[4][0]= None
board.boardArray[4][7]= None
pieceWhite= board.getPiece(5,4)
pieceBlack= board.getPiece(3,3)

board.PRINTBOARD()
print("\n")

wasSuccessful1=board.isWhiteChecked()
wasSuccessful2=board.isBlackChecked()
print("\nIs white checked: "+wasSuccessful1.__str__())
print("\nIs black checked: "+wasSuccessful2.__str__())