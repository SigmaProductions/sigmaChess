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
        if self.faction == factionColor.FACTION_WHITE:
            if coordVert == self.y + 1 and (abs(coordHorizontal - self.x == 1)):
                if square is not None and square.faction is not self.faction:
                    return True;
            return False;
        else:
            if coordVert == self.y - 1 and (abs(coordHorizontal - self.x == 1)):
                if square is not None and square.faction is not self.faction:
                    return True;
            return False;

    def checkMove(self, boardArray, coordHorizontal, coordVert):
        square = boardArray[coordHorizontal][coordVert];
        if self.faction == factionColor.FACTION_WHITE:
            if coordHorizontal == self.x and self.y == 2 and coordVert == self.y + 2:
                if square == None:
                    return True;
            elif coordHorizontal == self.x and coordVert == self.y + 1:
                if square == None:
                    return True;
            return False;
        else:
            if coordHorizontal == self.x and self.y == 6 and coordVert == self.y - 2:
                if square == None:
                    return True;
            if coordHorizontal == self.x and coordVert == self.y - 1:
                if square == None:
                    return True;
            return False;

class pieceKing(chessPiece):

    def checkAttack(self, boardArray, attackX, attackY):
        square=boardArray[attackX,attackY];
        if (abs(attackX - self.x) == 1) and (abs(attackY - self.y) == 1):
            if square is not None and square.faction is not self.faction:
                return True;
        return False;

    def checkMove(self, boardArray, moveX, moveY):
        square=boardArray[moveX,moveY];
        if (abs(moveX - self.x) == 1) and (abs(moveY - self.y) == 1):
            if square == None:
                return True;
        return False;





