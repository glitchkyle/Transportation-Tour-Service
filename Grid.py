import pygame, math, random, copy, time
from os.path import exists
from Color import colorDictionary
from Node import Node
from Driver import Driver
from Passenger import Passenger 
from PathFinding import findPathAStar

# Initialize Constants
APP_TITLE = "Transportation/Touring Service"

SURFACE_BACKGROUND = colorDictionary['WHITE']
NODE_DEFAULT_COLOR = colorDictionary['BLACK']
WALL_COLOR = colorDictionary['BLACK']
PASSENGER_COLOR = colorDictionary['YELLOW']
DRIVER_COLOR = colorDictionary['RED']
DEBUG_COLOR = colorDictionary['BLUE']

pygame.display.set_caption(APP_TITLE)

class Grid():
    # Constructor specifying window size and grid size (rows and columns)
    def __init__(self, winSize, gridSize):
        self.grid = []
        self.surface = pygame.display.set_mode((winSize, winSize))
        
        self.screenWidth = winSize
        self.screenHeight = winSize

        self.gridWidth = gridSize
        self.gridHeight = gridSize

        self.gap = winSize / gridSize

        self.selectedNode = None
        self.drivers = []
        self.passengers = []

    # Initialize grid with empty nodes
    def createGrid(self):
        for i in range(self.gridHeight):
            newRow = []
            for j in range(self.gridWidth):
                newNode = Node(i * self.gap, j * self.gap, self.gap, False)
                newRow.append(newNode)
            self.grid.append(newRow)

    # Initialize grid from file containing blocked nodes and filled nodes
    def importGrid(self, file):
        if exists(file):
            with open(file, 'r') as importFile:
                for line in importFile:
                    position = line.strip().split(" ")
                    position[0], position[1] = int(position[0]), int(position[1])
                    node = self.getNode(position[0], position[1])
                    if node is not None:
                        node.makeWall()
        else:
            raise Exception("Given import file does not exist")
    
    # Initialize n drivers in grid
    def addDrivers(self, n):
        for i in range(n):
            selectedNode = self.getRandomTraversableNode()

            newDriver = Driver(selectedNode.getGridPos())

            self.drivers.append(newDriver)
            selectedNode.addOccupant(newDriver)
    
    # Initialize n passengers in grid
    def addRandomPassengers(self, n, d):
        for i in range(n):
            selectedNode = self.getRandomTraversableNode()

            newPassenger = Passenger(selectedNode.getGridPos())

            for j in range(d):
                randomNode = self.getRandomTraversableNode()
                randomNode.setDebug(True)
                newPassenger.addDestination(randomNode.getGridPos())

            print(f"Passenger is at {newPassenger.getPos()}")
            print(f"Passenger Destinations are {newPassenger.getDestinations()}")

            self.passengers.append(newPassenger)
            selectedNode.addOccupant(newPassenger)
    
    # Get a random traversable node from grid
    def getRandomTraversableNode(self):        
        while True:
            randomRow = random.randint(0, self.gridWidth-1)
            randomColumn = random.randint(0, self.gridHeight-1)
            selectedNode = self.getNode(randomRow, randomColumn)
            if not selectedNode.getWall():
                return selectedNode
    
    # Draw the grid with pygames
    def drawGrid(self):
        self.surface.fill(SURFACE_BACKGROUND)
        for row in self.grid:
            for node in row:
                # If node is for debugging
                if node.getDebug():
                    pygame.draw.rect(self.surface, DEBUG_COLOR, node.getRect())
                # If node is wall
                elif node.getWall():
                    pygame.draw.rect(self.surface, WALL_COLOR, node.getRect())
                # If node contains drivers
                elif any(isinstance(driver, Driver) for driver in node.getOccupants()):
                    pygame.draw.rect(self.surface, DRIVER_COLOR, node.getRect())
                # If node contains passengers
                elif any(isinstance(passenger, Passenger) for passenger in node.getOccupants()):
                    pygame.draw.rect(self.surface, PASSENGER_COLOR, node.getRect())
                else:
                    pygame.draw.rect(self.surface, NODE_DEFAULT_COLOR, node.getRect(), 1)
        pygame.display.update()

    def getGridEvent(self):
        return pygame.event.get()

    def handleMousePressedEvent(self):
        # If left mouse button was pressed
        if pygame.mouse.get_pressed()[0]:
            selectedNode = self.getMousePosNode()
            selectedNode.makeWall()
        # If right mouse button was pressed
        elif pygame.mouse.get_pressed()[2]:
            pass
    
    def handleButtonPressedEvent(self, event):
        # If user pressed a button
        if event.type == pygame.KEYDOWN:
            # If user pressed D key, reset node
            if event.key == pygame.K_d:
                selectedNode = self.getMousePosNode()
                selectedNode.resetNode()
    
    def handleDrivers(self):
        for driver in self.drivers:
            # Assign passenger if driver has no passenger
            if len(self.passengers) > 0:
                currentPassenger = self.passengers[0]
                driver.setPassenger(currentPassenger)
                self.passengers.remove(currentPassenger)

            currentPassenger = driver.getPassenger()
            
            # Check if driver has assigned passenger
            if currentPassenger is not None:
                # Check if passenger has been picked up
                if currentPassenger.getPickedUp():
                    # Check if passenger reached last destination
                    if len(currentPassenger.getDestinations()) > 0 and driver.getPathLength() == 0:
                        # Go to next destination desired by passenger
                        nextDestination = currentPassenger.getNearestDestination(driver.getPos())
                        print(f"Passenger now being driven to {nextDestination}!")
                        path = findPathAStar(copy.deepcopy(self.grid), self.gridHeight, self.gridWidth, driver.getPos(), nextDestination)
                        driver.setPath(path)
                    elif len(currentPassenger.getDestinations()) == 0:
                        print("Passenger has been served!")
                        driver.setPassenger(None)
                # If passenger not picked up and driver has no calculated path to passenger
                elif driver.getPathLength() == 0:
                    # Path is now destination to passenger
                    path = findPathAStar(copy.deepcopy(self.grid), self.gridHeight, self.gridWidth, driver.getPos(), currentPassenger.getPos())
                    driver.setPath(path)
            
            # If drivers have a path, move to next path
            if driver.getPathLength() > 0:
                currentPos = driver.getPos()
                nextPos = driver.getNextPath()

                currentNode = self.getNode(currentPos[0], currentPos[1])
                nextNode = self.getNode(nextPos[0], nextPos[1])

                if not nextNode.getWall():

                    currentNode.removeOccupant(driver)

                    driver.setPos(nextPos)
                    nextNode.addOccupant(driver)
                    
                    if currentPassenger is not None:
                        # Check if passenger has been reached
                        if driver.getPos() == currentPassenger.getPos():
                            # Pick up passenger
                            print("Picked Up Passenger!")
                            x, y = currentPassenger.getPos()
                            passengerNode = self.getNode(x, y)
                            passengerNode.removeOccupant(currentPassenger)
                            currentPassenger.setPickedUp(True)

            # If drivers have no path, create a random path for hovering
            else:
                destination = self.getRandomTraversableNode()
                path = findPathAStar(copy.deepcopy(self.grid), self.gridHeight, self.gridWidth, driver.getPos(), destination.getGridPos())
                driver.setPath(path)
            
            time.sleep(0.25)
    
    # Get node from mouse position
    def getMousePosNode(self):
        mousePosX, mousePosY = self.getMousePos()
        x = math.floor(mousePosX / self.gap)
        y = math.floor(mousePosY / self.gap)
        return self.getNode(x, y)

    # Get current mouse position
    def getMousePos(self):
        return pygame.mouse.get_pos()

    # Get node using row and column as indices
    def getNode(self, row, column):
        if (row < self.gridHeight and row >= 0) and (column < self.gridWidth and column >= 0): 
            return self.grid[row][column]