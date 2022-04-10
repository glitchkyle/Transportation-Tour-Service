def findPathAStar(gridArr, height, width, startPos, endPos):
    print(f" Finding Path from {startPos} to {endPos}")

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
            print("Path Found!")
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
        
        for node in adjacentNodes:
            if node in closedList:
                continue
            if node.getWall():
                continue

            node.setGCost(currentGCost + 10)

            x1, y1 = node.getGridPos()
            x2, y2 = endPos
            heuristicDistance = calculateManhattanDistance(x1, y1, x2, y2)
            node.setHCost(heuristicDistance)

            node.setParentNode(currentSearchNode)

            for openNode in openList:
                if node == openNode and node.getGCost() > node.getGCost():
                    continue

            openList.append(node)

            # print(f"Node is at: {node.getGridPos()}. Node costs {node.getFCost()}")
        
        # Sort open list to make cheapest node on top
        # heapifySort(openList)

    return finalPath

def heapifyMin(nodeArr, size, i):

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
    startIndex = len(nodeArr) // 2 - 1
    for i in range(startIndex, -1, -1):
        heapifyMin(nodeArr, len(nodeArr), i)

def findCheapestNode(lst):
    cheapestNode = lst[0]
    cheapestVal = lst[0].getFCost()
    for node in lst:
        if node.getFCost() < cheapestVal:
            cheapestNode = node
    return cheapestNode

# Calculate Manhattan distance between two points (x,y)
def calculateManhattanDistance(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)