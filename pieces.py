from enum import Enum

class factionColor (Enum):
    FACTION_WHITE = 1;
    FACTION_BLACK = 2;

class chessPiece:

    def __init__(self, hX, hY, faction):
        self.x = hX;
        self.y = hY;
        self.faction=faction;

class piecePawn(chessPiece):

    def checkAttack(self, boardArray, coordHorizontal, coordVert):
        square = boardArray[coordHorizontal][coordVert];
        if square is None:
            return False;
        if self.faction == factionColor.FACTION_WHITE:
            if coordVert == self.y + 1 and (abs(coordHorizontal - self.x == 1)):
                if square.faction is not self.faction:
                    return True;
                return False;
        else:
            if coordVert == self.y - 1 and (abs(coordHorizontal - self.x == 1)):
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





