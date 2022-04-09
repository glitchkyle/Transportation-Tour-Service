def findPathAStar(gridArr, startNode, endNode):
    finalPath = []
    openList = []
    closedList = []

    openList.append(startNode)

    while len(openList) > 0:
        currentOpenListLength = len(openList)

        currentSearchNode = openList[0]
        # Remove current search node from list 
        # Sort list
        closedList.append(currentSearchNode)

    return finalPath

def heapifyMin(nodeArr, size, i):

    # Index position of arrrays as a tree
    largest = i                 # Root
    left = 2 * i + 1            # Left Child
    right = 2 * i + 2           # Right Child

    #if left < size and nodeArr[left]  

    pass

def heapifySort(nodeArr, size):
    startIndex = size // 2 - 1
    for i in range(startIndex, -1, -1):
        heapifyMin(nodeArr, size, i)