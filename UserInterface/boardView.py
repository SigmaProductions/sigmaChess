from tkinter import *
from PIL import ImageTk
from UserInterface.Resources.boardImagesDict import BoardGraphicsDict
from ChessEngine import pieces
from PhysicsEngine import physics
from math import pi
from PIL import Image
from math import sqrt

import pymunk.body

class BoardView(Frame):

    def __init__(self,master):
        super().__init__(master)
        #load pieces images from graphics/pieces/ folder
        self.piecesImages = BoardGraphicsDict()
        self.piecesImages.loadImages()
        self.config(bd=3,relief=GROOVE)
        #create boardCanvas on which tiles and pieces will be drawn
        self.piecesCanvas = Canvas(self, width=64 * 8,
                              height=64 * 8)
        self.piecesCanvas.pack()

    def drawBoard(self, physicsClient,chessBoard):
        """this method wipes canvas in the frame and draws it anew"""
        self.piecesCanvas.delete("all")
        self.piecesCanvas.create_image(256,256, image=self.piecesImages["tile"])
        for i in range(8):
            for j in range(8):
                tilePiece = chessBoard.getPiece(i, j)

                if tilePiece is not None:
                    #piece rotation with transparent background
                    if tilePiece.faction == pieces.factionColor.FACTION_WHITE:
                        rot = self.piecesImages[tilePiece.name].rotate(int(physicsClient.figures[i][j].angle*180/pi), expand=1)
                    else:
                        rot = self.piecesImages[tilePiece.name + "Black"].rotate(int(physicsClient.figures[i][j].angle*180/pi), expand=1)
                    fff = Image.new('RGBA', rot.size, (255,255,255,0))
                    out = Image.composite(rot, fff, rot)
                    out.convert('RGBA')
                    tilePiece.pieceImage = ImageTk.PhotoImage(image=out)
                    coords = list(self.__translateBoardCoords(physicsClient,i, j, chessBoard.whoMoved))
                    self.piecesCanvas.create_image(coords, image=tilePiece.pieceImage)

    def addBinding(self, eventName, function):
        self.piecesCanvas.bind(eventName, function)

    def __translateBoardCoords(self, physicsClient,boardPositionX, boardPositionY, whoMoved):
        """translates integer position on the chess board to pixel position in canvas"""
        figure=physicsClient.figures[boardPositionX][boardPositionY]
        if(whoMoved is None):
            x=boardPositionX
            y=boardPositionY
        else:
            x=figure.position[0]/64
            y=figure.position[1]/64
        if whoMoved == pieces.factionColor.FACTION_WHITE:
            x = 7 - x
            y = 7 - y 
        return (x*64 + 32
                , 512 - (y*64)-32)




