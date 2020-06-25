# # A competitive runner would like to create a route that starts and ends at his house,
# # with the condition that the route goes entirely uphill at first, and then entirely downhill.

# # Given a dictionary of places of the form {location: elevation}, 
# # and a dictionary mapping paths between some of these locations to their corresponding distances, 
# # find the length of the shortest route satisfying the condition above. Assume the runner's home is location 0.

# # For example, suppose you are given the following input:

# # elevations = {0: 5, 1: 25, 2: 15, 3: 20, 4: 10}
# # paths = {
# #     (0, 1): 10,
# #     (0, 2): 8,
# #     (0, 3): 15,
# #     (1, 3): 12,
# #     (2, 4): 10,
# #     (3, 4): 5,
# #     (3, 0): 17,
# #     (4, 0): 10
# # }
# # In this case, the shortest valid path would be 0 -> 2 -> 4 -> 0, with a distance of 28.
# import sys

# elevations = {0: 5, 1: 25, 2: 15, 3: 20, 4: 10}
# paths = {
#     (0, 1): 10,
#     (0, 2): 8,
#     (0, 3): 15,
#     (1, 3): 12,
#     (2, 4): 10,
#     (3, 4): 5,
#     (3, 0): 17,
#     (4, 0): 10
# }

# def path(previous, s):
#     if s is None:
#         return []
#     else:
#         return path(previous, previous[s]) + [s]

# # Helper function to convert dictionary into adjacency list format
# def shortestPath(elevations, paths, source):
#     # Each key is a vertex, which maps to a list of (neighbor, distance) tuples.
#     #  { location : [ (neighbor : distance) ] }
#     adjDict = dict()
#     for path, distance in paths.items():
#         start, end = path[0], path[1]  
        
#         if start not in adjDict.keys():
#             adjDict[start] = []
#         adjDict[start].append((end, distance))
#     #return adjDict
#     currentPath = []
#     currentPath.append(source)
#     bestPath = []
#     visited = []

#     bestWeight = shortestPathFinder(elevations, adjDict, currentPath, source, 0, visited, source, False, bestPath, 1000000)
#     print(bestWeight)
#     return

# def shortestPathFinder(elevations, adjDict, currentPath, currentNode, currentSum, visited, source, descending, bestPath, bestPathCost):
#     currentBest = bestPathCost

#     # Starting at the source, for all adjacent vertices, check for valid paths, updating path & pathcost along the way
#     for neighbor, distance in adjDict[currentNode]:
#         print("Current Node: ", currentNode)
#         # Goal Test:
#         if(neighbor == source):
#             if(elevations[neighbor] < elevations[currentNode]):
#                 if(currentSum + distance < currentBest):
#                     bestPath.clear()
#                     bestPath = currentPath
#                     currentBest = currentSum + distance
#                     print("Current best cost: ", currentBest)
#         else:
#             expectDescend = elevations.get(neighbor) < elevations.get(currentNode)
#             isValid = not descending or (descending and expectDescend)
#             if isValid:
#                 visited.append(neighbor)
#                 currentPath.append(neighbor)
#                 currentBest = shortestPathFinder(elevations, adjDict, currentPath, neighbor, currentSum+distance, visited, source, expectDescend, bestPath, currentBest)
#                 currentPath.remove(neighbor)
#                 visited.remove(neighbor)

#     return currentBest


# shortestPath(elevations, paths, 0)







# A competitive runner would like to create a route that starts and ends at his house,
# with the condition that the route goes entirely uphill at first, and then entirely downhill.

# Given a dictionary of places of the form {location: elevation}, 
# and a dictionary mapping paths between some of these locations to their corresponding distances, 
# find the length of the shortest route satisfying the condition above. Assume the runner's home is location 0.

# For example, suppose you are given the following input:

# elevations = {0: 5, 1: 25, 2: 15, 3: 20, 4: 10}
# paths = {
#     (0, 1): 10,
#     (0, 2): 8,
#     (0, 3): 15,
#     (1, 3): 12,
#     (2, 4): 10,
#     (3, 4): 5,
#     (3, 0): 17,
#     (4, 0): 10
# }
# In this case, the shortest valid path would be 0 -> 2 -> 4 -> 0, with a distance of 28.
import sys

elevations = {0: 5, 1: 25, 2: 15, 3: 20, 4: 10}
paths = {
    (0, 1): 10,
    (0, 2): 8,
    (0, 3): 15,
    (1, 3): 12,
    (2, 4): 10,
    (3, 4): 5,
    (3, 0): 17,
    (4, 0): 10
}

def printPath(route):
    for i in range(0, len(route)-1):
        print(route[i], '-> ', end='')
    print(route[len(route)-1])

# Helper function to convert dictionary into adjacency list format
def shortestPath(elevations, paths, source):
    # Each key is a vertex, which maps to a list of (neighbor, distance) tuples.
    #  { location : [ (neighbor : distance) ] }
    adjDict = dict()
    for path, distance in paths.items():
        start, end = path[0], path[1]  
        
        if start not in adjDict.keys():
            adjDict[start] = []
        adjDict[start].append((end, distance))
    #return adjDict
    currentPath = []
    currentPath.append(source)
    bestPath = []

    cost, route = shortestPathFinder(elevations, adjDict, currentPath, source, 0, source, False, bestPath, 1000000, [])
    print("Shortest Valid Path Route: ", end='')
    printPath(route)
    print("Shortest Valid Path Cost: ", cost)
    return

def shortestPathFinder(elevations, adjDict, currentPath, currentNode, currentSum, source, descending, bestPath, currentBest, route):

    # Starting at the source, for all adjacent vertices, check for valid paths, updating path & pathcost along the way
    for neighbor, distance in adjDict[currentNode]:
        #print("Current Node: ", currentNode)

        # Goal Test:
        if(neighbor == source):
            if(elevations[neighbor] < elevations[currentNode]):
                if(currentSum + distance < currentBest):
                    bestPath.clear()
                    bestPath = currentPath
                    currentBest = currentSum + distance
                    #print("Current best cost: ", currentBest)
                    bestPath.append(source)
                    #print("Current best path: ", bestPath)
                    route = bestPath.copy()
                    bestPath.remove(source)
        else:
            expectDescend = elevations.get(neighbor) < elevations.get(currentNode)
            isValid = not descending or (descending and expectDescend)
            if isValid:
                currentPath.append(neighbor)
                currentBest, route = shortestPathFinder(elevations, adjDict, currentPath, neighbor, currentSum+distance, source, expectDescend, bestPath, currentBest, route)
                currentPath.remove(neighbor)

    return currentBest, route


shortestPath(elevations, paths, 0)