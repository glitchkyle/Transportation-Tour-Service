from Grid import Grid

# Intialize Constants

SCREEN_SIZE = 1000
GRID_SIZE = 20
IMPORT_GRID = "testGrid.txt"

MAX_DRIVERS = 3                         # Maximum drivers within the grid at a time
STARTING_RANDOM_PASSENGERS = 3          # Starting passengers in grid

def test():
    pass

def main():
    myGrid = Grid(SCREEN_SIZE, GRID_SIZE)
    myGrid.createGrid()
    myGrid.importGrid(IMPORT_GRID)
    myGrid.addDrivers(MAX_DRIVERS)
    myGrid.addPassengers(STARTING_RANDOM_PASSENGERS)

    while True:
        for event in myGrid.getGridEvent():

            # Handle all key and click events
            myGrid.handleMousePressedEvent()
            myGrid.handleButtonPressedEvent(event)

        # Handle passengers
        myGrid.handlePassengers()

        # Handle all drivers
        myGrid.handleDrivers()

        myGrid.drawGrid()

if __name__ == "__main__":
    main()