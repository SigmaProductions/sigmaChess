from enum import Enum
from ChessEngine import pathing

class factionColor (Enum):
    FACTION_WHITE = 1
    FACTION_BLACK = 2

class chessPiece:
    name = None
    def __init__(self, hX, hY, faction):
        self.x = hX
        self.y = hY
        self.faction=faction


class piecePawn(chessPiece):
    name = "pawn"
    def checkAttack(self, boardArray, coordHorizontal, coordVert):
        square = boardArray[coordHorizontal][coordVert]
        if square is None:
            return False
        if self.faction == factionColor.FACTION_WHITE:
            if coordVert == self.y + 1 and (abs(coordHorizontal - self.x) == 1):
                if square.faction is not self.faction:
                    return True
                return False
        elif self.faction == factionColor.FACTION_BLACK:
            if coordVert + 1 == self.y  and (abs(coordHorizontal - self.x) == 1):
                if square.faction is not self.faction:
                    return True
            return False

    def checkMove(self, boardArray, coordHorizontal, coordVert):
        square = boardArray[coordHorizontal][coordVert]
        if square is not None:
            return False
        if self.faction == factionColor.FACTION_WHITE:
            if coordHorizontal == self.x and self.y == 1 and coordVert == self.y + 2:
                return True
            elif coordHorizontal == self.x and coordVert == self.y + 1:
                return True
            return False
        else:
            if coordHorizontal == self.x and self.y == 6 and coordVert == self.y - 2:
                return True
            if coordHorizontal == self.x and coordVert == self.y - 1:
                return True
            return False

class pieceKing(chessPiece):
    name = "king"

    def checkAttack(self, boardArray, coordHorizontal, coordVert):
        square=boardArray[coordHorizontal][coordVert]
        if (abs(coordHorizontal - self.x) <= 1) and (abs(coordVert - self.y) <= 1):
            if square is not None and square.faction is not self.faction:
                return True
        return False

    def checkMove(self, boardArray, coordHorizontal, coordVert):
        square=boardArray[coordHorizontal][coordVert]
        if square is not None:
            return False
        if (abs(coordHorizontal - self.x) <= 1) and (abs(coordVert - self.y) <= 1):
            return True
        return False

class pieceRook(chessPiece):
    name = "rook"

    def checkAttack(self, boardArray, coordHorizontal, coordVert):
        return self.checkMove(boardArray, coordHorizontal, coordVert)

    def checkMove(self, boardArray, coordHorizontal, coordVert):
        square = boardArray[coordHorizontal][coordVert]
        emptyPath = pathing.piecePath(self.x, self.y, boardArray, coordHorizontal, coordVert)
        if (coordVert == self.y or coordHorizontal == self.x) and emptyPath is not False:
            if square is None:
                return True
            if square.faction is not self.faction:
                return True
        return False

class pieceBishop(chessPiece):
    name = "bishop"

    def checkAttack(self, boardArray, coordHorizontal, coordVert):
        return self.checkMove(boardArray, coordHorizontal, coordVert)

    def checkMove(self, boardArray, coordHorizontal, coordVert):
        square = boardArray[coordHorizontal][coordVert]
        emptyPath = pathing.piecePath(self.x, self.y,boardArray, coordHorizontal, coordVert)
        if abs(coordHorizontal - self.x) == abs(coordVert - self.y) and emptyPath is not False:
            if square is None:
                return True
            if square.faction is not self.faction:
                return True
        return False

class pieceKnight(chessPiece):
    name = "knight"

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

class pieceQueen(chessPiece):
    name = "queen"

    def checkAttack(self, boardArray, coordHorizontal, coordVert):
        return self.checkMove(boardArray, coordHorizontal, coordVert)

    def checkMove(self, boardArray, coordHorizontal, coordVert):
        square = boardArray[coordHorizontal][coordVert]
        emptyPath = pathing.piecePath(self.x, self.y,boardArray, coordHorizontal, coordVert)
        if (abs(coordHorizontal - self.x) == abs(coordVert - self.y) or (coordVert == self.y or coordHorizontal == self.x)) and emptyPath is not False:
            if square is None:
                return True
            if square.faction is not self.faction:
                return True
        return False






