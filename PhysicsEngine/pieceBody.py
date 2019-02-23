from pymunk import *


class PieceBody:
    def __init__(self, chessPiece=None, body=None):
        self.piece = chessPiece
        self.body = body
        self.timeIdle = 0 #increases pull force over time, resets with move
