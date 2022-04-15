from os import stat
from Color import colorDictionary
import math

class Node(object):    
    # Constructor specifying Rect parameters and color
    def __init__(self, xpos, ypos, size, wall):
        self.x = xpos
        self.y = ypos

        self.nodeWidth = size
        self.nodeHeight = size
        
        self.wall = wall
        self.debug = False

        self.g = math.inf
        self.h = math.inf
        self.parent = None

        self.occupants = []

    # Get Rect representation of node
    def getRect(self):
        return (self.x, self.y, self.nodeWidth, self.nodeHeight)
    
    def getGridPos(self):
        return (math.floor(self.x / self.nodeWidth), math.floor(self.y / self.nodeHeight))

    def getWall(self):
        return self.wall
    
    def setWall(self, state):
        self.wall = state

    def makeWall(self):
        self.wall = True
        self.color = colorDictionary['BLACK']
    
    def getDebug(self):
        return self.debug

    def setDebug(self, status):
        self.debug = status

    def getOccupants(self):
        return self.occupants

    def addOccupant(self, occupant):
        self.occupants.append(occupant)

    def removeOccupant(self, occupant):
        if occupant in self.occupants:
            self.occupants.remove(occupant)

    def getFCost(self):
        return self.g + self.h

    def getGCost(self):
        return self.g

    def setGCost(self, cost):
        self.g = cost
    
    def setHCost(self, cost):
        self.h = cost

    def getParentNode(self):
        return self.parent

    def setParentNode(self, node):
        self.parent = node

    def resetNode(self):
        self.color = colorDictionary['BLACK']
        self.wall = False
        self.special = False
        self.occupants = []
