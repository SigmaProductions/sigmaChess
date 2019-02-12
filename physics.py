from pymunk import *

class Physics:
    def __init__(self):
        self.space=Space()
        self.space.gravity= 0.0,-9000.0

        self.constructEnvironment()

        for _ in range(32):
            body= Body(10,10)
            body.position=0,0
            shape= Poly(body,[(0,0),(0,1),(1,1),(1,0)])
            shape.collision_type=1
            self.space.add(body,shape)
                    

        self.figures= [[None for s in range(8)] for p in range(8)]
        
    def constructEnvironment(self):
        #constructing box inside which whole chessboard is

        box=list()
        box.append(Segment(self.space.static_body,(0,8),(0,0),0.0))
        box.append(Segment(self.space.static_body,(8,8),(0,8),0.0))
        box.append(Segment(self.space.static_body,(8,8),(8,0),0.0))
        box.append(Segment(self.space.static_body,(0,0),(8,0),0.0))
        for wall in box:
            wall.friction=0.0
            self.space.add(wall)

    def initFigures(self):
        i=0
        for x in range(8):
            for y in range(8):
                field= self.board.getPiece(x,y)
                if(field is not None):
                    body = self.space.bodies[i]
                    body.position= x,y
                    self.figures[x][y]=body
                    i+=1
                    

    def BindToBoard(self, board):
        self.board= board
        self.initFigures()

    def run(self):
        self.space.step(0.0005)

    def BoardChanged(self):
        self.initFigures()



PhysicsSingleton= Physics()