# Describe an algorithm to compute the longest increasing subsequence of an array of numbers in O(n log n) time.

# Approach 1: Recursion

# Global Var to store max
global maximum

# Utility function
def LIS_Utility(arr, n):
    
    # Get access to maximum
    global maximum

    # Base Case
    if n == 1: return 1

    maxEnd = 1

    # Recursively get all LIS
    for i in range(1, n):
        res = LIS_Utility(arr, i)
        if arr[i-1] < arr[n-1] and res+1 > maxEnd:
            maxEnd = res + 1
    
    # Compare maxEnd with overall maximum
    maximum = max(maximum, maxEnd)

    return maxEnd

def LIS(arr):

    # Get access to global var
    global maximum

    n = len(arr)
    maximum = 1

    LIS_Utility(arr, n)

    return maximum

arr = [9, 23, 8, 34, 22, 49, 42, 66]
print("Length of the Longest Increasing Subsequence in the array (Method 1): ", arr)
print(LIS(arr))

#   Time Complexity: O(n^n)
#       - Overlapping subproblems in our recursion tree leaves us with exponential runtime! The recursive approach is computationally expensive; however,
#         the space requirement is constant, since there is no work done outside of the recursive function calls.

#   Space Complexity: O(1)

# -----------------------------------------------------------------------------------------

# Second Approach: Dynamic Programming
#   Another solution to this problem is dynamic programming, which makes use of the fact that we have overlapping subproblems. 
#   More specifically, we will be using memoization to avoid repeated computations, and therefore improve our runtime.

def lis(arr):
    n = len(arr)

    # Array to keep track of the current subsequence
    lis = [1] * n

    # Compute the LIS values in bottum-up DP fashion
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    maximum = 0

    # Pick the max of all values in LIS
    for i in range(n):
        maximum = max(maximum, lis[i])

    return maximum

print("Length of the Longest Increasing Subsequence in the array (Method 2): ", arr)
print(lis(arr))

# Time Complexity: O(n^2)
#   - We have decreased our runtime from exponential to quadratic, through the use of memoization
#   - The quadratic runtime stems from the nested loop -- Inner-most statement is executed n^2 times!

# Space Complexity:
#   - The extra space required for this solution is O(n), because we are storing up to N elements in the lis array