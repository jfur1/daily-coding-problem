# Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.

# For example, given the following preorder traversal:

# [a, b, d, e, c, f, g]

# And the following inorder traversal:

# [d, b, e, a, f, c, g]

# You should return the following tree:

#     a
#    / \
#   b   c
#  / \ / \
# d  e f  g

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def constructTree(preOrder, inOrder, start, end):
    if start > end:
        return None

    # Select the current node from preOrder traversal
    node = Node(preOrder[constructTree.preIndex])
    constructTree.preIndex += 1

    # If the node has no children, then return
    if start == end:
        return node
    
    # Else, find the index of the node from inOrder traversal
    index = search(inOrder, start, end, node.data)

    # Using the index from the InOrder traversal, construct left and right subtrees recursively
    node.left = constructTree(preOrder, inOrder, start, index-1)
    node.right = constructTree(preOrder, inOrder, index+1, end)

    return node
     
# Utility Functions

def search(arr, start, end, val):
    for i in range(start, end+1):
        if arr[i] == val:
            return i

def inOrderPrint(root):
    if root is None:
        return -1
    
    inOrderPrint(root.left)

    print(root.data)

    inOrderPrint(root.right)

inOrder = ['d', 'b', 'e', 'a', 'f', 'c', 'g']
preOrder = ['a', 'b', 'd', 'e', 'c', 'f', 'g']
constructTree.preIndex = 0
root = constructTree(preOrder, inOrder, 0, len(inOrder)-1)
print("In order traversal of the resulting tree:")
inOrderPrint(root)
