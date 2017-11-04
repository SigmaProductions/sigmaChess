from enum import Enum

class factionColor (Enum):
    FACTION_WHITE = 1;
    FACTION_BLACK = 2;

class chessPiece:

    def __init__(self, hX, hY, faction):
        self.x = hX;
        self.y = hY;
        self.faction=faction;

    def checkPath(self, boardArray, coordHorizontal, coordVert):
        a = int((coordHorizontal - self.x)/(coordVert - self.y))
        b = int(self.y - (self.x*a))
        if self.x >= coordHorizontal:
            high = self.x
            low = coordHorizontal
        else:
            high = coordHorizontal
            low = self.x

        for squarex in range(low+1, high):
            squarey = squarex*a + b
            if boardArray[squarex][squarey] is not None:
                return False
        return True
    def isInRange(self, coordHorizontal, coordVert):
        if coordVert < 8 and coordVert > -1:
            if coordHorizontal < 8 and coordHorizontal > -1:
                return True;
        return False;

class piecePawn(chessPiece):

    def checkAttack(self, boardArray, coordHorizontal, coordVert):
        square = boardArray[coordHorizontal][coordVert];
        if square is None:
            return False;
        if self.faction == factionColor.FACTION_WHITE:
            if coordVert == self.y + 1 and (abs(coordHorizontal - self.x) == 1):
                if square.faction is not self.faction:
                    return True;
                return False;
        elif self.faction == factionColor.FACTION_BLACK:
            if coordVert + 1 == self.y  and (abs(coordHorizontal - self.x) == 1):
                if square.faction is not self.faction:
                    return True;
            return False;

    def checkMove(self, boardArray, coordHorizontal, coordVert):
        square = boardArray[coordHorizontal][coordVert];
        if square is not None:
            return False;
        if self.faction == factionColor.FACTION_WHITE:
            if coordHorizontal == self.x and self.y == 1 and coordVert == self.y + 2:
                return True;
            elif coordHorizontal == self.x and coordVert == self.y + 1:
                return True;
            return False;
        else:
            if coordHorizontal == self.x and self.y == 6 and coordVert == self.y - 2:
                return True;
            if coordHorizontal == self.x and coordVert == self.y - 1:
                return True;
            return False;

class pieceKing(chessPiece):

    def checkAttack(self, boardArray, coordHorizontal, coordVert):
        square=boardArray[coordHorizontal][coordVert];
        if (abs(coordHorizontal - self.x) <= 1) and (abs(coordVert - self.y) <= 1):
            if square is not None and square.faction is not self.faction:
                return True;
        return False;

    def checkMove(self, boardArray, coordHorizontal, coordVert):
        square=boardArray[coordHorizontal][coordVert];
        if square is not None:
            return False;
        if (abs(coordHorizontal - self.x) <= 1) and (abs(coordVert - self.y) <= 1):
            return True;
        return False;

class pieceRook(chessPiece):

    def checkAttack(self, boardArray, coordHorizontal, coordVert):
        return self.checkMove(boardArray, coordHorizontal, coordVert)

    def checkMove(self, boardArray, coordHorizontal, coordVert):
        square = boardArray[coordHorizontal][coordVert]
        if coordHorizontal in range(8) and coordVert == self.y and square.faction is not self.faction or coordVert in range(8) and coordHorizontal == self.x and square.faction is not self.faction:
            if square is None:
                return True
            if square.faction is not self.faction:
                return True
        return False

class pieceBishop(chessPiece):

    def checkAttack(self, boardArray, coordHorizontal, coordVert):
        return self.checkMove(boardArray, coordHorizontal, coordVert)

    def checkMove(self, boardArray, coordHorizontal, coordVert):
        square = boardArray[coordHorizontal][coordVert]
        emptyPath = self.checkPath(boardArray, coordHorizontal, coordVert)
        if abs(coordHorizontal - self.x) == abs(coordVert - self.y) and coordHorizontal in range(8) and coordVert in range(8) and emptyPath is not False:
            if square is None:
                return True
            if square.faction is not self.faction:
                return True
        return False

class pieceKnight(chessPiece):

    def checkAttack(self, boardArray, coordHorizontal, coordVert):
        return self.checkMove(boardArray, coordHorizontal, coordVert)

    def checkMove(self, boardArray, coordHorizontal, coordVert):
        square = boardArray[coordHorizontal][coordVert]
        if abs(coordHorizontal - self.x) == 2 and abs(coordVert - self.y) == 1 or abs(coordVert - self.y) == 2 and abs(coordHorizontal - self.x) == 1:
            if square is None:
                return True
            if square.faction is not self.faction:
                return True
        return False








