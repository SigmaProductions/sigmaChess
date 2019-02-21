from pymunk import *
import pygame
from pygame.locals import *
from pygame.color import *
import pymunk
from pymunk import Vec2d
import pymunk.pygame_util
class Physics:
    def __init__(self, board):
        self.board = board
        self.space=Space()
        self.space.gravity= 0.0,-900000.0
        self.space.sleep_time_threshold = 0.3
        self.constructEnvironment()
        self.figures= [[None for s in range(8)] for p in range(8)]
        
    def constructEnvironment(self):
        spaceSize = 512
        thiccness = 0.1
        bounds = [pymunk.Segment(self.space.static_body, (-32, -32), (-32, spaceSize-32), thiccness),
                  pymunk.Segment(self.space.static_body, (-32, spaceSize-32), (spaceSize-32, spaceSize-32), thiccness),
                  pymunk.Segment(self.space.static_body, (spaceSize-32, spaceSize-32), (spaceSize-32, -32), thiccness),
                  pymunk.Segment(self.space.static_body, (spaceSize-32, -32), (-32, -32), thiccness)]
        for wall in bounds:
            wall.friction = 1
            self.space.add(wall)
        pieceSize = 64
        for _ in range(32):
                pieceBody = pymunk.Body(0,0)
                pieceBox = pymunk.Poly.create_box(pieceBody,(pieceSize,pieceSize),1.0)
                pieceBox.mass = 100
                pieceBox.friction = 0.4
                self.space.add(pieceBody,pieceBox)

    def initFigures(self):
        i=0
        for x in range(8):
            for y in range(8):
                field= self.board.getPiece(x,y)
                if(field is not None):
                    body = self.space.bodies[i]
                    body.position= x*64,y*64
                    self.space.reindex_shapes_for_body(body)
                    self.figures[x][y]=body
                    i+=1
        i=0
        for x in range(8):
            for y in range(8):
                if (self.board.getPiece(x,y) is None) and (self.figures[x][y] is not None):
                    body = self.figures[x][y]
                    self.space.remove(body,body.shapes)
                    self.figures[x][y] = None

    def Step(self):
        self.space.step(0.0005)

    def MoveCallback(self):
        self.initFigures()