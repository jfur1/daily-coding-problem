# Good morning! Here's your coding interview problem for today.

# This problem was recently asked by Google.

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?
# --------------------------------------------------------


# Brute Force: nested loop
def twoNums(nums, k):
    for i in range(0, len(nums)):
        for j in range(i, len(nums)):
            if nums[j] + nums[i] == k:
                return True
    return False

nums = [10, 15, 3, 7]
k = 17
# print(twoNums(nums, k))

# One pass: hash map
def onePass(nums, k):
    flag = False
    hash = dict()
    for i in range(0, len(nums)):
        if k - nums[i] in hash:
            flag = True
        if nums[i] not in hash:
            hash[nums[i]] = True
    return flag
        

print(onePass(nums, k))