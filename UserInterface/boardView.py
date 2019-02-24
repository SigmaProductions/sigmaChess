from tkinter import *
from PIL import ImageTk
from UserInterface.Resources.boardImagesDict import BoardGraphicsDict
from ChessEngine import pieces
from math import pi
from PIL import Image
from ChessEngine.boardObserver import Observer

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
        self.observer = Observer()

    def drawBoard(self, physicsClient,chessBoard):
        """this method wipes canvas in the frame and draws it anew"""
        self.piecesCanvas.delete("all")
        self.piecesCanvas.create_image(256, 256, image=self.piecesImages["tile"])
        for i in range(8):
            for j in range(8):
                tilePiece = chessBoard.getPiece(i, j)
                body = pymunk.Body()
                if tilePiece is not None:
                    for fig in physicsClient.pieceBodies:
                        if fig.piece == tilePiece:
                            body = fig.body
                    #piece rotation with transparent background

                    if tilePiece.faction == pieces.factionColor.FACTION_WHITE:
                        piece = self.piecesImages[tilePiece.name]
                    else:
                        piece = self.piecesImages[tilePiece.name + "Black"]
                    '''highlightCallback returns the currently selected piece from EventHandler'''
                    if self.observer.callbacks.__len__() > 0:
                        if tilePiece == self.observer.callbacks[0]():
                            dummy = piece.copy()
                            dummy.alpha_composite(self.piecesImages["highlight"])
                            rot = dummy.rotate(int(body.angle * 180 / pi), expand=1)
                        else:
                            rot = piece.rotate(int(body.angle*180/pi), expand=1)
                    else:
                        rot = piece.rotate(int(body.angle * 180 / pi), expand=1)
                    fff = Image.new('RGBA', rot.size, (255,255,255,0))
                    out = Image.composite(rot, fff, rot)
                    out.convert('RGBA')
                    tilePiece.pieceImage = ImageTk.PhotoImage(image=out)
                    coords = list(self.__translateBoardCoords(i, j, chessBoard.whoMoved, physicsClient))
                    self.piecesCanvas.create_image(coords, image=tilePiece.pieceImage)
                    if self.observer.callbacks.__len__() > 0:
                        self.drawMoves(chessBoard, self.observer.callbacks[0]())

    def addBinding(self, eventName, function):
        self.piecesCanvas.bind(eventName, function)

    def drawMoves(self,chessBoard,piece):
        if piece is None or chessBoard is None:
            return
        for x in range(8):
            for y in range(8):
                if piece.checkMove(chessBoard.boardArray,x,y) or piece.checkAttack(chessBoard.boardArray,x,y):
                    self.piecesCanvas.create_image(self.__translateBoardCoords(x,y,chessBoard.whoMoved), image=self.piecesImages.highlightTk)

    def __translateBoardCoords(self,boardPositionX, boardPositionY, whoMoved, physicsClient=None):
        """translates integer position on the chess board to pixel position in canvas"""
        if physicsClient is not None:
            figure = pymunk.Body()
            for fig in physicsClient.pieceBodies:
                if fig.piece == physicsClient.board.getPiece(boardPositionX,boardPositionY):
                    figure = fig.body
            x=figure.position[0]/64
            y=figure.position[1]/64
        else:
            x=boardPositionX
            y=boardPositionY
        if whoMoved == pieces.factionColor.FACTION_WHITE:
            x = 7 - x
            y = 7 - y
        return (x*64 + 32
                , 512 - (y*64)-32)
