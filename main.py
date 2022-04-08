import time
from Grid import Grid

# Intialize Constants
SCREEN_SIZE = 800
GRID_SIZE = 40

def main():
    myGrid = Grid(SCREEN_SIZE, GRID_SIZE)
    
    myGrid.createGrid()
    myGrid.drawGrid()

    time.sleep(5)

if __name__ == "__main__":
    main()