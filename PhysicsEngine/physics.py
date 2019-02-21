from pymunk import *
import pymunk
import pymunk.pygame_util


class Physics:
    def __init__(self, board):
        self.board = board
        self.space=Space()
        self.space.gravity= 0.0,-300000.0
        self.space.sleep_time_threshold = 0.3
        self.constructEnvironment()
        self.figures= [[None for s in range(8)] for p in range(8)]
        self.assignBodies()

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
        for _ in range(64):
            pieceBody = pymunk.Body(0,0)
            pieceBox = pymunk.Poly.create_box(pieceBody,(pieceSize,pieceSize),1.0)
            pieceBox.mass = 1000
            pieceBox.friction = 0.4
            self.space.add(pieceBody,pieceBox)

    def assignBodies(self):
        i = 0
        for x in range(8):
            for y in range(8):
                body = self.space.bodies[i]
                self.figures[x][y]=body
                i += 1

    def initFigures(self):
        i = 0
        self.assignBodies()
        for x in range(8):
            for y in range(8):
                field = self.board.getPiece(x, y)
                body = self.figures[x][y]
                if field is not None:
                    body.position = x*64, y*64
                else:
                    body.position = 10000, 10000
                body.velocity = (0, 0)
                self.space.reindex_shapes_for_body(body)
                i += 1

    def Step(self):
        self.space.step(0.0005)

    def MoveCallback(self):
        self.initFigures()