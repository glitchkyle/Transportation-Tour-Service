from Color import colorDictionary
import math

class Node(object):    
    # Constructor specifying Rect parameters and color
    def __init__(self, xpos, ypos, size, wall, special, color):
        self.x = xpos
        self.y = ypos

        self.nodeWidth = size
        self.nodeHeight = size
        
        self.color = color
        self.wall = wall
        self.special = special

        self.f = math.inf
        self.g = math.inf
        self.h = math.inf

        self.occupants = []

    # Get Rect representation of node
    def getRect(self):
        return (self.x, self.y, self.nodeWidth, self.nodeHeight)
    
    def getGridPos(self):
        return (math.floor(self.x / self.nodeWidth), math.floor(self.y / self.nodeHeight))
        
    def getColor(self):
        return self.color
    
    def setColor(self, color):
        self.color = color

    def getWall(self):
        return self.wall
    
    def setWall(self, state):
        self.wall = state

    def makeWall(self):
        self.wall = True
        self.color = colorDictionary['BLACK']

    def getSpecial(self):
        return self.special
    
    def setSpecial(self, state):
        self.special = state
    
    def getOccupants(self):
        return self.occupants

    def addOccupant(self, occupant):
        self.occupants.append(occupant)

    def removeOccupant(self, occupant):
        if occupant in self.occupants:
            self.occupants.remove(occupant)

    def resetNode(self):
        self.color = colorDictionary['BLACK']
        self.wall = False
        self.special = False
        self.occupants = []
