# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given the head of a singly linked list, reverse it in-place.

# Iterative and Recusive Solutions included:
# Time Complexity: O(n)
# Space Complexity: O(1)

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def recursiveReverse(self, head):
        if head is None or head.next is None:
            return head

        rest = self.recursiveReverse(head.next)

        head.next.next = head
        head.next = None

        return rest
    
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

# Driver Code
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)
print("Iterative Solution:")
print("Given Linked List:")
llist.printList()
llist.reverse()
print("\nReversed Linked List:")
llist.printList()
print()
# Recursive Implementation Driver Code
llist2 = LinkedList()
llist2.push(20)
llist2.push(4)
llist2.push(15)
llist2.push(85)
print("Recursive Solution:")
print("Given Linked List:")
llist2.printList()
llist2.head = llist2.recursiveReverse(llist2.head)
print("Reversed Linked List:")
llist2.printList()