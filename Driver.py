class Driver(object):
    def __init__(self, pos):
        """
        Constructor Method

        :param pos: Grid Position of Driver
        :type pos: tuple
        """
        self.currentPos = pos               # Grid Position
        self.assignedPassenger = None       # Passenger to pick up and serve
        self.currentDestination = None      # Current Destination on Grid
        self.pathQueue = []                 # Queue containing node positions to traverse
    
    # Accessors

    def getPos(self):
        return self.currentPos
    
    def getPassenger(self):
        return self.assignedPassenger
    
    def getDestination(self):
        return self.currentDestination

    def getPathLength(self):
        return len(self.pathQueue)
    
    # Mutators
    
    def setPos(self, newPos):
        self.currentPos = newPos
    
    def setPassenger(self, newPassenger):
        self.assignedPassenger = newPassenger
    
    # Methods
    
    def getNextPath(self):
        """
        Gets next traversable position in path
        
        :return: Position to be traversed
        :rtype: tuple
        """
        if self.getPathLength() > 0:
            searchPos = self.pathQueue[0]
            self.pathQueue.remove(searchPos)
            # Reached Destination
            if self.getPathLength() == 0:
                self.currentDestination = None
            return searchPos

    def setPath(self, newPath):
        """
        Sets new path for driver to traverse

        :param newPath: New path for driver
        :type newPath: tuple list
        """
        if len(newPath) > 0:
            self.currentDestination = newPath[len(newPath) - 1]
            self.pathQueue = newPath
        