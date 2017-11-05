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
        boardtemplate = open(r"C:\Users\Przrg\Desktop\SIGMAchess\sigmaChess\boardtemplate.txt", "r" )
        for y in range(8):
            line = boardtemplate.readline()
            for x in range(8):
                whatPiece = line[x]
                if whatPiece == "O":
                    boardArray[x][y] = None
                elif whatPiece == "P":
                    if y <= 3:
                        boardArray[x][y] = piecePawn(x, y, factionColor.FACTION_WHITE)
                    else:
                        boardArray[x][y] = piecePawn(x, y, factionColor.FACTION_BLACK)
                elif whatPiece == "R":
                    if y <= 3:
                        boardArray[x][y] = pieceRook(x, y, factionColor.FACTION_WHITE)
                    else:
                        boardArray[x][y] = pieceRook(x, y, factionColor.FACTION_BLACK)
                elif whatPiece == "N":
                    if y <= 3:
                        boardArray[x][y] = pieceKnight(x, y, factionColor.FACTION_WHITE)
                    else:
                        boardArray[x][y] = pieceKnight(x, y, factionColor.FACTION_BLACK)
                elif whatPiece == "B":
                    if y <= 3:
                        boardArray[x][y] = pieceBishop(x, y, factionColor.FACTION_WHITE)
                    else:
                        boardArray[x][y] = pieceBishop(x, y, factionColor.FACTION_BLACK)
                elif whatPiece == "Q":
                    if y <= 3:
                        boardArray[x][y] = pieceQueen(x, y, factionColor.FACTION_WHITE)
                    else:
                        boardArray[x][y] = pieceQueen(x, y, factionColor.FACTION_BLACK)
                elif whatPiece == "K":
                    if y <= 3:
                        boardArray[x][y] = pieceKing(x, y, factionColor.FACTION_WHITE)
                    else:
                        boardArray[x][y] = pieceKing(x, y, factionColor.FACTION_BLACK)
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
        if type(self.boardArray[xNew][yNew] == piecePawn):
            self.pawnPromotion(xNew, yNew)

    def pawnPromotion(self, xNew, yNew):
        if yNew == 7:
            self.boardArray[xNew][yNew] = pieceQueen(xNew, yNew, factionColor.FACTION_WHITE)
        elif yNew == 0:
            self.boardArray[xNew][yNew] = pieceQueen(xNew, yNew, factionColor.FACTION_BLACK)

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


    def isWhiteChecked(self):
        for i in range(8):
            for j in range(8):
                if (type(self.boardArray[i][j]) == pieceKing) and (self.boardArray[i][j].faction == factionColor.FACTION_WHITE):
                    xKing=i;
                    yKing=j;
        for i in range(8):
            for j in range(8):
                if self.boardArray[i][j]==None:
                    continue
                if self.boardArray[i][j].faction == factionColor.FACTION_WHITE:
                    continue
                if self.boardArray[i][j].faction == factionColor.FACTION_BLACK:
                    piece=self.getPiece(i,j)
                    if self.movePiece(piece,xKing,yKing) == True:
                        return True
                    else:
                        continue
        return False;

    def isBlackChecked(self):
        for i in range(8):
            for j in range(8):
                if (type(self.boardArray[i][j]) == pieceKing) and (self.boardArray[i][j].faction == factionColor.FACTION_BLACK):
                    xKing=i;
                    yKing=j;
        for i in range(8):
            for j in range(8):
                if self.boardArray[i][j]==None:
                    continue
                if self.boardArray[i][j].faction == factionColor.FACTION_BLACK:
                    continue
                if self.boardArray[i][j].faction == factionColor.FACTION_WHITE:
                    piece=self.getPiece(i,j)
                    if self.movePiece(piece,xKing,yKing) == True:
                        return True
                    else:
                        continue
        return False;