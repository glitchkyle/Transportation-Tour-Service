from Color import colorDictionary

class Node(object):
    # Constructor specifying Rect parameters and color
    def __init__(self, xpos, ypos, width, height, wall, special, color):
        self.x = xpos
        self.y = ypos

        self.nodeWidth = width
        self.nodeHeight = height
        
        self.color = color
        self.wall = wall
        self.special = special

        self.occupants = []

    # Get Rect representation of node
    def getRect(self):
        return (self.x, self.y, self.nodeWidth, self.nodeHeight)
        
    def getColor(self):
        return self.color
    
    def setColor(self, color):
        self.color = color

    def getWall(self):
        return self.wall
    
    def setWall(self, state):
        self.wall = state

    def getSpecial(self):
        return self.special
    
    def setSpecial(self, state):
        self.special = state

    def resetNode(self):
        self.color = colorDictionary['BLACK']
        self.wall = False
        self.special = False
        self.occupants = []
