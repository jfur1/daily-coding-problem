# Given an array of integers in which two elements appear exactly once and all other elements appear exactly twice, find the two elements that appear only once.

# For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8. The order does not matter.

# Follow-up: Can you do this in linear time and constant space?

# Author: John Furlong
# Date: June 12, 2020
import numpy as np

# Approach 1: Brute Force
# Time Complexity = O(n log n) -> Dominated by the sorted() function
def findTwo(arr):
    res = []
    arr = sorted(arr)
    for i in range(1, len(arr)-1):
        if(arr[i] != arr[i-1]) and (arr[i] != arr[i+1]):
            res.append(arr[i])
    print("The two non-repeating numbers are: ", res[0], res[1])
    return

arr = [2, 4, 6, 8, 10, 2, 6, 10]
print('Approach 1: ')
findTwo(arr)

# Approach 2: Follow-up in linear time & constant space:
# Idea: n (XOR) n = 0  =>  The two set bits of the total xor coorespond to the different bits between x and y.
def findTwo2(arr):
    res = arr[0]
    x, y = 0, 0
    # Store the XOR of all the elements
    for i in range(1, len(arr)):
        res = res ^ arr[i]
    # Get the rightmost set bit
    set_bit = res & ~(res-1) 
    # Compare rightmost set bit to respective positions throughout the array
    # One will have the same bit set, and another without that bit set
    for i in range(0, len(arr)):
        # Matching set bits => Undo the xor
        if(arr[i] & set_bit):
            x = x ^ arr[i]
        # Bit not set => Undo xor
        else:
            y = y ^ arr[i]
    print('The two non-repeating numbers are: ', x, y)
    return x, y

print('Approach 2: ')
findTwo2(arr)
# This algorithm takes O(n) (linear) time, and requires 0(1) (constant) space
# This is because the function loops through the array twice, but constants are dropped from
# time complexity. Similarly, we store the results in the first index of the array, which is
# why our space complexity is constant -- 0(1).