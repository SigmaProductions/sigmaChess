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
        for i in range(2):
            for k in range(8):
                boardArray[k][i] = piecePawn(k, i, factionColor.FACTION_WHITE)
        for i in range(8, 6):
            for k in range(8):
                boardArray[k][i] = piecePawn(k, i, factionColor.FACTION_BLACK)
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
                else:
                    print("-", end="")
    def TESTBOARD1(self):
        testBoard = self.__createEmptyArray()
        testBoard[4][4] = piecePawn(4, 4, factionColor.FACTION_BLACK)
        self.boardArray = testBoard

    def TESTBOARD2(self):
        testBoard = self.__createEmptyArray()
        testBoard[4][4] = piecePawn(4, 4, factionColor.FACTION_WHITE)
        self.boardArray = testBoard

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

