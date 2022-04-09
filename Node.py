from Color import colorDictionary

class Node(object):
    # Constructor specifying Rect parameters and color
    def __init__(self, xpos, ypos, width, height, color):
        self.x = xpos
        self.y = ypos

        self.nodeWidth = width
        self.nodeHeight = height
        
        self.color = color

        self.occupants = []

    # Get Rect representation of node
    def getRect(self):
        return (self.x, self.y, self.nodeWidth, self.nodeHeight)
        
    def getColor(self):
        return self.color
    
    def changeColor(self):
        pass

    def resetNode(self):
        self.color = colorDictionary['WHITE']
        self.occupants = []
