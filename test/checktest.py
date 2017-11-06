from board import *

class SigmaChess():

    board= chessBoard()
    board.boardArray[4][0]= None
    board.boardArray[4][7]= None
    board.boardArray[5][4]= pieceKing(5,4,factionColor.FACTION_WHITE)
    board.boardArray[3][2]= pieceKing(3,2,factionColor.FACTION_BLACK)

    board.PRINTBOARD()
    print("\n")

    print("Biała szachowa: ",board.isChecked(factionColor.FACTION_WHITE))
    print("Czarna szachowa: ", board.isChecked(factionColor.FACTION_BLACK))
    print("Bialy krol: ",board.getKing(factionColor.FACTION_WHITE))
    print("Gorszy krol: ",board.getKing(factionColor.FACTION_BLACK))