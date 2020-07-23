# Let's represent an integer in a linked list format by having each node represent a digit in the number. 
# The nodes make up the number in reversed order.

# For example, the following linked list:

# 1 -> 2 -> 3 -> 4 -> 5
# is the number 54321.

# Given two linked lists in this format, return their sum in the same linked list format.

# For example, given

# 9 -> 9
# 5 -> 2
# return 124 (99 + 25) as:

# 4 -> 2 -> 1

# Node class 
class Node: 

    # Function to initialise the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize next as null 
  
  
# Linked List class contains a Node object 
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
    
    # This function prints contents of linked list 
    # starting from head 
    def printList(self): 
        temp = self.head 
        while (temp): 
            if temp.next is None:
                print(temp.data)
                break
            print (temp.data,' -> ' , end = '') 
            temp = temp.next

def num_to_list(num):
    # Convert the integer into a list of digits
    digits = [int(digit) for digit in str(num)]
    llist = LinkedList()
    llist.head = Node(digits[len(digits)-1])
    tmp = llist.head
    # For each digit in our list starting from the end, convert into a linked list
    for i in range(len(digits)-2, -1, -1):
        if i == 0:
            tmp.next = Node(digits[i])
            break
        tmp.next = Node(digits[i])
        tmp = tmp.next
    llist.printList()
    # Return the linked list
    return llist

def add_lists(list1, list2):
    num1 = num2 = 0
    i = j = 0
    tmp = list1.head
    # Get digits from the first linked list => store base-10 decimal value
    while(tmp is not None):
        num1 += (tmp.data) * (10 ** i)
        tmp = tmp.next
        i += 1
    tmp2 = list2.head
    # Get digits from second linked list => store base-10 decimal value
    while tmp2 is not None:
        num2 += (tmp2.data) * (10 ** j)
        tmp2 = tmp2.next
        j += 1
    num = num1 + num2
    num_to_list(num)
    return

# Code execution starts here 
if __name__=='__main__': 
  
    # Initialize the 2 example lists
    list1 = LinkedList() 
    list2 = LinkedList()

    list1.head = Node(9)
    list1second = Node(9)
    list1.head.next = list1second

    list2.head = Node(5)
    list2second = Node(2)
    list2.head.next = list2second

    add_lists(list1, list2)
