from Grid import Grid

# Intialize Constants
SCREEN_SIZE = 800
GRID_SIZE = 20
MAX_DRIVERS = 3
MAX_RANDOM_PASSENGERS = 3
MAX_DESTINATIONS = 3
IMPORT_GRID = "testGrid.txt"

def test():
    myGrid = Grid(SCREEN_SIZE, GRID_SIZE)
    myGrid.createGrid()
    myGrid.importGrid(IMPORT_GRID)
    myGrid.addDrivers(MAX_DRIVERS)
    myGrid.addRandomPassengers(MAX_RANDOM_PASSENGERS, MAX_DESTINATIONS)

    while True:
        for event in myGrid.getGridEvent():

            # Handle all key and click events
            myGrid.handleMousePressedEvent()
            myGrid.handleButtonPressedEvent(event)

        # Handle all drivers
        myGrid.handleDrivers()

        myGrid.drawGrid()


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
    test()