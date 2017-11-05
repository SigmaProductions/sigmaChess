from controller.networking import multiplayer
from pieces import piecePawn
from pieces import factionColor

test= multiplayer.ConnectionHandler()
test.SendMove(piecePawn(0,0,factionColor.FACTION_BLACK),(1,0))

input()