import pygame, math, random, copy, time
from os.path import exists
from Color import colorDictionary
from Node import Node
from Driver import Driver
from PathFinding import findPathAStar

# Initialize Constants
APP_TITLE = "Transportation/Touring Service"

SURFACE_BACKGROUND = colorDictionary['WHITE']
NODE_DEFAULT_COLOR = colorDictionary['BLACK']
WALL_COLOR = colorDictionary['BLACK']
PASSENGER_COLOR = colorDictionary['YELLOW']
DRIVER_COLOR = colorDictionary['RED']

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

    # Initialize grid with empty nodes
    def createGrid(self):
        for i in range(self.gridHeight):
            newRow = []
            for j in range(self.gridWidth):
                newNode = Node(i * self.gap, j * self.gap, self.gap, False, False, NODE_DEFAULT_COLOR)
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
            raise Exception("Given file does not exist")
    
    # Initialize n drivers in grid
    def addDrivers(self, n):
        for i in range(n):
            selectedNode = self.getRandomTraversableNode()

            selectedNode.setSpecial(True)
            selectedNode.setColor(DRIVER_COLOR)

            newDriver = Driver(selectedNode.getGridPos())

            self.drivers.append(newDriver)
    
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
                if node.getWall() or node.getSpecial():
                    pygame.draw.rect(self.surface, node.color, node.getRect())
                else:
                    pygame.draw.rect(self.surface, node.color, node.getRect(), 1)
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
            
            # If drivers have a path, move to next path
            if driver.getPathLength() > 0:
                currentPos = driver.getPos()
                nextPos = driver.getNextPath()

                currentNode = self.getNode(currentPos[0], currentPos[1])
                nextNode = self.getNode(nextPos[0], nextPos[1])

                if not nextNode.getWall():

                    currentNode.removeOccupant(driver)
                    currentNode.setSpecial(False)
                    currentNode.setColor(NODE_DEFAULT_COLOR)

                    driver.setPos(nextPos)
                    nextNode.addOccupant(driver)
                    nextNode.setSpecial(True)
                    nextNode.setColor(DRIVER_COLOR)

            # If drivers have no path, create a random path
            else:
                destination = self.getRandomTraversableNode()
                path = findPathAStar(copy.deepcopy(self.grid), self.gridHeight, self.gridWidth, driver.getPos(), destination.getGridPos())
                driver.setPath(path)
            
            time.sleep(0.25)
    
    def handlePassengers(self):
        pass
    
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