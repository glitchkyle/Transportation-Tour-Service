class Driver(object):
    def __init__(self, pos):
        self.currentPos = pos               # Grid Position
        self.assignedPassenger = None       # Passenger to pick up and serve
        self.currentDestination = None      # Current Destination on Grid
        self.pathQueue = []                 # Queue containing node positions to traverse
    
    def getPos(self):
        return self.currentPos
    
    def setPos(self, newPos):
        self.currentPos = newPos
    
    def getPassenger(self):
        return self.assignedPassenger
    
    def setPassenger(self, newPassenger):
        self.assignedPassenger = newPassenger
    
    def getDestination(self):
        return self.currentDestination

    def getPathLength(self):
        return len(self.pathQueue)
    
    def getNextPath(self):
        if self.getPathLength() > 0:
            searchPos = self.pathQueue[0]
            self.pathQueue.remove(searchPos)
            # Reached Destination
            if self.getPathLength() == 0:
                self.currentDestination = None
            return searchPos

    def setPath(self, newPath):
        if len(newPath) > 0:
            self.currentDestination = newPath[len(newPath) - 1]
            self.pathQueue = newPath
        