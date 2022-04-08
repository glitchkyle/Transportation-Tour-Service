from Color import colorDictionary

class Node(object):
    # Default Constructor
    def __init__(self):
        self.x = None
        self.y = None
        self.nodeWidth = 0
        self.nodeHeight = 0
        self.color = colorDictionary['BLACK']

    # Constructor specifying Rect parameters and color
    def __init__(self, xpos, ypos, width, height, color):
        self.x = xpos
        self.y = ypos
        self.nodeWidth = width
        self.nodeHeight = height
        self.color = color

    # Get Rect representation of node
    def getRect(self):
        return (self.x, self.y, self.nodeWidth, self.nodeHeight)
        
    def getColor(self):
        return self.color
    
    def changeColor(self):
        pass

    def resetNode(self):
        pass
