from Color import colorDictionary
import math
from Driver import Driver
from Passenger import Passenger

class Node(object):    
    # Constructor specifying Rect parameters and color
    def __init__(self, xpos, ypos, size, wall):
        """
        Constructor Method for Node

        :param xpos: X position of node
        :type xpos: int 
        :param ypos: Y position of node
        :type ypos: int 
        :param size: Size of node in Pygame pixels
        :type size: int 
        :param wall: True if node will act as a wall
        :type wall: bool
        """
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
    
    # Accessors 
    def isWall(self):
        return self.wall
    
    def getDebug(self):
        return self.debug
    
    def getOccupants(self):
        return self.occupants
    
    def getParentNode(self):
        return self.parent
    
    def getGCost(self):
        return self.g

    # Mutators
    def setWall(self, state):
        self.wall = state
    
    def setDebug(self, status):
        self.debug = status
    
    def setGCost(self, cost):
        self.g = cost
    
    def setHCost(self, cost):
        self.h = cost

    def setParentNode(self, node):
        self.parent = node

    # Methods

    def getRect(self):
        """
        Gets Rect representation of node for drawing in Pygame

        :return: Position and size of node
        :rtype: tuple
        """
        return (self.x, self.y, self.nodeWidth, self.nodeHeight)
    
    # Get Grid Position of Node
    def getGridPos(self):
        """
        Gets grid position of node using position and size
        
        :return: Grid position of node 
        :rtype: tuple
        """
        return (math.floor(self.x / self.nodeWidth), math.floor(self.y / self.nodeHeight))

    def makeWall(self):
        """
        Sets node to be a wall
        """
        self.wall = True
        self.color = colorDictionary['BLACK']

    def getDriver(self):
        """
        Gets a random driver within occupants attribute

        :return: Driver from occupants attribute
        :rtype: Driver
        """
        for occupant in self.occupants:
            if isinstance(occupant, Driver):
                return occupant
    
    def containsDrivers(self):
        """
        Checks if there are drivers within the node

        :return: True if there are drivers occupying node
        :rtype: bool
        """
        return any(isinstance(driver, Driver) for driver in self.getOccupants())

    def containsPassengers(self):
        """
        Checks if there are passengers within the node

        :return: True if there are passengers occupying node
        :rtype: bool
        """
        return any(isinstance(passenger, Passenger) for passenger in self.getOccupants())

    def addOccupant(self, occupant):
        """
        Adds an occupant to the occupants list of the node

        :param occupant: Occupant to be added
        :type occupant: Driver or Passenger
        """
        self.occupants.append(occupant)

    def removeOccupant(self, occupant):
        """
        Removes a specific occupant from the occupants list of the node 

        :param occupant: Occupant to be removed
        :type occupant: Driver or Passenger
        """
        if occupant in self.occupants:
            self.occupants.remove(occupant)

    def getFCost(self):
        """
        Returns total cost of node to be used in A* path finding

        :return: Cost from start node plus cost to end node
        :rtype: int
        """
        return self.g + self.h

    def resetNode(self):
        """
        Resets node attributes to make node into a regular traversable path
        """
        self.color = colorDictionary['BLACK']
        self.wall = False
        self.special = False
        self.occupants = []
