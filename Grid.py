import pygame
from Color import colorDictionary
from Node import Node
import math

# Initialize Constants
APP_TITLE = "Transportation/Touring Service"
SURFACE_BACKGROUND = colorDictionary['WHITE']
NODE_BORDER_COLOR = colorDictionary['BLACK']
PASSENGER_COLOR = colorDictionary['YELLOW']

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

        self.newlyAddedNode = None

    # Initialize grid with empty nodes
    def createGrid(self):
        for i in range(self.gridHeight):
            newRow = []
            for j in range(self.gridWidth):
                newNode = Node(i * self.gap, j * self.gap, self.gap, self.gap, False, False, NODE_BORDER_COLOR)
                newRow.append(newNode)
            self.grid.append(newRow)

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

    def resetGrid(self):
        for row in self.grid:
            for node in row:
                node.resetNode()
    
    def deleteGrid(self):
        pygame.quit()

    def getGridEvent(self):
        return pygame.event.get()

    def handleMousePressedEvent(self):
        # If left mouse button was pressed
        if pygame.mouse.get_pressed()[0]:
            mousePosX, mousePosY = pygame.mouse.get_pos()
            selectedNode = self.getMousePosNode(mousePosX, mousePosY)
            selectedNode.setColor(PASSENGER_COLOR)
            selectedNode.setSpecial(True)
            self.newlyAddedNode = selectedNode
        # If right mouse button was pressed
        elif pygame.mouse.get_pressed()[2]:
            if self.newlyAddedNode is not None:
                mousePosX, mousePosY = pygame.mouse.get_pos()
                selectedNode = self.getMousePosNode(mousePosX, mousePosY)
    
    def handleButtonPressedEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                mousePosX, mousePosY = pygame.mouse.get_pos()
                selectedNode = self.getMousePosNode(mousePosX, mousePosY)
                selectedNode.resetNode()

    def getMousePosNode(self, mousePosX, mousePosY):
        x = math.floor(mousePosX / self.gap)
        y = math.floor(mousePosY / self.gap)
        return self.getNode(x, y)

    def getMousePos(self):
        return pygame.mouse.get_pos()

    def getNode(self, row, column):
        if (row <= self.gridHeight - 1 and row >= 0) and (column <= self.gridWidth - 1 and column >= 0): 
            return self.grid[row][column]