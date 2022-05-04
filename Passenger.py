from PathFinding import calculateManhattanDistance
import math

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
    
    # Methods
    
    def addDestination(self, newDest):
        """
        Add a destination to the list of passenger desired destinations

        :param newDest: Destination to be added
        :type newDest: tuple
        """
        if newDest not in self.destinations:
            self.destinations.append(newDest)
    
    def getNearestDestination(self, driverCurrentPos):
        """
        Finds the closest destination from current position 
        
        :param driverCurrentPos: Position of driver and passenger
        :type driverCurrentPos: tuple
        :return: Nearest destination
        :rtype: tuple
        """
        cheapestDestination = self.destinations[0]
        x1, y1 = driverCurrentPos

        x2, y2 = cheapestDestination
        minValDestination = calculateManhattanDistance(x1, y1, x2, y2)

        for pos in self.destinations:
            x2, y2 = pos
            if calculateManhattanDistance(x1, y1, x2, y2) < minValDestination:
                minValDestination = calculateManhattanDistance(x1, y1, x2, y2)
                cheapestDestination = pos
        
        self.destinations.remove(cheapestDestination)
        return cheapestDestination
    
    