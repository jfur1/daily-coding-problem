# The transitive closure of a graph is a measure of which vertices are reachable from other vertices. 
# It can be represented as a matrix M, where M[i][j] == 1 if there is a path between vertices i and j, and otherwise 0.

# For example, suppose we are given the following graph in adjacency list form:

# graph = [
#     [0, 1, 3],
#     [1, 2],
#     [2],
#     [3]
# ]
# The transitive closure of this graph would be:

# [1, 1, 0, 1]
# [0, 1, 1, 0]
# [0, 0, 1, 0]
# [0, 0, 0, 1]
# Given a graph, find its transitive closure.

def listToMatrix(list):
    n = len(list)
    matrix = [[0 for x in range(0, n)] for y in range(0, n)]

    for i in range(0, len(list)):
        for j in range(0, len(list[i])):
            idx_j = list[i][j]
            matrix[i][idx_j] = 1
    return matrix

def printMatrix(matrix):
    for i in range(0, len(matrix)):
        print("[", end='')
        for j in range(0, len(matrix[i])):
            print(matrix[i][j], end='')
            if(j < len(matrix[i]) - 1):
                print(", ", end='')
        print("]")

graph = [
    [0, 1, 3],
    [1, 2],
    [2],
    [3]
]

print("Graph in adjacency list form: ")
printMatrix(graph)
transClosure = listToMatrix(graph)
print("Transitive closure of the graph: ")
printMatrix(transClosure)