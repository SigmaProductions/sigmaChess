from pymunk import *


class PieceBody:
    def __init__(self, chessPiece=None, body=None):
        self.piece = chessPiece
        self.body = body
