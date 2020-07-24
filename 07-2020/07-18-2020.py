# A rule looks like this:

# A NE B

# This means this means point A is located northeast of point B.

# A SW C

# means that point A is southwest of C.

# Given a list of rules, check if the sum of the rules validate. For example:

# A N B
# B NE C
# C N A
# does not validate, since A cannot be both north and south of C.

# A NW B
# A N B
# is considered valid.

class Node:
    def __init__(self, node, direction, adj):
        self.node = node
        self.direction = direction
        self.adjNode = adj
        self.adj = dict()

class Graph:
    def __init__(self, vertices):
        self.nodes = vertices

def validate(arr):
    # Cartesian Coordinate Deltas
    delta_x = [-1, -1, 0, 1, 1, 1, 0, -1]
    delta_y = [0, 1, 1, 1, 0, -1, -1, -1]

    for line in arr:
        node = Node(line[0], line[1], line[2])

    

arr = [ ['A', 'N', 'B'],
        ['B', 'NE', 'C'], 
        ['C', 'N', 'A'] ]