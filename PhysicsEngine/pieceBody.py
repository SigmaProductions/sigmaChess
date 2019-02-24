from pymunk import *


class PieceBody:
    def __init__(self, board, chessPiece=None, body=None):
        self.board = board
        self.piece = chessPiece
        self.body = body
        self.timeIdle = 0 #increases pull force over time, resets with move

    """Check if piece is still in play and delete the body if it's not"""
    def amIAlive(self):
        for x in range(8):
            for y in range(8):
                if self.board.getPiece(x,y) == self.piece:
                    return True
        self.piece = None
        self.body.space.remove(self.body, self.body.shapes)
        return False
