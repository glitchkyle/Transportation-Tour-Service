import pygame, math, random, copy, time
from os.path import exists
from Color import colorDictionary
from Node import Node
from Driver import Driver
from Passenger import Passenger 
from PathFinding import findPathAStar

# Initialize Constants

APP_TITLE = "Transportation/Touring Service"

DESTINATION_SAVE_GRID = "savedGrid.txt"

DRIVER_SPEED = 0.1                  # Speed of Drivers
MAX_PASSENGERS = 7                  # Maximum possible passengers within the grid at a time
PASSENGER_SPAWN_RATE = 5            # Chances of a passenger spawning at a given moment
MAX_PASSENGER_DESTINATIONS = 3      # Maximum possible destinations passengers can have

SURFACE_BACKGROUND = colorDictionary['WHITE']
NODE_DEFAULT_COLOR = colorDictionary['BLACK']
WALL_COLOR = colorDictionary['BLACK']
PASSENGER_COLOR = colorDictionary['YELLOW']
DRIVER_COLOR = colorDictionary['RED']
DEBUG_COLOR = colorDictionary['BLUE']
DRIVER_HIGHLIGHTED_COLOR = colorDictionary['ORANGE']
DESTINATION_HIGHLIGHTED_COLOR = colorDictionary['GREEN']

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

        self.highlightedDriver = None

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
    
    def saveGrid(self, desFile):
        walls = ""
        # Get all walled nodes
        for i in range(self.gridHeight):
            for j in range(self.gridWidth):
                currentNode = self.getNode(i, j)
                if currentNode.isWall():
                    wallPos = str(i) + ' ' + str(j) + '\n'
                    walls += wallPos
        # Write all walled nodes to destination file
        with open(desFile, 'w') as df:
            df.write(walls)
    
    # Initialize n drivers in grid
    def addDrivers(self, n):
        for i in range(n):
            selectedNode = self.getRandomTraversableNode()

            newDriver = Driver(selectedNode.getGridPos())

            self.drivers.append(newDriver)
            selectedNode.addOccupant(newDriver)
    
    # Initialize n passengers in grid
    def addPassengers(self, n):
        for i in range(n):
            selectedNode = self.getRandomTraversableNode()

            newPassenger = Passenger(selectedNode.getGridPos())

            numDestinations = random.randint(1, MAX_PASSENGER_DESTINATIONS)

            for j in range(numDestinations):
                randomNode = self.getRandomTraversableNode()
                #randomNode.setDebug(True)
                newPassenger.addDestination(randomNode.getGridPos())

            self.passengers.append(newPassenger)
            selectedNode.addOccupant(newPassenger)
    
    def addRandomPassenger(self, maximumDestinations):
        selectedNode = self.getRandomTraversableNode()

        newPassenger = Passenger(selectedNode.getGridPos())

        numDestinations = random.randint(1, maximumDestinations)

        for j in range(numDestinations):
            randomNode = self.getRandomTraversableNode()
            #randomNode.setDebug(True)
            newPassenger.addDestination(randomNode.getGridPos())

        self.passengers.append(newPassenger)
        selectedNode.addOccupant(newPassenger)
    
    # Get a random traversable node from grid
    def getRandomTraversableNode(self):        
        while True:
            randomRow = random.randint(0, self.gridWidth-1)
            randomColumn = random.randint(0, self.gridHeight-1)
            selectedNode = self.getNode(randomRow, randomColumn)
            if not selectedNode.isWall() and not selectedNode.containsDrivers() and not selectedNode.containsPassengers():
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
                elif node.isWall():
                    pygame.draw.rect(self.surface, WALL_COLOR, node.getRect())
                # If node contains drivers
                elif node.containsDrivers():
                    pygame.draw.rect(self.surface, DRIVER_COLOR, node.getRect())
                # If node contains passengers
                elif node.containsPassengers():
                    pygame.draw.rect(self.surface, PASSENGER_COLOR, node.getRect())
                else:
                    pygame.draw.rect(self.surface, NODE_DEFAULT_COLOR, node.getRect(), 1)
                
                if self.highlightedDriver is not None:
                    # Highlight Driver
                    currentPosition = self.highlightedDriver.getPos()
                    posX, posY = currentPosition
                    highlightedDriver = self.getNode(posX, posY)
                    pygame.draw.rect(self.surface, DRIVER_HIGHLIGHTED_COLOR, highlightedDriver.getRect())

                    # Highlight Destination
                    currentDestination = self.highlightedDriver.getDestination()
                    if currentDestination is not None:
                        desX, desY = currentDestination
                        highlightedDestination = self.getNode(desX, desY)
                        pygame.draw.rect(self.surface, DESTINATION_HIGHLIGHTED_COLOR, highlightedDestination.getRect())

        pygame.display.update()

    def getGridEvent(self):
        return pygame.event.get()

    def setHighlightedDriver(self, node):
        if node.containsDrivers():
            self.highlightedDriver = node.getDriver()

    def clearHighlightedDriver(self):
        self.highlightedDriver = None

    def handleMousePressedEvent(self):
        # If left mouse button was pressed, highlight driver in selected node
        if pygame.mouse.get_pressed()[0]:
            selectedNode = self.getMousePosNode()
            self.setHighlightedDriver(selectedNode)
        # If right mouse button was pressed, create wall
        elif pygame.mouse.get_pressed()[2]:
            selectedNode = self.getMousePosNode()
            selectedNode.makeWall()
        
    def handleButtonPressedEvent(self, event):
        # If user pressed a button
        if event.type == pygame.KEYDOWN:
            # If user pressed D key, reset node
            if event.key == pygame.K_d:
                selectedNode = self.getMousePosNode()
                selectedNode.resetNode()
            # If user pressed Space key, add random passenger
            elif event.key == pygame.K_SPACE:
                if len(self.passengers) < MAX_PASSENGERS:
                    self.addRandomPassenger(MAX_PASSENGER_DESTINATIONS)
            # If user pressed C key, clear highlighted driver
            elif event.key == pygame.K_c:
                self.clearHighlightedDriver()
            elif event.key == pygame.K_s:
                self.saveGrid(DESTINATION_SAVE_GRID)
            elif event.key == pygame.K_p:
                pygame.quit()
                raise Exception("Program Stopped")
    
    def handlePassengers(self):
        if len(self.passengers) < MAX_PASSENGERS:
            spawnChance = random.randint(1, 100)
            if spawnChance <= PASSENGER_SPAWN_RATE:
                self.addRandomPassenger(MAX_PASSENGER_DESTINATIONS)
    
    def handleDrivers(self):
        for driver in self.drivers:
            # Assign passenger if driver has no passenger
            if len(self.passengers) > 0 and driver.getPassenger() is None:
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

                if not nextNode.isWall():

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
            
            time.sleep(DRIVER_SPEED)
    
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