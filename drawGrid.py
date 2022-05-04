from Grid import Grid

# Intialize Constants

SCREEN_SIZE = 1000
GRID_SIZE = 20

IMPORT_GRID = "testGrid.txt"
DESTINATION_SAVE_GRID = "savedGrid.txt"

MAX_DRIVERS = 3                         # Maximum drivers within the grid at a time
STARTING_RANDOM_PASSENGERS = 3          # Starting passengers in grid

def main():
    """
    Function for creating or drawing new grid to be imported 
    """
    myGrid = Grid(SCREEN_SIZE, GRID_SIZE)
    myGrid.createGrid()
    myGrid.importGrid(DESTINATION_SAVE_GRID)

    while True:

        # Handle all key and click events
        myGrid.handleMousePressedEvent()
        myGrid.handleButtonPressedEvent()

        myGrid.drawGrid()

if __name__ == "__main__":
    main()