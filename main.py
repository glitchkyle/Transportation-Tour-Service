import time
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
    #myGrid.importGrid
    myGrid.addDrivers(5)

    while True:
        for event in myGrid.getGridEvent():

            # Handle all key and click events
            myGrid.handleMousePressedEvent()
            myGrid.handleButtonPressedEvent(event)

            # Handle all passengers
            #myGrid.handlePassengers()

            # Handle all drivers
            #myGrid.handleDrivers()

            myGrid.drawGrid()

if __name__ == "__main__":
    main()