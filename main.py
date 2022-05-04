from Grid import Grid

# Intialize Constants

SCREEN_SIZE = 1000
GRID_SIZE = 50

IMPORT_GRID = "testGrid.txt"
DESTINATION_SAVE_GRID = "savedGrid.txt"

MAX_DRIVERS = 3                         # Maximum drivers within the grid at a time
STARTING_RANDOM_PASSENGERS = 3          # Starting passengers in grid

def main():
    # Create Grid Object
    myGrid = Grid(SCREEN_SIZE, GRID_SIZE)
    myGrid.createGrid()
    myGrid.importGrid(DESTINATION_SAVE_GRID)

    # Instantiate Drivers and Initial Passengers
    myGrid.addDrivers(MAX_DRIVERS)
    myGrid.addPassengers(STARTING_RANDOM_PASSENGERS)

    while True:
        # Handle all button pressed events
        myGrid.handleButtonPressedEvent()

        # Handle all mouse click events
        myGrid.handleMousePressedEvent()

        # Handle passengers
        myGrid.handlePassengers()

        # Handle all drivers
        myGrid.handleDrivers()

        # Update Grid Drawing
        myGrid.drawGrid()

if __name__ == "__main__":
    main()