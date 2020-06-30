# Author: John Furlong
# Implement 3 stacks using a single list:

# class Stack:
#     def __init__(self):
#         self.list = []

#     def pop(self, stack_number):
#         pass

#     def push(self, item, stack_number):
#         pass

class Stack:
    # Constructor
    def __init__(self):
        self.list = []
        # List of 3 stack pointers -- Index 0 is None so we can use given stack_num as ptr index
        self.stackPtrs = [None, -1, -1, -1]

    # Pop the top item off of the given stack
    def pop(self, stack_num):
        if self.isEmpty(stack_num):
            print("Stack: ", stack_num, "is empty!")
            return
        # Get the pointer from the given stack_num, then pop the item and decrease the ptr
        self.list.pop(self.stackPtrs[stack_num])
        if stack_num == 1:
            self.stackPtrs[1] -= 1
            self.stackPtrs[2] -= 1
            self.stackPtrs[3] -= 1
        elif stack_num == 2:
            self.stackPtrs[2] -= 1
            self.stackPtrs[3] -= 1
        else:
            self.stackPtrs[3] -= 1

    # Pushes an item onto a given stack
    def push(self, item, stack_num):
        # The indexes to stacks 2 & 3 change depending on the previous stacks
        if stack_num == 1:
            self.stackPtrs[1] += 1
            self.stackPtrs[2] += 1
            self.list.insert(self.stackPtrs[1], item)
        
        elif stack_num == 2:
            # If Previous stack is empty
            if self.isEmpty(1):
                self.stackPtrs[2] = 0
                self.list.insert(0, item)
            else:
                self.stackPtrs[2] += 1
                self.list.insert(self.stackPtrs[stack_num], item)

        else:
            self.stackPtrs[3] = len(self.list)
            self.list.insert(self.stackPtrs[stack_num], item)

        #print(stack_num, '|', self.stackPtrs[stack_num])

    # Print the original list
    def printList(self):
        for item in self.list:
            print(item)

    # Print the individual stacks
    def printStacks(self):
        print('Stack 1:')
        for i in range(0, self.stackPtrs[1]+1):
            print(self.list[i])
        print('Stack 2:')
        for j in range(self.stackPtrs[1]+1, self.stackPtrs[2]+1):
            print(self.list[j])
        print('Stack 3:')
        for k in range(self.stackPtrs[2]+1, len(self.list)):
            print(self.list[k])
        print()

    # Check if a given stack is empty or not
    def isEmpty(self, stack_num):
        if self.stackPtrs[stack_num] == -1:
            return 1
        else: 
            return 0


stack = Stack()
# 3 Lists to be assembled into respective stacks
list1 = ['a', 'b', 'c', 'd', 'e', 'f']
list2 = [1, 2, 3, 4, 5, 6]
list3 = ['apples', 'bannanas', 'oranges', 'grapes', 'strawberries', 'tangerines']

# Push the lists into their stacks
for item in list1:
    stack.push(item, 1)

for item in list2:
    stack.push(item, 2)

for item in list3:
    stack.push(item, 3)

# Print the stacks after pushing data
stack.printStacks()

# Pop 2 items from stack #1
stack.pop(1)
stack.pop(1)
    
# Pop 3 items from stack #2
for i in range(3):
    stack.pop(2)

# Pop 1 item from stack #3
stack.pop(3)

print('Pop: \n\t 2 items from stack #1, \n\t 3 items from stack #2, \n\t 1 item from stack #3')
# Print after popping elements
stack.printStacks()
