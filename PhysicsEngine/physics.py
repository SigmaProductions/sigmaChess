from pymunk import *
import pymunk
import pymunk.pygame_util
from PhysicsEngine import pieceBody
from math import *

class Physics:
    def __init__(self, board):
        self.board = board
        self.space=Space()
        self.space.gravity= 0.0,0.0
        self.space.sleep_time_threshold = 0.3
        self.space.damping = 0.001
        self.pieceBodies = [pieceBody.PieceBody() for i in range(32)]
        self.constructEnvironment()
        self.initFigures()

    def constructEnvironment(self):
        spaceSize = 512
        thiccness = 0.1
        bounds = [pymunk.Segment(self.space.static_body, (-32, -32), (-32, spaceSize-32), thiccness),
                  pymunk.Segment(self.space.static_body, (-32, spaceSize-32), (spaceSize-32, spaceSize-32), thiccness),
                  pymunk.Segment(self.space.static_body, (spaceSize-32, spaceSize-32), (spaceSize-32, -32), thiccness),
                  pymunk.Segment(self.space.static_body, (spaceSize-32, -32), (-32, -32), thiccness)]
        for wall in bounds:
            wall.friction = 0
            self.space.add(wall)
        pieceSize = 64
        i = 0
        for x in range(8):
            for y in range(8):
                if self.board.getPiece(x, y) is not None:
                    body = pymunk.Body(0, 0)
                    pieceBox = pymunk.Poly.create_box(body, (pieceSize, pieceSize), 1.0)
                    pieceBox.mass = 1000
                    pieceBox.friction = 0.4
                    self.space.add(body, pieceBox)
                    self.pieceBodies[i] = pieceBody.PieceBody(self.board.getPiece(x, y), body)
                    i += 1

    def pullFigures(self):
        for x in range(8):
            for y in range(8):
                field = self.board.getPiece(x, y)
                if field is not None:
                    for fig in self.pieceBodies:
                        if fig.piece == field:
                            vec1 = pymunk.Vec2d(fig.body.position)
                            vec2 = pymunk.Vec2d(field.x*64, field.y*64)
                            fig.body.force = (30000000/(0.1+pow(vec2.get_distance(vec1),2/3)))*(vec2-vec1)

    def initFigures(self):
        for x in range(8):
            for y in range(8):
                field = self.board.getPiece(x, y)
                if field is not None:
                    for fig in self.pieceBodies:
                        if fig.piece == field:
                            fig.body.position = (x*64, y*64)
                            self.space.reindex_shapes_for_body(fig.body)

    def forceImpulse(self):
        for x in range(8):
            for y in range(8):
                field = self.board.getPiece(x, y)
                if field is not None:
                    for fig in self.pieceBodies:
                        if fig.piece == field:
                            vec1 = pymunk.Vec2d(fig.body.position)
                            vec2 = pymunk.Vec2d(field.x*64, field.y*64)
                            fig.body.force += (100000000*(vec2-vec1))

    def Step(self):
        self.space.step(0.0005)
        self.pullFigures()

    def MoveCallback(self):
        self.forceImpulse()

