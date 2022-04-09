import pygame
from Color import colorDictionary
from Node import Node
import math

# Initialize Constants
APP_TITLE = "Transportation/Touring Service"
SURFACE_BACKGROUND = colorDictionary['WHITE']
NODE_BORDER_COLOR = colorDictionary['BLACK']

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

    # Initialize grid with empty nodes
    def createGrid(self):
        for i in range(self.gridHeight):
            newRow = []
            for j in range(self.gridWidth):
                newNode = Node(i * self.gap, j * self.gap, self.gap, self.gap, NODE_BORDER_COLOR)
                newRow.append(newNode)
            self.grid.append(newRow)

    # Draw the grid with pygames
    def drawGrid(self):
        self.surface.fill(SURFACE_BACKGROUND)
        for row in self.grid:
            for node in row:
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
        if pygame.mouse.get_pressed()[0]:
            mousePosX, mousePosY = pygame.mouse.get_pos()
            selectedNode = self.getMousePosNode(mousePosX, mousePosY)
        elif pygame.mouse.get_pressed()[2]:
            print("Mouse Button Two Down")

    def getMousePosNode(self, mousePosX, mousePosY):
        return self.getNode(math.floor(mousePosX / self.gap), math.floor(mousePosY / self.gap))

    def getMousePos(self):
        return pygame.mouse.get_pos()

    def getNode(self, row, column):
        print(row, column)
        if (row <= self.gridHeight - 1 and row >= 0) and (column <= self.gridWidth - 1 and column >= 0): 
            return self.grid[row][column]



