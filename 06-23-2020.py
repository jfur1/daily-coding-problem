# Author: John Furlong
# Given a binary search tree, find the floor and ceiling of a given integer.
# The floor is the highest element in the tree less than or equal to an integer, 
# while the ceiling is the lowest element in the tree greater than or equal to an integer.

# If either value does not exist, return None.

# Binary Search Tree
class Node:
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None

# Function returns the ceiling
def ceiling(root, n):
    
    # Base Case:
    if root == None:
        return -1

    # Found equal key
    if root.key == n:
        return root.key

    # If the root < target, ceiling must be in the right subtree
    if root.key < n:
        return ceiling(root.right, n)

    # Otherwise, the ceiling could be in either subtree
    val = ceiling(root.left, n)

    return val if val >= n else root.key

# Function returns the floor
def floor(root, n):
    
    # Base Case:
    if root == None:
        return -1

    # Found equal key
    if root.key == n:
        return root.key

    # If the root > target, floor must be in the left subtree
    if root.key > n:
        return floor(root.left, n)

    # Otherwise, the floor could be in either the root or the right subtree
    else:
        val = floor(root.right, n)
        if val == -1 or val > n:
            return root.key
        else:
            return val


# Test tree
#       8
#      / \
#     4   12
#    / \  / \
#   2  6  10  14

root = Node(8) 
  
root.left = Node(4) 
root.right = Node(12) 
  
root.left.left = Node(2) 
root.left.right = Node(6) 
  
root.right.left = Node(10) 
root.right.right = Node(14) 
  
for i in range(16): 
    print('Value:', i)
    print('Ceiling Value:', ceiling(root, i))
    print('Floor Value:', floor(root, i))
    print()