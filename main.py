from Grid import Grid

# Intialize Constants
SCREEN_SIZE = 800
GRID_SIZE = 30
MAX_DRIVERS = 3

def test():
    myGrid = Grid(SCREEN_SIZE, GRID_SIZE)
    myGrid.createGrid()
    #myGrid.importGrid
    myGrid.addDrivers(1)

    # Handle all drivers
    myGrid.handleDrivers()


def main():
    myGrid = Grid(SCREEN_SIZE, GRID_SIZE)
    myGrid.createGrid()
    myGrid.addDrivers(MAX_DRIVERS)

    while True:
        for event in myGrid.getGridEvent():

            # Handle all key and click events
            myGrid.handleMousePressedEvent()
            myGrid.handleButtonPressedEvent(event)

        # Handle all passengers
        myGrid.handlePassengers()

        # Handle all drivers
        myGrid.handleDrivers()

        myGrid.drawGrid()

if __name__ == "__main__":
    main()