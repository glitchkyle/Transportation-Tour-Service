import time
import pygame
from Grid import Grid

# Intialize Constants
SCREEN_SIZE = 800
GRID_SIZE = 60

def test():
    myGrid = Grid(SCREEN_SIZE, GRID_SIZE)
    
    myGrid.createGrid()
    myGrid.drawGrid()

    time.sleep(5)

def main():
    myGrid = Grid(SCREEN_SIZE, GRID_SIZE)
    myGrid.createGrid()

    while True:
        for event in myGrid.getGridEvent():
            myGrid.handleMousePressedEvent()
            myGrid.handleButtonPressedEvent(event)
            myGrid.drawGrid()

if __name__ == "__main__":
    main()