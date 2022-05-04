def findPathAStar(gridArr, height, width, startPos, endPos):
    """
    Finds a path using A-star between the start position and end position in given grid

    :param gridArr: Array representation of grid. Grid attribute of Grid Object.
    :type gridArr: 2D Node Array 
    :param height: Height of grid or number of rows
    :type height: int
    :param width: Width of grid or number of columns
    :type width: int
    :param startPos: Starting Position
    :type startPos: tuple
    :param endPos: Ending Position
    :type endPos: tuple 
    :return: Final shortest path found
    :rtype: tuple array
    """
    #print(f" Finding Path from {startPos} to {endPos}")

    finalPath = []
    openList = []
    closedList = []

    startNode = gridArr[startPos[0]][startPos[1]]
    startNode.setGCost(0)
    startNode.setHCost(0)

    openList.append(startNode)

    while len(openList) > 0:

        # Remove root, cheapest node, from binary heap
        currentSearchNode = openList[0]

        # Find cheapest node using linear search
        # currentSearchNode = findCheapestNode(openList)

        openList.remove(currentSearchNode)

        # Add node to closed list
        closedList.append(currentSearchNode)

        # If path found, trace back to start node
        if currentSearchNode.getGridPos() == endPos:
            #print("Path Found!")
            while currentSearchNode != startNode:
                finalPath.append(currentSearchNode.getGridPos())
                currentSearchNode = currentSearchNode.getParentNode()
            finalPath.reverse()
            break

        currentGCost = currentSearchNode.getGCost()
        adjacentNodes = []
        currentRow, currentColumn = currentSearchNode.getGridPos()

        # Get all adjacent nodes to current node being searched

        # Top Center (currentRow - 1, currentColumn)
        if (currentRow - 1 >= 0 and currentRow - 1 < height) and (currentColumn >= 0 and currentColumn < width):
            searchNode = gridArr[currentRow - 1][currentColumn]
            adjacentNodes.append(searchNode)

        # Middle Left (currentRow, currentColumn - 1)
        if (currentRow >= 0 and currentRow < height) and (currentColumn - 1 >= 0 and currentColumn - 1 < width):
            searchNode = gridArr[currentRow][currentColumn - 1]
            adjacentNodes.append(searchNode)

        # Middle Right (currentRow, currentColumn + 1)
        if (currentRow >= 0 and currentRow < height) and (currentColumn + 1 >= 0 and currentColumn + 1 < width):
            searchNode = gridArr[currentRow][currentColumn + 1]
            adjacentNodes.append(searchNode)

        # Bottom Center (currentRow + 1, currentColumn)
        if (currentRow + 1 >= 0 and currentRow + 1 < height) and (currentColumn >= 0 and currentColumn < width):
            searchNode = gridArr[currentRow + 1][currentColumn]
            adjacentNodes.append(searchNode)
        
        # Process all children
        for node in adjacentNodes:
            # Skip if child has already been processed
            if node in closedList:
                continue
            # Skip if child is a wall 
            if node.isWall():
                continue
            
            # Assign cost from start to current node
            node.setGCost(currentGCost + 10)

            # Assign cost from current node to end node
            x1, y1 = node.getGridPos()
            x2, y2 = endPos
            heuristicDistance = calculateManhattanDistance(x1, y1, x2, y2)
            node.setHCost(heuristicDistance)

            # Check if node already in openlist
            if node in openList:
                continue

            # Assign parent
            node.setParentNode(currentSearchNode)

            openList.append(node)

            # print(f"Node is at: {node.getGridPos()}. Node costs {node.getFCost()}")
        
        # Sort open list to make cheapest node on top
        heapifySort(openList)

    return finalPath

def heapifyMin(nodeArr, size, i):
    """
    Sorts node array as a binary heap with cheapest node on top

    :param nodeArr: Node array to be sorted as binary heap
    :type nodeArr: Node Array
    :param size: Size of overall array
    :type size: int 
    :param i: Index of root in subtree
    :type i: int
    """

    # Index position of arrrays as a tree
    smallest = i                # Root
    left = 2 * i + 1            # Left Child
    right = 2 * i + 2           # Right Child

    # If left child is smaller than root
    if left < size and nodeArr[left].getFCost() < nodeArr[smallest].getFCost():
        smallest = left

    # If right child is smaller than root
    if right < size and nodeArr[right].getFCost() < nodeArr[smallest].getFCost():
        smallest = right

    # If smallest is not the current root, switch current root to smallest
    if smallest != i:
        nodeArr[smallest], nodeArr[i] = nodeArr[i], nodeArr[smallest]
        heapifyMin(nodeArr, size, smallest)

def heapifySort(nodeArr):
    """
    Recursively sorts given node array until cheapest node is root

    :param nodeArr: Node array to be sorted as a binary heap
    :type nodeArr: Node Array
    """
    startIndex = len(nodeArr) // 2 - 1
    for i in range(startIndex, -1, -1):
        heapifyMin(nodeArr, len(nodeArr), i)

def findCheapestNode(lst):
    """
    Linearly search for the cheapest node 

    :param lst: Node array to be searched
    :type lst: Node Array
    """
    cheapestNode = lst[0]
    cheapestVal = lst[0].getFCost()
    for node in lst:
        if node.getFCost() < cheapestVal:
            cheapestNode = node
    return cheapestNode

def calculateManhattanDistance(x1, y1, x2, y2):
    """
    Finds the Manhattan Distance between two points

    :param x1: X position of initial point
    :type x1: int
    :param y1: Y position of initial point 
    :type y1: int 
    :param x2: X position of final point
    :type x2: int 
    :param y2: Y position of final point
    :type y2: int
    :return: Manhattan Distance of two given points
    :rtype: int
    """
    return abs(x2 - x1) + abs(y2 - y1)