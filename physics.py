from pymunk import *

class Physics:
    def __init__(self):
        self.space=Space()
        self.space.gravity= 0.0,-9000.0

        shape= Segment(self.space.static_body,(-100,-0.1),(500,-0.1),0.0)
        shape.friction=100.0
        self.space.add(shape)


        self.figures= [[None for s in range(8)] for p in range(8)]
        

    def initFigures(self):
        #first remove every body from space, TODO change position dont recreate whole space each time
        for body in self.space.bodies:
            self.space.remove(body)
        
        for x in range(8):
            for y in range(8):
                field= self.board.getPiece(x,y)
                if(field is not None):
                    body= Body(10,10)
                    body.position=x,y

                    self.figures[x][y]=body

                    shape= Circle(body,0.5)
                    shape.collision_type=1
                    self.space.add(body,shape)
                    


    def BindToBoard(self, board):
        self.board= board
        self.initFigures()

    def run(self):
        self.space.step(0.0001)

    def BoardChanged(self):
        self.initFigures()



PhysicsSingleton= Physics()