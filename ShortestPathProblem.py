import numpy as np

def solution (src, dest):
    ##Define Board
    res = []
    for i in range(8):
        res.append(np.arange(8*i, 8*(i+1)))

    res = np.array(res)

    ##Define Coordinates for Board for OutofBounds Checking
    boardCoord = []
    for i in range(8):
        for j in range(8):
            coordinate = (i,j)
            boardCoord.append(coordinate)
    ##
    StartCoordinatesTuple = np.where(res == src)
    DestinationCoordTuple = np.where(res == dest)
    StartCoord = list(zip(StartCoordinatesTuple[0],StartCoordinatesTuple[1]))
    DestinationCoord = list(zip(DestinationCoordTuple[0],DestinationCoordTuple[1]))

    visitedNodes = []
    unvisitedNodes = []
    visitedNodesCoord = []
    unvisitedNodesCoord = []

    distance = 0
    StartCoordandDistance = StartCoord[0]
    unvisitedNodes.append(StartCoordandDistance+(distance,))
    unvisitedNodesCoord.append(StartCoordandDistance)
    
    while DestinationCoord[0] not in unvisitedNodesCoord:  
        FindNeighbour(unvisitedNodes[0],boardCoord,visitedNodes,unvisitedNodes,visitedNodesCoord,unvisitedNodesCoord)

    index = unvisitedNodesCoord.index(DestinationCoord[0])
    LocationShortDist = unvisitedNodes[index]
    ShortestDistance = LocationShortDist[2]    
 
    return ShortestDistance 
               
         
def FindNeighbour(StartCoordinate,boardCoordinates,visitedNodes,unvisitedNodes,visitedNodesCoord,unvisitedNodesCoord):
    ## negative will denote moving in left direction, positive is moving in right direction for X
    ## negative will denote moving in up direction, positive is moving in down direction for Y
    ## Define array of possible moves first column is x-direction, second is y-direction
    defineMoves = [(-1,2),
                   (-1,-2),
                   (1,2),
                   (1,-2),
                   (2,1),
                   (2,-1),
                   (-2,1),
                   (-2,-1)]

    distance = StartCoordinate[2]
    StartCoordandDistance = (StartCoordinate[0],StartCoordinate[1],distance)
    visitedNodes.append(StartCoordandDistance) ##Visited Nodes Now store Coordinates and Distance

    StartCoord = (StartCoordinate[0],StartCoordinate[1])
    visitedNodesCoord.append(StartCoord) ##VisitedNodesCoordinate stores just coordinates of visited locations
    
    for i in range(len(defineMoves)):
        possibleCoordinate = (StartCoordinate[0]+defineMoves[i][0],StartCoordinate[1]+defineMoves[i][1]) ##Check all 8 possible moves
        if(possibleCoordinate in boardCoordinates): ##Check boundary conditions
            if (possibleCoordinate not in visitedNodesCoord): ##Check if node has been visited before
                distance += 1
                unvisitedNodesCoord.append(possibleCoordinate)
                possibleCoordinate = possibleCoordinate + (distance,)              
                unvisitedNodes.append(possibleCoordinate)
                distance = StartCoordinate[2]
                
    for each in unvisitedNodes: ##Removing visited nodes from unvisited nodes
        if each in visitedNodes:
            unvisitedNodes.remove(each)

    for each in unvisitedNodesCoord: ##Removing visited nodes from unvisited nodes
        if each in visitedNodesCoord:
            unvisitedNodesCoord.remove(each)
    
    return unvisitedNodes

start = 8
destination = 52
print(solution(start,destination))