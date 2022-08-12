# Good morning! Here's your coding interview problem for today.

# This problem was asked by Uber.

# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?

# Brute Force: Nested loop to calculate product for each index
# Runtime: O(N^2)
# Aux Space: O(N)
from re import L


def transformArray(nums):
    newArr = []
    val = None
    for i in range(0, len(nums)):
        val = None
        for j in range(0, len(nums)):
            if i == j: continue
            if val is None: 
                val = nums[j]
            else:
                val *= nums[j]
                
        newArr.append(val)
    
    return newArr    


nums = [1, 2, 3, 4, 5]
nums2 = [3, 2, 1]
print('[1, 2, 3, 4, 5] => ',transformArray(nums))
print('[3, 2, 1] => ',transformArray(nums2))

# Optimization Goal < O(N^2)
# Runtime: O(N)
# Aux Space: O(N)
def quickTransform(nums):
    totalProduct = 1
    newArr = []
    for i in range(0, len(nums)):
        totalProduct *= nums[i]
    
    for i in range(0, len(nums)):
        newArr.append(int(totalProduct / nums[i]))

    return newArr

print("quickTransform([1, 2, 3, 4, 5]) ==> ", quickTransform(nums))
