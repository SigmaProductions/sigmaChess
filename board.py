from pieces import *

class chessBoard:
    boardArray = [[]]

    def __init__(self):
        self.boardArray = self.__spawnPieces()

    def __createEmptyArray(self):
        hArray = []
        for i in range(8):
            hArray.append([])
            for k in range(8):
                hArray[i].append(None)
        return hArray

    def __spawnPieces(self):
        boardArray = self.__createEmptyArray()
        for k in range(8):
            boardArray[k][1] = piecePawn(k, 1, factionColor.FACTION_WHITE)
            boardArray[k][6] = piecePawn(k, 6, factionColor.FACTION_BLACK)

        boardArray[0][0] = pieceRook(0 ,0, factionColor.FACTION_WHITE)
        boardArray[1][0] = pieceKnight(1, 0, factionColor.FACTION_WHITE)
        boardArray[2][0] = pieceBishop(2, 0, factionColor.FACTION_WHITE)
        boardArray[3][0] = pieceQueen(3, 0, factionColor.FACTION_WHITE)
        boardArray[4][0] = pieceKing(4, 0, factionColor.FACTION_WHITE)
        boardArray[5][0] = pieceBishop(5, 0, factionColor.FACTION_WHITE)
        boardArray[6][0] = pieceKnight(6, 0, factionColor.FACTION_WHITE)
        boardArray[7][0] = pieceRook(7, 0, factionColor.FACTION_WHITE)

        boardArray[0][7] = pieceRook(0, 7, factionColor.FACTION_BLACK)
        boardArray[1][7] = pieceKnight(1, 7, factionColor.FACTION_BLACK)
        boardArray[2][7] = pieceBishop(2, 7, factionColor.FACTION_BLACK)
        boardArray[3][7] = pieceQueen(3, 7, factionColor.FACTION_BLACK)
        boardArray[4][7] = pieceKing(4, 7, factionColor.FACTION_BLACK)
        boardArray[5][7] = pieceBishop(5, 7, factionColor.FACTION_BLACK)
        boardArray[6][7] = pieceKnight(6, 7, factionColor.FACTION_BLACK)
        boardArray[7][7] = pieceRook(7, 7, factionColor.FACTION_BLACK)
        return boardArray

    def movePiece(self, pieceToMove, xNew, yNew):
        """this method  performs both attack and move"""
        ##check if it can move
        isAttack = pieceToMove.checkAttack(self.boardArray,coordHorizontal=xNew, coordVert=yNew)
        if isAttack == True:
            self.__move(pieceToMove, xNew, yNew)
            return True

        ##check if it can attack
        isLegal = pieceToMove.checkMove(self.boardArray,coordHorizontal=xNew, coordVert=yNew)
        if isLegal == True:
            self.__move(pieceToMove, xNew, yNew)
            return True

        #cant do neither
        return False


    def __move(self,pieceToMove, xNew, yNew):
        xCurrent = pieceToMove.x
        yCurrent = pieceToMove.y

        #change coords inside piece object
        pieceToMove.x=xNew
        pieceToMove.y=yNew

        self.boardArray[xNew][yNew] = pieceToMove
        self.boardArray[xCurrent][yCurrent] = None


    def getPiece(self,coordHorizontal, coordVert):
        return self.boardArray[coordHorizontal][coordVert]

    def PRINTBOARD(self):
        for i in range(8):
            print("")
            for j in range(8):
                if type(self.boardArray[j][7 - i]) is piecePawn:
                    print("P", end="")
                elif type(self.boardArray[j][7-i]) is pieceKing:
                    print("K", end="")
                elif type(self.boardArray[j][7-i]) is pieceBishop:
                    print("B", end="")
                elif type(self.boardArray[j][7-i]) is pieceKnight:
                    print("N", end="")
                elif type(self.boardArray[j][7-i]) is pieceRook:
                    print("R", end="")
                elif type(self.boardArray[j][7-i]) is pieceQueen:
                    print("Q",end="")
                else:
                    print("-", end="")

    def isVictory(self):
        whiteExist = False
        blackExist = False
        for i in range(8):
            for j in range(8):
                if self.boardArray[j][i] == None:
                    continue
                if self.boardArray[j][i].faction == factionColor.FACTION_WHITE:
                    whiteExist = True
                if self.boardArray[j][i].faction == factionColor.FACTION_BLACK:
                    blackExist = True
        if blackExist != True:
            print("White victory!")
        if whiteExist != True:
            print("Black victory!")