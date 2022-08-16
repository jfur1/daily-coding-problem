
# Good morning! Here's your coding interview problem for today.

# This problem was asked by Stripe.

# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

# You can modify the input array in-place.

def smallestInteger(nums):
    smallest = float("inf")
    seen = dict()

    for i in range(0, len(nums)):
        if nums[i] < 1:
            continue
        else:
            smallest = min(smallest, nums[i])
            if nums[i] not in seen:
                seen[nums[i]] = True
    
    smallest += 1

    while smallest in seen:
        smallest += 1
            
    return smallest


nums = [3, 4, -1, 1]
nums2 = [1, 2, 0] 
print("first missing positive integer: ",smallestInteger(nums2))
