class Driver(object):
    def __init__(self, pos):
        self.currentPos = pos       # Grid Position
        self.pathQueue = []         # Queue containing node positions to traverse
    
    def getPos(self):
        return self.currentPos
    
    def setPos(self, newPos):
        self.currentPos = newPos

    def getPathLength(self):
        return len(self.pathQueue)
    
    def getNextPath(self):
        if self.getPathLength() > 0:
            searchPos = self.pathQueue[0]
            self.pathQueue.remove(searchPos)
            return searchPos

    def setPath(self, newPath):
        self.pathQueue = newPath
    