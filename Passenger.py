from PathFinding import calculateManhattanDistance
import math

class Passenger(object):
    def __init__(self, pos):
        self.currentPos = pos       # Grid Position
        self.destinations = []      # Node positions to be traversed
        self.pickedUp = False

    def getPos(self):
        return self.currentPos
    
    def getDestinations(self):
        return self.destinations
    
    def addDestination(self, newDest):
        if newDest not in self.destinations:
            self.destinations.append(newDest)
    
    def getNearestDestination(self, driverCurrentPos):
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
    
    def getPickedUp(self):
        return self.pickedUp
    
    def setPickedUp(self, status):
        self.pickedUp = status