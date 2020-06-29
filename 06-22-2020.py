# Given an integer n, find the next biggest integer with the same number of 1-bits on.
# For example, given the number 6 (0110 in binary), return 9 (1001).
# Help from GeeksforGeeks

# Author: John Furlong

def nextNum(n):
    next = 0
    if(n):

        # right-most set bit
        rightBit = n & -(n)

        # Clear the right side string of 1's and set the bit immediately to the left of the string of 1's
        nextHighestBit = n + int(rightBit)

        # Reset the right most bits
        rightBits = n ^ int(nextHighestBit)

        # Adjust the string of 1's to the right-most extreme
        rightBits = (int(rightBits) / int(rightBit))

        # Correction factor -- undo shift from addition
        rightBits = int(rightBits) >> 2

        # Add the left and right string of bits
        next = nextHighestBit | rightBits

    return next

print("Next highest number with the same number of set bits: ", end='')
print(nextNum(156))