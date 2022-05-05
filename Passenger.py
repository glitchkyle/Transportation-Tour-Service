from PathFinding import sortDestinationDijkstra

class Passenger(object):
    def __init__(self, pos):
        """
        Constructor Method

        :param pos: Grid Position of Passenger
        :type pos: tuple
        """
        self.currentPos = pos       # Grid Position
        self.destinations = []      # Node positions to be traversed
        self.pickedUp = False
    
    # Accessors

    def getPos(self):
        return self.currentPos
    
    def getDestinations(self):
        return self.destinations
    
    def getPickedUp(self):
        return self.pickedUp

    # Mutators

    def setPickedUp(self, status):
        self.pickedUp = status
    
    def setDestinations(self, lst):
        self.destinations = lst
    
    # Methods
    
    def addDestination(self, newDest):
        """
        Add a destination to the list of passenger desired destinations

        :param newDest: Destination to be added
        :type newDest: tuple
        """
        if newDest not in self.destinations:
            self.destinations.append(newDest)
    
    def getNearestDestination(self):
        """
        Returns the nearest destination from the sorted queue of destinations
        
        :return: Nearest destination
        :rtype: tuple
        """
        currentDestination = self.destinations[0]
        self.destinations.remove(currentDestination)
        return currentDestination
    
    